import json
from flask import Flask
from flask import request
from exceptions import NegativePointException
from point_tracker import PointTracker
from transaction import Transaction

app = Flask(__name__)

point_tracker = PointTracker()

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/transaction", methods = ["post"])
def add_transaction():
    transaction = Transaction(request.values.get("payer"), int(request.values.get("points")), request.values.get("timestamp"))
    try:
        point_tracker.add_transaction(transaction)
    except NegativePointException as e:
        return str(e), 400
    return "" 

@app.route("/spend", methods = ["post"])
def spend():
    try:
        order_list = point_tracker.spend(request.values.get("points"))
    except NegativePointException as e:
        return str(e), 400
    return json.dumps(order_list)

@app.route("/balance")
def balance():    
    return point_tracker.balance()

app.run()