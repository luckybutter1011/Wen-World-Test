import requests

TOKEN = '7188910603:AAGG-9sIlhdrZ4y4ZTcoURrl5c4jqdI3zL4'
WEBHOOK_URL = 'https://telegram-1-triend.replit.app/' + TOKEN

response = requests.get(f'https://api.telegram.org/bot{TOKEN}/setWebhook?url={WEBHOOK_URL}')
print(response.json())