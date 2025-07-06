from twilio.rest import Client
from datetime import datetime, timedelta
import time

acc_sid='' #use your account sid (34 digit) from Twilio web
auth_token=''  #Use your auth token( 32 digits) from Twilio
client= Client(acc_sid, auth_token)


def send_reminder(to, msg_body):
    try:
        msg=client.messages.create(
            body=msg_body,
            from_='whatsapp:+##########',  # Twilio sandbox number
            to=f'whatsapp:{to}' 
        )
        print(f'Message sent successfully! SID: {msg.sid}')
    except Exception as e:
        # print(f'Failed to send message: {e}')
        print('An error occurred while sending the message:')
        
name= input('Enter your receiver name: ')
to= input('Enter your receiver phone number with code (+91): ')
msg_body= input(f'Enter your message {name}: ')

# Schedule the message to be sent in 1 minute
date_str=input('Enter the date in YYYY-MM-DD format: ')
time_str=input('Enter the time in HH:MM format (24 hours): ')

send_time = datetime.now() + timedelta(minutes=1)
sehc_datetime=datetime.strptime(f"{date_str} {time_str}", "%Y-%m-%d %H:%M")

cur_date=datetime.now()
time_diff = sehc_datetime - cur_date

delay_seconds = time_diff.total_seconds()

if delay_seconds <= 0:
    print('The specified time is in the past, please enter a future time and date.')
else:
    print(f'Message scheduled to be send to {name} at {sehc_datetime}')

    time.sleep(delay_seconds)
    send_reminder(to, msg_body)
