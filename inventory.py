import pandas as pd
from tabulate import tabulate

stock = {
            "table": {
                "category": "furnitures",
                "stock_count": 10,
                "stock_identifier": "number",
                "cost_price": 100,
                "selling_price": 120,
            },
            "pen": {
                "category": "stationaries",
                "stock_count": 50,
                "stock_identifier": "number",
                "cost_price": 5,
                "selling_price": 6
            },
            "carrot": {
                "category": "vegetables",
                "stock_count": 10,
                "stock_identifier": "kg",
                "cost_price": 20,
                "selling_price": 25
            },
            "apple": {
                "category": "fruits",
                "stock_count": 10,
                "stock_identifier": "kg",
                "cost_price": 20,
                "selling_price": 25
            },
        }

def print_inventory():
    print ""
    print "Inventory Details - Vivira Grocery Store"
    df = pd.DataFrame(stock).T
    df.fillna(0, inplace=True)
    print(tabulate(df, headers='keys', tablefmt='psql'))
    print ""

def update_inventory(item):
    stock[item.item_name]["stock_count"] -= item.item_count
