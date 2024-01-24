import os

from twilio.rest import Client

account_sid = 'ACf0c9d42b2c1e3b702635dd92c2e53d0a'
auth_token = '[AuthToken]'
client = Client(account_sid, auth_token)

message = client.messages.create(
  to='+97517744848',
  from_='+12065650695',
  body="012230020053"

  
)


print(message.sid)