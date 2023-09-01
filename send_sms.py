from twilio.rest import Client
from config import settings
account_sid = settings.account_sid
auth_token = settings.auth_token
client = Client(account_sid, auth_token) 

def send_sms(msg):
    message = client.api.account.messages.create(  
                                messaging_service_sid='MG2cb312a626e6b74bb58da5f65709dda1', 
                                body=msg,      
                                to='+917792839346' 
                            )
    return 

def send_sms_mukesh(msg):
    message = client.api.account.messages.create(  
                                messaging_service_sid='MG2cb312a626e6b74bb58da5f65709dda1', 
                                body=msg,      
                                to='+916375469992' 
                            )
    return
