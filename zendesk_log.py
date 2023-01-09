from integracoes_card.settings import ZENDESK_SUBDOMAIN_OTAVIO, ZENDESK_B64_OTAVIO
import requests


def zendesk_log():
    url = f"http://{ZENDESK_SUBDOMAIN_OTAVIO}.com/api/v2/audit_logs"
    payload = {}
    headers = {
        'Authorization': ZENDESK_B64_OTAVIO,
        'Cookie': '__cfruid=7ad1390d5f4202b39349e9ef8324a5d967da5bcb-1671633776; '
                  '_zendesk_cookie=BAhJIhl7ImRldmljZV90b2tlbnMiOnt9fQY6BkVU--459ed01949a36415c1716b5711271c3d08918307'
                  '; '
                  '_zendesk_session'
                  '=USsreXlSSVNZNUxTUmhCTVpuS2xDM2tEb3Z4WXZLK0x4NUQ0R1NpWWhidVgwbFFvM0pVTTBPQkZpTmNmc3llUElrUm95MnYyb2lSaFlZSW5SUm92VVhldmpZMWFHMHkzQUdtZ2tnYWNDQjFIZUZKc1o3a1JPYW1KdGtVaHU1UnQtLWM0UnNXZGhwaU1Jc3FoVThKL25aU0E9PQ%3D%3D--12016013170efa74c4b48bca9d561e5869f1b422 '
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    resposta = response.json()
    log = resposta['audit_logs']

    return log[0]


def checa_id(log_id):
    inicio = get_log()
    id_inicio = inicio['id']

    if id_inicio == log_id:
        return True
    else:
        return False
 
def segundo():
    segundo = int(datetime.now().strftime('%S'))
    
    return segundo

agora = segundo()
while agora < 60:
   novo_agora = segundo()
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
