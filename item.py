class item(object):
    def __init__(self, name=None, count = None):
        self.item_name = name
        self.item_count = count
        self.category = None
        self.cost_price = None
        self.selling_price = None
        self.stock_identifier = None

    def check_offer_eligibility(self, **kwargs):
        pass