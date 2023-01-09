from integracoes_card.settings import ZENDESK_SUBDOMAIN_OTAVIO, ZENDESK_B64_OTAVIO, ZENDESK_EMAIL_OTAVIO, \
    ZENDESK_TOKEN_OTAVIO, ZENDESK_SUBDOMAIN_OTAVIO
from zenpy import Zenpy
import requests
import json


# RETORNA AS CREDENCIAIS ZENDESK PARA USAR NA API DO ZENPY
def get_zenpyCredentials():
    credentials = {
        'email': ZENDESK_EMAIL_OTAVIO,
        'token': ZENDESK_TOKEN_OTAVIO,
        'subdomain': ZENDESK_SUBDOMAIN_OTAVIO
    }

    return credentials


####################################################### TICKETS #######################################################
# RETORNA O JSON COMPLETO DO TICKET
def get_ticketAPI(ticketid):
    url = f"https://{ZENDESK_SUBDOMAIN_OTAVIO}.zendesk.com/api/v2/tickets/{ticketid}"
    payload = {}
    headers = {
        'Authorization': ZENDESK_B64_OTAVIO,
        'Cookie': '__cfruid=35f1912526043ae5f474b9fe5ae8e56bcfdb2c4f-1669820706; '
                  '_zendesk_cookie=BAhJIhl7ImRldmljZV90b2tlbnMiOnt9fQY6BkVU--459ed01949a36415c1716b5711271c3d08918307 '
    }

    response = requests.request('GET', url, headers=headers, data=payload)

    return response.json()


def get_ticket(ticket_id):
    zenpy_client = Zenpy(**get_zenpyCredentials())
    ticket = zenpy_client.tickets(id=ticket_id)
    dicio = {
        'Ticket': ticket.id,
        'Emissor': {
            'Nome': get_ticketSubmitterName(ticket_id),
            'ID': get_ticketSubmitterId(ticket_id),
            'E-mail': get_ticketSubmitterEmail(ticket_id),
            'Localização': get_ticketSubmitterLocale(ticket_id),
            'Função': get_ticketSubmitterRole(ticket_id)
        },
        'Solicitante': {
            'Nome': get_ticketRequesterName(ticket_id),
            'ID': get_ticketRequesterId(ticket_id),
            'E-mail': get_ticketRequesterEmail(ticket_id),
            'Localização': get_ticketRequesterLocale(ticket_id),
            'Função': get_ticketRequesterRole(ticket_id)
        },
        'Data de Criação': get_criacaoTicket(ticket_id),
        'Privacidade': get_ticketPrivacy(ticket_id),
        'Grupo': {
            'ID': get_ticketGroupId(ticket_id),
            'Nome': get_ticketGroupName(ticket_id)
        },
        'Marca': {
            'ID': get_ticketBrandId(ticket_id),
            'Nome': get_ticketBrandName(ticket_id)
        },
        'Organização': {
            'ID': get_ticketOrgId(ticket_id),
            'Nome': get_ticketOrgName(ticket_id),
            'Código SGV': get_ticketOrgSGV(ticket_id)
        },
        'Assunto': get_ticketSubject(ticket_id),
        'Descrição': get_ticketDescription(ticket_id),
        'ID externa do Ticket': get_ticketExternalId(ticket_id)
    }
    dicio_json = json.dumps(dicio)

    return dicio_json


# BUSCA O AUDIT DO TICKET INFORMADO
def get_audit(ticketID):
    url = f"https://{ZENDESK_SUBDOMAIN_OTAVIO}.zendesk.com/api/v2/tickets/{ticketID}/audits"
    payload = {}
    headers = {
        'Authorization': ZENDESK_B64_OTAVIO,
        'Cookie': '__cfruid=35f1912526043ae5f474b9fe5ae8e56bcfdb2c4f-1669820706; '
                  '_zendesk_cookie=BAhJIhl7ImRldmljZV90b2tlbnMiOnt9fQY6BkVU--459ed01949a36415c1716b5711271c3d08918307 '
    }

    response = requests.request('GET', url, headers=headers, data=payload)
    if response.status_code == 200:
        return response.json()
    else:
        return ''


