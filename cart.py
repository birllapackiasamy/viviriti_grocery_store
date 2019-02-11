import inventory
from bill import Bill

class cart(object):

    def __init__(self):
        # Initalize the cart with proper ds
        self.items = []
        self.bill = Bill()

    def add_to_cart(self, item):
        # Check offers
        # Update inventory
        self.items.append(item)
        inventory.update_inventory(item)

    def remove_from_cart(self, **kwargs):
        # Update inventory
        pass

    def show_cart(self):
        pass

    def clear_cart(self):
        # Update inventory
        pass

    def checkout(self):
        for item in self.items:
            self.bill.add_item_to_bill(item)