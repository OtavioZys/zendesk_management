from django.shortcuts import render
import psycopg2
import json
import pandas as pd
from numpy import NAN, NaN, number
from cmath import nan
from django.contrib.auth.decorators import login_required
from apps.zendesk.models import TicketAudits, TicketFormatado, TicketMetric, GatilhosAtivos, MacrosAtivas, \
    AutomacoesAtivas, SLAsAtivas
from apps.zendesk.getters import get_audit, get_ticketID, get_ticket
from apps.zendesk.zendesk_log import zendesk_log, checa_id
from apps.zendesk.funcoes import get_requests, get_metrics, get_activeTriggers, get_activeAutomations, \
    get_activeMacros, get_slaPolicies


@login_required
def index_zendesk(request):
    lista_ids_nan = []
    lista_requestersIDS = []
    file = pd.read_excel(r'C:\Users\otavio.zys\Desktop\zendesk\testes\usuarios_perdidos.xlsx')
    dict_file = file.to_dict('list')
    cont = 0
    for item in (dict_file['id']):
        requester_id = item
        if requester_id is nan or requester_id is NaN or requester_id is NAN:
            lista_ids_nan.append(requester_id)
        elif requester_id != nan and requester_id != NaN and requester_id != NAN:
            lista_requestersIDS.append(int(requester_id))
        else:
            print(requester_id)
        cont = cont + 1

    lista_requesterTickets = []
    cont1 = 1
    for value in lista_requestersIDS:
        lista_requesterTickets = get_ticketID(value)
        if lista_requesterTickets == 0:
            print(f"Requester {value} sem tickets!")
            pass
        else:
            for item in lista_requesterTickets:
                lista = json.dumps(get_audit(item))
                if lista == 0:
                    print(f"Audit do ticket {item} falhou.")
                    pass
                else:
                    TicketAudits.objects.using('default').create(
                        ticket_id=item,
                        ticket_audit=lista,
                        ticket_userID=value
                    )
                    print(f"Requester {value}: audit do Ticket {item}. Inserções: {cont1}")
                    cont1 = cont1 + 1

    context = {'audit': lista_requesterTickets}

    return render(request, 'zendesk/index.html', context)


@login_required
def formata_ticket(request):
    lista_ids_nan = []
    lista_requestersIDS = []
    file = pd.read_excel(r'C:\Users\otavio.zys\Desktop\zendesk\testes\usuarios_perdidos.xlsx')
    dict_file = file.to_dict('list')
    cont = 0
    for item in (dict_file['id']):
        requester_id = item
        if requester_id is nan or requester_id is NaN or requester_id is NAN:
            lista_ids_nan.append(requester_id)
        elif requester_id != nan and requester_id != NaN and requester_id != NAN:
            lista_requestersIDS.append(int(requester_id))
        else:
            print(requester_id)
        cont = cont + 1

    lista_requesterTickets = []
    cont1 = 1
    for value in lista_requestersIDS:
        lista_requesterTickets = get_ticketID(value)
        if lista_requesterTickets == 0:
            print(f"Requester {value} sem tickets!")
            pass
        else:
            for item in lista_requesterTickets:
                formatado = get_ticket(item)
                TicketFormatado.objects.using('default').create(
                    ticket_id=item,
                    ticket_formatado=formatado
                )
                print(f"Requester {value}: Ticket #{item} formatado. Inserções: {cont1}")
                cont1 = cont1 + 1

    context = {'formatado': lista_requesterTickets}

    return render(request, 'zendesk/formata_ticket.html', context)


@login_required
def regras_ativas(request):
    lista_regras = []
    gatilhos = get_activeTriggers()
    automacoes = get_activeAutomations()
    macros = get_activeMacros()
    slas = get_slaPolicies()
    lista_gatilhos = []
    for gatilho in gatilhos:
        GatilhosAtivos.objects.using('default').create(
            gatilho_id=gatilho['id'],
            gatilho_titulo=gatilho['title'],
            gatilho_body=gatilho
        )
        trigger = {'Gatilho': gatilho['id'], 'Nome': gatilho['title']}
        lista_gatilhos.append(trigger)
    lista_automacoes = []
    for automacao in automacoes:
        AutomacoesAtivas.objects.using('default').create(
            automacoes_id=automacao['id'],
            automacoes_titulo=automacao['title'],
            automacoes_body=automacao
        )
        automation = {'Automação': automacao['id'], 'Nome': automacao['title']}
        lista_automacoes.append(automation)
    lista_macros = []
    for macro in macros:
        MacrosAtivas.objects.using('default').create(
            macro_id=macro['id'],
            macro_titulo=macro['title'],
            macro_body=macro
        )
        macro1 = {'Macro': macro['id'], 'Nome': macro['title']}
        lista_macros.append(macro1)
    lista_slas = []
    for sla in slas:
        SLAsAtivas.objects.using('default').create(
            sla_id=sla['id'],
            sla_titulo=sla['title'],
            sla_body=sla
        )
        sla1 = {'SLA': sla['id'], 'Nome': sla['title']}
        lista_slas.append(sla1)

    lista_regras = lista_gatilhos + lista_automacoes + lista_macros + lista_slas

    context = {'regras': lista_regras}

    return render(request, 'zendesk/regras_ativas.html', context)


@login_required
def zendesk_logs(request):
    def get_segundo():
        segundo = int(datetime.now().strftime('%S'))

        return segundo

    agora = get_segundo()
    while agora < 60:
        novo_agora = get_segundo()
        if novo_agora == 15 or novo_agora == 30 or novo_agora == 45 or novo_agora == 59:
            pass
        else:
            teste = get_log()
            created = teste['id']
            checa = checa_id(created)
            if checa:
                pass
            else:
                print(get_log())

    return render(request, 'zendesk/logs.html', context)

# Create your views here.
