from twilio.rest import Client

# Substitua suas credenciais por variáveis de ambiente para segurança
account_sid = 'ACc9dc8a5cc02c30e74881a86c11ddd6a7'
auth_token = 'd3f01ca344351af1c88b3575ab7e85f3'

client = Client(account_sid, auth_token)

# Enviar mensagem
message = client.messages.create(
    from_='whatsapp:+14155238886',
    body='Olá, esta é uma mensagem enviada via Twilio!',
    to='whatsapp:+5511941400110'
)

print(f"Mensagem enviada! SID: {message.sid}")
