import requests
import json

webhook_url = 'http://localhost:5000/webhook'

data = { 'name': 'jason', 'description': 'some desc' }

r = requests.post(webhook_url, data=json.dumps(data), headers={'Content-Type': 'application/json'})
