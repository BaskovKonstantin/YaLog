import requests
import json
payload =   {'level': 'INFO', 'message': 'TEST MESSAGE'}
payload = json.dumps(payload)
payload = json.loads(payload)

r =  requests.post('http://127.0.0.1:5000/log', json=payload)