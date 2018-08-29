import csv
from twilio.rest import Client 
from secrets import account_sid, auth_token

client = Client(account_sid, auth_token) 

with open('club.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['Name'], row['Phone Number'], row['Grade'])






# message = client.messages.create( 
#                                 from_='+18065135906',
#                                 body='body',     
#                                 to='+18066762209'
#                             ) 