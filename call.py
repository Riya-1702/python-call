from twilio.rest import Client

# Twilio credentials
account_sid = ''
auth_token = ''
twilio_number = ''
to_number = input("Enter the number to call (with country code): ")

# Initialize client
client = Client(account_sid, auth_token)

# Make the call
call = client.calls.create(
    to=to_number,
    from_=twilio_number,
    twiml='<Response><Say>Hello! This is a test call from Twilio using Python. Have a great day!</Say></Response>'
)

print(f"Call initiated! SID: {call.sid}")
