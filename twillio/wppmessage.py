from functions import *

# Substitua suas credenciais por variáveis de ambiente para segurança
account_sid = 'ACc9dc8a5cc02c30e74881a86c11ddd6a7'
auth_token = 'd3f01ca344351af1c88b3575ab7e85f3'

twillio = Twillio(account_sid, auth_token)
# twillio.send_wpp_message('whatsapp:+14155238886', 'whatsapp:+5511941400110', 'DISSE QUE TO USANDO CARAI')

messages = twillio.historical_wpp_message('whatsapp:+5511941400110')
print(messages)