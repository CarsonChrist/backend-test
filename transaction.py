from datetime import datetime

class Transaction:

    def __init__(self, payer, points, timestamp):
        self._payer = payer
        self._points = points
        self._timestamp = timestamp

    def __eq__(self, new_transaction):
        return (self.get_payer() == new_transaction.get_payer()) and (self.get_points() == new_transaction.get_points()) and (self.get_timestamp() == new_transaction.get_timestamp())

    def __lt__(self, new_transaction):
        return datetime.strptime(self._timestamp, '%Y-%m-%dT%H:%M:%SZ') < datetime.strptime(new_transaction.get_timestamp(), '%Y-%m-%dT%H:%M:%SZ')
    
    def __add__(self, new_transaction):
        total = self.get_points() + new_transaction.get_points()
        self.set_points(total)
        return total

    def set_points(self, new_points):
        self._points = new_points

    def get_payer(self):
        return self._payer
    
    def get_points(self):
        return self._points

    def get_timestamp(self):
        return self._timestamp

    def __str__(self):
        return f"payer: {self._payer}, points: {self._points}, timestamp: {self._timestamp}"

    def __repr__(self):
        return str(self)