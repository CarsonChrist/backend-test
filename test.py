import requests

# Requests identical to the points.pdf example
requests.post('http://localhost:5000/transaction', data={"payer": "DANNON", "points": 1000, "timestamp": "2020-11-02T14:00:00Z" })
requests.post('http://localhost:5000/transaction', data={"payer": "UNILEVER", "points": 200, "timestamp": "2020-10-31T11:00:00Z" })
requests.post('http://localhost:5000/transaction', data={"payer": "DANNON", "points": -200, "timestamp": "2020-10-31T15:00:00Z"})
requests.post('http://localhost:5000/transaction', data={"payer": "MILLER COORS", "points": 10000, "timestamp": "2020-11-01T14:00:00Z"})
requests.post('http://localhost:5000/transaction', data={"payer": "DANNON", "points": 300, "timestamp": "2020-10-31T10:00:00Z"})
r = requests.post('http://localhost:5000/spend', data={"points": 5000})

# Print the list of points spent to complete the spend POST request
print(r.json())

r = requests.get('http://localhost:5000/balance')

# Print the list of payers and their total points to complete the balance GET request
print(r.json())