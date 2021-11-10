import requests
requests.post('http://localhost:5000/transaction', data={"payer": "DANNON", "points": 1000, "timestamp": "2020-11-02T14:00:00Z" })
requests.post('http://localhost:5000/transaction', data={"payer": "UNILEVER", "points": 200, "timestamp": "2020-10-31T11:00:00Z" })
requests.post('http://localhost:5000/transaction', data={"payer": "DANNON", "points": -200, "timestamp": "2020-10-31T15:00:00Z"})
requests.post('http://localhost:5000/transaction', data={"payer": "MILLER COORS", "points": 10000, "timestamp": "2020-11-01T14:00:00Z"})
requests.post('http://localhost:5000/transaction', data={"payer": "DANNON", "points": 300, "timestamp": "2020-10-31T10:00:00Z"})
r = requests.post('http://localhost:5000/spend', data={"points": 5000})
print(r.json())
r = requests.get('http://localhost:5000/balance')
print(r.json())