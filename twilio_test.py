from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACb01b3ec9462c0f18d74eabcb1f0869bb"
# Your Auth Token from twilio.com/console
auth_token  = "4a49e9f6ea4e59c5cd382141d0b31626"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+13207604424",
    from_="+13203570095",
    body="Hello from Python!")

print(message.sid)