# BUSCA TODOS OS TICKETS DO USUÁRIO INFORMADO
def get_ticketID(requester):
    lista_ids = []
    try:
        zenpy_client = Zenpy(**get_zenpyCredentials())
        requester_tickets = zenpy_client.search(type='ticket', requester_id=requester)
        for ticket in requester_tickets:
            lista_ids.append(ticket.id)
        return lista_ids
    except Exception as error:
        print(error)
        return ''


def get_ticketSubject(ticket_id):
    try:
        zenpy_client = Zenpy(**get_zenpyCredentials())
        ticket = zenpy_client.tickets(id=ticket_id)
        ticket_subject = ticket.subject

        return ticket_subject
    except Exception as error:
        print(error)
        return ''


def get_ticketDescription(ticket_id):
    try:
        zenpy_client = Zenpy(**get_zenpyCredentials())
        ticket = zenpy_client.tickets(id=ticket_id)
        ticket_description = ticket.description

        return ticket_description
    except Exception as error:
        print(error)
        return ''


def get_ticketExternalId(ticket_id):
    try:
        zenpy_client = Zenpy(**get_zenpyCredentials())
        ticket = zenpy_client.tickets(id=ticket_id)
        if ticket.external_id is None:
            ext_id = "Sem ID externa"
        else:
            ext_id = ticket.external_id

        return ext_id
    except Exception as error:
        print(error)
        return ''


# RETORNA O DATETIME DE CRIAÇÃO DO TICKET
def get_criacaoTicket(ticket_id):
    try:
        zenpy_client = Zenpy(**get_zenpyCredentials())
        ticket = zenpy_client.tickets(id=ticket_id)
        ticket_birthdate = ticket.created_at

        return ticket_birthdate
    except Exception as error:
        print(error)
        return ''


# RETORNA A DESCRIÇÃO DO TICKET
def get_ticketDescription(ticket_id):
    try:
        zenpy_client = Zenpy(**get_zenpyCredentials())
        ticket = zenpy_client.tickets(id=ticket_id)
        ticket_description = ticket.description

        return ticket_description
    except Exception as error:
        print(error)
        return ''


# RETORNA O ID EXTERNO DO TICKET, QUANDO EXISTE
def get_ticketExternalId(ticket_id):
    try:
        zenpy_client = Zenpy(**get_zenpyCredentials())
        ticket = zenpy_client.tickets(id=ticket_id)
        ticket_externalID = ticket.external_id
        if ticket_externalID is None:
            return ''
        else:
            return ticket_externalID
    except Exception as error:
        print(error)
        return ''


# RETORNA PRIVACIDADE DO TICKET
def get_ticketPrivacy(ticket_id):
    try:
        zenpy_client = Zenpy(**get_zenpyCredentials())
        ticket = zenpy_client.tickets(id=ticket_id)
        ticket_privacy = ticket.is_public
        if ticket_privacy:
            return "Ticket Público"
        else:
            return "Ticket Privado!"
    except Exception as error:
        print(error)
        return ''


# RETORNA O ID DO GRUPO AO QUAL O TICKET É ASSOCIADO
def get_ticketGroupId(ticket_id):
    try:
        zenpy_client = Zenpy(**get_zenpyCredentials())
        ticket = zenpy_client.tickets(id=ticket_id)
        group_id = ticket.group.id

        return group_id
    except Exception as error:
        print(error)
        return ''


# RETORNA O NOME DO GRUPO AO QUAL O TICKET É ASSOCIADO
def get_ticketGroupName(ticket_id):
    try:
        zenpy_client = Zenpy(**get_zenpyCredentials())
        ticket = zenpy_client.tickets(id=ticket_id)
        group_name = ticket.group.name

        return group_name
    except Exception as error:
        print(error)
        return ''


