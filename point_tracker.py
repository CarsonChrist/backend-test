from transaction import Transaction
from linked_list import LinkedList
from exceptions import NegativePointException

class PointTracker:

    def __init__(self):
        # data structure for transactions
        self._transactions = LinkedList()

        # dict of payer and total
        self._payer_totals = {}  # payer: total points
    
    # add transaction
    def add_transaction(self, transaction):

        #update payer totals
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

    # spend points
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
                
        # return transaction order
        order_list = []
        for payer in order:
            order_list.append({"payer": payer, "points": order[payer]})
        return order_list

    # return payers and their total points
    def balance(self):       
        return self._payer_totals

    # return aggregate point total
    def total(self):
        total = 0
        for i in self._payer_totals.values():
            total += i
        return total

# pt = PointTracker()
# t1 = Transaction("DANNON", 1000, "2020-11-02T14:00:00Z" )
# t2 = Transaction("UNILEVER", 200, "2020-10-31T11:00:00Z")
# t3 = Transaction("DANNON", -200, "2020-10-31T15:00:00Z")
# # t4 = Transaction("MILLER COORS", 10000, "2020-11-01T14:00:00Z")
# # t5 = Transaction("DANNON", 300, "2020-10-31T10:00:00Z")
# pt.add_transaction(t1)
# pt.add_transaction(t2)
# pt.add_transaction(t3)
# # pt.add_transaction(t4)
# # pt.add_transaction(t5)
# pt._transactions.list()
# print(pt.spend(5000))
# print(pt.balance())