from transaction import Transaction
from linked_list import LinkedList
from exceptions import NegativePointException

# Point tracking class that is implemented by app.py
class PointTracker:

    # Default constructor
    def __init__(self):
        # Linked list for containing transaction order
        self._transactions = LinkedList()

        # Dictionary storing updated payer and point totals
        self._payer_totals = {}  # payer: total points
    
    # Add transaction to linked list and update dictionary
    def add_transaction(self, transaction):
        if transaction.get_payer() in self._payer_totals:
            if transaction.get_points() + self._payer_totals[transaction.get_payer()] < 0:
                raise NegativePointException()
            else:
                self._payer_totals[transaction.get_payer()] += transaction.get_points()
                self._transactions.insert(transaction)
        else:           
            if transaction.get_points() < 0:
                raise NegativePointException()
            else:
                self._payer_totals[transaction.get_payer()] = transaction.get_points()
                self._transactions.insert(transaction)

    # Spend points by iterating through transaction linked list until
    # the amount of points are spent, then update payer totals dictionary
    # and return the transaction order dictionary
    def spend(self, points):
        if int(points) > self.total():
            raise NegativePointException()
        remaining = int(points)
        order = {}  # payer: points spent
        for node in self._transactions.iterate():
            temp_points = node.value.get_points()
            temp_payer = node.value.get_payer()
            if temp_points > remaining:
                node.value.set_points(temp_points - remaining)
                if temp_payer in order.keys():
                    order[temp_payer] += -1 * remaining
                else:
                    order[temp_payer] = -1 * remaining
                self._payer_totals[temp_payer] -= remaining
                remaining = 0
                break
            else:
                if temp_payer in order.keys():
                    order[temp_payer] += -1 * temp_points
                else:
                    order[temp_payer] = -1 * temp_points
                self._payer_totals[temp_payer] -= temp_points
                self._transactions.remove_head()
                remaining -= temp_points
                if remaining == 0:
                    break
                
        # Return transaction order for spent points
        order_list = []
        for payer in order:
            order_list.append({"payer": payer, "points": order[payer]})
        return order_list

    # Return payers and their total points
    def balance(self):       
        return self._payer_totals

    # Return aggregate point total
    def total(self):
        total = 0
        for i in self._payer_totals.values():
            total += i
        return total