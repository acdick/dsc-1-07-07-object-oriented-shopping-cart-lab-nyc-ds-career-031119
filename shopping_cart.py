class ShoppingCart:
    # write your code here
    def __init__(self, emp_discount=None):
        self.total = 0
        self.employee_discount = emp_discount
        self.items = []

    def add_item(self, name, price, quantity=1):
        item = {}
        item['name'] = name
        item['price'] = price
        item['quantity'] = quantity
        self.items.append(item)
        self.total += price * quantity
        return self.total

    def mean_item_price(self):
       pass

    def median_item_price(self):
        pass

    def apply_discount(self):
       pass

    def void_last_item(self):
        pass
