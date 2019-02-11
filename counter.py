from bill import Bill
from inventory import update_inventory


class Counter(object):

    def __init__(self, customer, stock):
        self.customer = customer
        self.stock = stock
        self.bill = Bill()

    def checkout(self):
        # For all the items in the cart
        # Create a bill
        # Update the stock

        for item in self.customer.cart.items:
            # Populate the neccessary details
            item.category = self.stock[item.item_name]['category']
            item.cost_price = self.stock[item.item_name]['cost_price']
            item.selling_price = self.stock[item.item_name]['selling_price']
            item.stock_identifier = self.stock[item.item_name]['stock_identifier']

            # Update the stock
            update_inventory(item)

            # Add item to bill
            self.bill.add_item_to_bill(item)

        # Returning bill object
        return self.bill
