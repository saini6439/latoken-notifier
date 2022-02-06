from twilio.rest import Client
from config import settings
account_sid = settings.account_sid
auth_token = settings.auth_token
client = Client(account_sid, auth_token) 

def send_sms(msg):
    message = client.api.account.messages.create(  
                                messaging_service_sid='MG78d527f0a5e19ef93a15178c3942f41d', 
                                body=msg,      
                                to='+919785466389' 
                            )
    return 