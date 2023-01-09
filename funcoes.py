from integracoes_card.settings import ZENDESK_SUBDOMAIN_OTAVIO, ZENDESK_B64_OTAVIO, ZENDESK_EMAIL_OTAVIO, \
    ZENDESK_TOKEN_OTAVIO, ZENDESK_SUBDOMAIN_OTAVIO
from apps.zendesk.getters import get_zenpyCredentials
from zenpy import Zenpy
import requests
import json

zenpy_client = Zenpy(**get_zenpyCredentials())


def get_requests(user_id):
    url = f"https://{ZENDESK_SUBDOMAIN_OTAVIO}.zendesk.com/api/v2/users/{user_id}/requests.json"
    payload = {}
    headers = {
        'Authorization': ZENDESK_B64_OTAVIO,
        'Cookie': '__cfruid=35f1912526043ae5f474b9fe5ae8e56bcfdb2c4f-1669820706; '
                  '_zendesk_cookie=BAhJIhl7ImRldmljZV90b2tlbnMiOnt9fQY6BkVU--459ed01949a36415c1716b5711271c3d08918307'
                  '; '
                  '_zendesk_session'
                  '=bTZod3UvZUNzejlpTi9EV09LcTJyU09tR3lCSm9ZZXNwRi9kZndVVk43U05NSVRDTVBqUjRDaWg3OXpSRlBuR1B5S2gxUU9hV04xd0pUd25VMkc2aU9KTHdoR3NDYW9HSFpnNmErbnFZUXpJWU1SSmJockhxWXlpQm0wOHkvZDEtLWNmMFJOby9ybjJiclFFZ0NkNGo0SHc9PQ%3D%3D--d2e853f94b6bd65bcf758d5b8271febb01381b78 '
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    return response.json()


def get_metrics(ticket_id):
    url = f"https://{ZENDESK_SUBDOMAIN_OTAVIO}.zendesk.com/api/v2/tickets/{ticket_id}/metrics"
    payload = {}
    headers = {
        'Authorization': ZENDESK_B64_OTAVIO,
        'Cookie': '__cfruid=35f1912526043ae5f474b9fe5ae8e56bcfdb2c4f-1669820706; '
                  '_zendesk_cookie=BAhJIhl7ImRldmljZV90b2tlbnMiOnt9fQY6BkVU--459ed01949a36415c1716b5711271c3d08918307'
                  '; '
                  '_zendesk_session'
                  '=bTZod3UvZUNzejlpTi9EV09LcTJyU09tR3lCSm9ZZXNwRi9kZndVVk43U05NSVRDTVBqUjRDaWg3OXpSRlBuR1B5S2gxUU9hV04xd0pUd25VMkc2aU9KTHdoR3NDYW9HSFpnNmErbnFZUXpJWU1SSmJockhxWXlpQm0wOHkvZDEtLWNmMFJOby9ybjJiclFFZ0NkNGo0SHc9PQ%3D%3D--d2e853f94b6bd65bcf758d5b8271febb01381b78 '
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    return response.json()


def get_activeTriggers():
    url = f"https://{ZENDESK_SUBDOMAIN_OTAVIO}.zendesk.com/api/v2/triggers/active"
    payload = {}
    headers = {
        'Authorization': ZENDESK_B64_OTAVIO,
        'Cookie': '__cfruid=35f1912526043ae5f474b9fe5ae8e56bcfdb2c4f-1669820706; '
                  '_zendesk_cookie=BAhJIhl7ImRldmljZV90b2tlbnMiOnt9fQY6BkVU--459ed01949a36415c1716b5711271c3d08918307'
                  '; '
                  '_zendesk_session'
                  '=bTZod3UvZUNzejlpTi9EV09LcTJyU09tR3lCSm9ZZXNwRi9kZndVVk43U05NSVRDTVBqUjRDaWg3OXpSRlBuR1B5S2gxUU9hV04xd0pUd25VMkc2aU9KTHdoR3NDYW9HSFpnNmErbnFZUXpJWU1SSmJockhxWXlpQm0wOHkvZDEtLWNmMFJOby9ybjJiclFFZ0NkNGo0SHc9PQ%3D%3D--d2e853f94b6bd65bcf758d5b8271febb01381b78 '
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    resposta = response.json()
    gatilhos = resposta['triggers']

    return gatilhos


def get_activeAutomations():
    url = f"https://{ZENDESK_SUBDOMAIN_OTAVIO}.zendesk.com/api/v2/automations/active"
    payload = {}
    headers = {
        'Authorization': ZENDESK_B64_OTAVIO,
        'Cookie': '__cfruid=35f1912526043ae5f474b9fe5ae8e56bcfdb2c4f-1669820706; '
                  '_zendesk_cookie=BAhJIhl7ImRldmljZV90b2tlbnMiOnt9fQY6BkVU--459ed01949a36415c1716b5711271c3d08918307'
                  '; '
                  '_zendesk_session'
                  '=bTZod3UvZUNzejlpTi9EV09LcTJyU09tR3lCSm9ZZXNwRi9kZndVVk43U05NSVRDTVBqUjRDaWg3OXpSRlBuR1B5S2gxUU9hV04xd0pUd25VMkc2aU9KTHdoR3NDYW9HSFpnNmErbnFZUXpJWU1SSmJockhxWXlpQm0wOHkvZDEtLWNmMFJOby9ybjJiclFFZ0NkNGo0SHc9PQ%3D%3D--d2e853f94b6bd65bcf758d5b8271febb01381b78 '
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    resposta = response.json()
    automacoes = resposta['automations']

    return automacoes


def get_activeMacros():
    url = f"https://{ZENDESK_SUBDOMAIN_OTAVIO}.zendesk.com/api/v2/macros/active"
    payload = {}
    headers = {
        'Authorization': ZENDESK_B64_OTAVIO,
        'Cookie': '__cfruid=35f1912526043ae5f474b9fe5ae8e56bcfdb2c4f-1669820706; '
                  '_zendesk_cookie=BAhJIhl7ImRldmljZV90b2tlbnMiOnt9fQY6BkVU--459ed01949a36415c1716b5711271c3d08918307'
                  '; '
                  '_zendesk_session'
                  '=bTZod3UvZUNzejlpTi9EV09LcTJyU09tR3lCSm9ZZXNwRi9kZndVVk43U05NSVRDTVBqUjRDaWg3OXpSRlBuR1B5S2gxUU9hV04xd0pUd25VMkc2aU9KTHdoR3NDYW9HSFpnNmErbnFZUXpJWU1SSmJockhxWXlpQm0wOHkvZDEtLWNmMFJOby9ybjJiclFFZ0NkNGo0SHc9PQ%3D%3D--d2e853f94b6bd65bcf758d5b8271febb01381b78 '
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    resposta = response.json()
    macros = resposta['macros']

    return macros


def get_slaPolicies():
    url = f"https://{ZENDESK_SUBDOMAIN_OTAVIO}.zendesk.com/api/v2/slas/policies"
    payload = {}
    headers = {
        'Authorization': ZENDESK_B64_OTAVIO,
        'Cookie': '__cfruid=35f1912526043ae5f474b9fe5ae8e56bcfdb2c4f-1669820706; '
                  '_zendesk_cookie=BAhJIhl7ImRldmljZV90b2tlbnMiOnt9fQY6BkVU--459ed01949a36415c1716b5711271c3d08918307'
                  '; '
                  '_zendesk_session'
                  '=bTZod3UvZUNzejlpTi9EV09LcTJyU09tR3lCSm9ZZXNwRi9kZndVVk43U05NSVRDTVBqUjRDaWg3OXpSRlBuR1B5S2gxUU9hV04xd0pUd25VMkc2aU9KTHdoR3NDYW9HSFpnNmErbnFZUXpJWU1SSmJockhxWXlpQm0wOHkvZDEtLWNmMFJOby9ybjJiclFFZ0NkNGo0SHc9PQ%3D%3D--d2e853f94b6bd65bcf758d5b8271febb01381b78 '
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    resposta = response.json()
    slas = resposta['sla_policies']

    return slas
