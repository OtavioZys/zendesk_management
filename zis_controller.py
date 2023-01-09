
tags = ticket_event['tags']
via = ticket_event['']
canal = via['channel']



if canal == 'WhatsApp' or canal == 'API':
    tags = ticket_event['tags']
    for item in tags:
        if item == 'chatbot_autoatendimento':
            ticket_id.append(ticket_event['ticket']['id'])