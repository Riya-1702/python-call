from twilio.rest import Client

# Twilio credentials
account_sid = 'AC235cb59aa9b6ea74f3a5eacd50650797'
auth_token = '0a5a298c0d8eeab10c1b6c0beb564ccc'
twilio_number = '+17755499097'
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
