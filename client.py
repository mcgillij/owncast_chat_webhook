import requests
import json

webhook_url = 'http://localhost:5000/webhook'

data = {'eventData': {'body': 'f',
               'id': 'MHLpo7Hng',
               'rawBody': 'f',
               'timestamp': '2021-09-20T23:02:54.980066719Z',
               'user': {'createdAt': '2021-09-20T22:34:33.139297191Z',
                        'displayColor': 22,
                        'displayName': 'mcgillij',
                        'id': 'avyQt7N7R',
                        'previousNames': ['mcgillij']},
               'visible': True},
         'type': 'CHAT'}

r = requests.post(webhook_url, data=json.dumps(data), headers={'Content-Type': 'application/json'})
