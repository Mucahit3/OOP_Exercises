from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = ""
# Your Auth Token from twilio.com/console
auth_token  = ""

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="",     # Your phone number
    from_="",  # Your twilio phone number
    body="I love you! <3")

print(message.sid)
