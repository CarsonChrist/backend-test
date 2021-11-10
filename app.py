import json
from flask import Flask
from flask import request
from exceptions import NegativePointException
from point_tracker import PointTracker
from transaction import Transaction

app = Flask(__name__)

point_tracker = PointTracker()

# POST route to add a transaction
@app.route("/transaction", methods = ["post"])
def add_transaction():
    transaction = Transaction(request.values.get("payer"), int(request.values.get("points")), request.values.get("timestamp"))
    try:
        point_tracker.add_transaction(transaction)
    except NegativePointException as e:
        return str(e), 400
    return "" 

# POST route to spend points
# returns the payers and points spent
@app.route("/spend", methods = ["post"])
def spend():
    try:
        order_list = point_tracker.spend(request.values.get("points"))
    except NegativePointException as e:
        return str(e), 400
    return json.dumps(order_list)

# GET route to return balance of payers and their total points
@app.route("/balance")
def balance():    
    return point_tracker.balance()

app.run()