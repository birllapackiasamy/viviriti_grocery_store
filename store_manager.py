from multiprocessing import Process

import inventory

from customer import customer
from counter import Counter


class StoreManager(object):

    def __init__(self):
        # Initializing the Grocery Store
        self.stock = inventory.stock
        self.days_transactions= []
        print "Welcome to Vivira Grocery Store"
        print "--------------------------------"
        inventory.print_inventory()

    def intialize_customer(self):
        # Creating Customer Object for purchase
        return customer(
            fname="Birlla",
            lname="Packiasamy",
            age=27,
            company="Gain Credit",
            mobile=8888888888,
            address="Pallikarnai, Chennai"
        )

    def open_shop(self, **kwargs):
        # Initalize customer
        cus = self.intialize_customer()
        # Customer Shopping
        cus.start_shopping()
        # Genreating bill from cart
        bill_details = Counter(cus, self.stock).checkout()
        # Printing the bill
        bill_details.print_bill()
        # Adding bill details to global list for tracking
        self.days_transactions.append(bill_details)

        # Initalize customer
        cus2 = self.intialize_customer()
        # Customer Shopping
        cus2.start_shopping()
        # Genreating bill from cart
        bill_details = Counter(cus2, self.stock).checkout()
        # Printing the bill
        bill_details.print_bill()
        # Adding bill details to global list for tracking
        self.days_transactions.append(bill_details)

    def print_transaction_history(self):
        total_bill = 0
        total_items = {}
        for each_bill in self.days_transactions:
            total_bill += each_bill.bill_amount
        print "Total Sale: {}".format(total_bill)

    def close_shop(self):
        print ""
        print "Closing Store, Summary of transactions: "
        self.print_transaction_history()
        print ""
        inventory.print_inventory()

if __name__ == "__main__":
    sm = StoreManager()
    sm.open_shop()
    sm.close_shop()
