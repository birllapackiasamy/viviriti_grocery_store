import datetime
from tabulate import tabulate


class Bill(object):

    def __init__(self):
        self.bill_no = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        self.bill_items = []
        self.bill_amount = 0
        self.headers = ["Item name", "Quantity", "Price"]


    def add_item_to_bill(self, item):
        self.bill_items.append(item)
        self.bill_amount += item.selling_price * item.item_count

    def print_bill(self):
        print "Bill Details:"
        print "-------------"
        print "Dear Customer, Thanks for shopping with us. Please find below the bill details"
        print ""
        print "Bill No: {} Date: {}".format(self.bill_no, str(datetime.datetime.now().date()))

        bill_list=[]
        total_quantity = 0
        total_price = 0
        for each in self.bill_items:
            total_quantity += each.item_count
            total_price += each.selling_price
            bill_list.append([each.item_name, each.item_count, each.selling_price])
        bill_list.append(["total", total_quantity, total_price])
        print tabulate(bill_list, self.headers, tablefmt='psql')