# RETORNA O NOME DA MARCA AO QUAL O TICKET É ASSOCIADO
def get_ticketBrandName(ticket_id):
    try:
        zenpy_client = Zenpy(**get_zenpyCredentials())
        ticket = zenpy_client.tickets(id=ticket_id)
        brand_name = ticket.brand.name

        return brand_name
    except Exception as error:
        print(error)
        return ''


# RETORNA O ID DA MARCA AO QUAL O TICKET É ASSOCIADO
def get_ticketBrandId(ticket_id):
    try:
        zenpy_client = Zenpy(**get_zenpyCredentials())
        ticket = zenpy_client.tickets(id=ticket_id)
        brand_id = ticket.brand.id

        return brand_id
    except Exception as error:
        print(error)
        return ''


############################################ ORGANIZATIONS ############################################################
# RETORNA O ID DA ORGANIZAÇÃO DO TICKET
def get_ticketOrgId(ticket_id):
    try:
        zenpy_client = Zenpy(**get_zenpyCredentials())
        ticket = zenpy_client.tickets(id=ticket_id)
        org_id = ticket.organization.id

        return org_id
    except Exception as error:
        print(error)
        return ''


# RETORNA O NOME DA ORGANIZAÇÃO DO TICKET
def get_ticketOrgName(ticket_id):
    try:
        zenpy_client = Zenpy(**get_zenpyCredentials())
        ticket = zenpy_client.tickets(id=ticket_id)
        org_name = ticket.organization.name

        return org_name
    except Exception as error:
        print(error)
        return ''


# RETORNA O CÓDIGO SGV DA ORGANIZAÇÃO DO TICKET
def get_ticketOrgSGV(ticket_id):
    try:
        zenpy_client = Zenpy(**get_zenpyCredentials())
        ticket = zenpy_client.tickets(id=ticket_id)
        org_sgv = ticket.organization.external_id

        return org_sgv
    except Exception as error:
        print(error)
        return ''


################################################## USERS ##############################################################
# RETORNA O NOME DO ATRIBUÍDO AO TICKET
def get_ticketAssigneeName(ticket_id):
    try:
        zenpy_client = Zenpy(**get_zenpyCredentials())
        ticket = zenpy_client.tickets(id=ticket_id)
        assignee_name = ticket.assignee.name

        return assignee_name
    except Exception as error:
        print(error)
        return ''


# RETORNA O ID DO ATRIBUÍDO AO TICKET
def get_ticketAssigneeId(ticket_id):
    try:
        zenpy_client = Zenpy(**get_zenpyCredentials())
        ticket = zenpy_client.tickets(id=ticket_id)
        assignee_id = ticket.assignee.id

        return assignee_id
    except Exception as error:
        print(error)
        return ''


# RETORNA O EMAIL DO ATRIBUÍDO AO TICKET
def get_ticketAssigneeEmail(ticket_id):
    try:
        zenpy_client = Zenpy(**get_zenpyCredentials())
        ticket = zenpy_client.tickets(id=ticket_id)
        assignee_email = ticket.assignee.email

        return assignee_email
    except Exception as error:
        print(error)
        return ''


# RETORNA O LOCAL DO ATRIBUÍDO AO TICKET
def get_ticketAssigneeLocale(ticket_id):
    try:
        zenpy_client = Zenpy(**get_zenpyCredentials())
        ticket = zenpy_client.tickets(id=ticket_id)
        assignee_locale = ticket.assignee.locale

        return assignee_locale
    except Exception as error:
        print(error)
        return ''


# RETORNA A FUNÇÃO DO ATRIBUÍDO AO TICKET
def get_ticketAssigneeRole(ticket_id):
    try:
        zenpy_client = Zenpy(**get_zenpyCredentials())
        ticket = zenpy_client.tickets(id=ticket_id)
        assignee_role = ticket.assignee.role

        return assignee_role
    except Exception as error:
        print(error)
        return ''


