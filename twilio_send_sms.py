from twilio.rest import TwilioRestClient
#Don't share your secrets!
account_sid = "{{ account_sid }}" # Your Account SID from www.twilio.com/console
auth_token  = "{{ auth_token }}"  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)

#Note: The number +12345678901 is unverified. Trial accounts cannot send messages to unverified numbers;
message = client.messages.create(body="Hello from Python",
    to="+12345678901",    # Replace with your phone number
    from_="+12345678901") # Replace with your Twilio number

print(message.sid)
