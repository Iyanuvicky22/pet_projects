# from twilio.rest import Client
# account_sid = 'AC5a689976060463841370923128d9d5a6'
# auth_token = '[AuthToken]'
# client = Client(account_sid, auth_token)
# message = client.messages.create(
#   messaging_service_sid='MG615e4dee778a2c9b48d86b31c4efdc59',
#   body='Ahoy 👋',
#   to='+18777804236'
# )
# print(message.sid)

import re

username = "apotiks224"
pattern = re.compile(r'^[a-z][a-z0-9-]{1,32}$')

print(pattern.match(username) is not None)