# RETORNA O NOME DO SOLICITANTE DO TICKET
def get_ticketRequesterName(ticket_id):
    try:
        zenpy_client = Zenpy(**get_zenpyCredentials())
        ticket = zenpy_client.tickets(id=ticket_id)
        requester_name = ticket.requester.name

        return requester_name
    except Exception as error:
        print(error)
        return ''


# RETORNA O ID DO SOLICITANTE DO TICKET
def get_ticketRequesterId(ticket_id):
    try:
        zenpy_client = Zenpy(**get_zenpyCredentials())
        ticket = zenpy_client.tickets(id=ticket_id)
        requester_id = ticket.requester.id

        return requester_id
    except Exception as error:
        print(error)
        return ''


# RETORNA O EMAIL DO SOLICITANTE DO TICKET
def get_ticketRequesterEmail(ticket_id):
    try:
        zenpy_client = Zenpy(**get_zenpyCredentials())
        ticket = zenpy_client.tickets(id=ticket_id)
        requester_email = ticket.requester.email

        return requester_email
    except Exception as error:
        print(error)
        return ''


# RETORNA O LOCAL DO SOLICITANTE DO TICKET
def get_ticketRequesterLocale(ticket_id):
    try:
        zenpy_client = Zenpy(**get_zenpyCredentials())
        ticket = zenpy_client.tickets(id=ticket_id)
        requester_locale = ticket.requester.locale

        return requester_locale
    except Exception as error:
        print(error)
        return ''


# RETORNA A FUNÇÃO DO SOLICITANTE DO TICKET
def get_ticketRequesterRole(ticket_id):
    try:
        zenpy_client = Zenpy(**get_zenpyCredentials())
        ticket = zenpy_client.tickets(id=ticket_id)
        requester_role = ticket.requester.role

        return requester_role
    except Exception as error:
        print(error)
        return ''


# RETORNA O NOME DO EMISSOR DO TICKET
def get_ticketSubmitterName(ticket_id):
    try:
        zenpy_client = Zenpy(**get_zenpyCredentials())
        ticket = zenpy_client.tickets(id=ticket_id)
        submitter_name = ticket.submitter.name

        return submitter_name
    except Exception as error:
        print(error)
        return ''


# RETORNA O ID DO EMISSOR DO TICKET
def get_ticketSubmitterId(ticket_id):
    try:
        zenpy_client = Zenpy(**get_zenpyCredentials())
        ticket = zenpy_client.tickets(id=ticket_id)
        submitter_id = ticket.submitter.id

        return submitter_id
    except Exception as error:
        print(error)
        return ''


# RETORNA O EMAIL DO EMISSOR DO TICKET
def get_ticketSubmitterEmail(ticket_id):
    try:
        zenpy_client = Zenpy(**get_zenpyCredentials())
        ticket = zenpy_client.tickets(id=ticket_id)
        submitter_email = ticket.submitter.email

        return submitter_email
    except Exception as error:
        print(error)
        return ''


# RETORNA O LOCAL DO EMISSOR DO TICKET
def get_ticketSubmitterLocale(ticket_id):
    try:
        zenpy_client = Zenpy(**get_zenpyCredentials())
        ticket = zenpy_client.tickets(id=ticket_id)
        submitter_locale = ticket.submitter.locale

        return submitter_locale
    except Exception as error:
        print(error)
        return ''


# RETORNA A FUNÇÃO DO EMISSOR DO TICKET
def get_ticketSubmitterRole(ticket_id):
    try:
        zenpy_client = Zenpy(**get_zenpyCredentials())
        ticket = zenpy_client.tickets(id=ticket_id)
        submitter_role = ticket.submitter.role

        return submitter_role
    except Exception as error:
        print(error)
        return ''
