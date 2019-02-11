from cart import cart
from item import item

class customer(object):

    def __init__(self, fname, lname, age, mobile, company, address):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.mobile = mobile
        self.company = company
        self.address = address
        self.cart = cart()

    def add_item_to_cart(self):
        self.cart.items.append(item(
            name="table", count=1
        ))
        self.cart.items.append(item(
            name="carrot", count=1
        ))

    def start_shopping(self):
        self.add_item_to_cart()
