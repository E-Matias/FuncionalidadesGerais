from twilio.rest import Client

class Twillio:
    def __init__(self, account_sid:str, auth_token:str):
        self.client: Client = Client(account_sid, auth_token)
    
    def send_wpp_message(self, sender:str, receiver:str, content:str):
        self.client.messages.create(
            from_=sender,
            body=content,
            to=receiver
        )
    
    def historical_wpp_message(self, receiver:str):
        infos:list = []
        messages:list = self.client.messages.list(from_=receiver)
        for message in messages:
            info:dict = {"data": message.date_sent, "to": message.to, "body": message.body,"status": message.status}
            infos.append(info)
        return infos

