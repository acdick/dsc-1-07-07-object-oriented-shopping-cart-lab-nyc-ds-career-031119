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

    def n_items(self):
        n_items = 0
        for item in self.items:
            n_items += item['quantity']

        return n_items

    def mean_item_price(self):
        return self.total / self.n_items()

    def median_item_price(self):
        median = 0
        prices = []
        n_items = self.n_items()

        for item in self.items:
            prices.append(item['price'])
        prices.sort()

        if n_items % 2 != 0:
            median = prices[int(n_items / 2)]
        else:
            median = prices[int(n_items / 2)]
            median += prices[int(n_items / 2)+1]
            median /= 2

        return median

    def apply_discount(self):
        if not self.employee_discount:
            return 'Sorry, there is no discount to apply to your cart :('

        self.total = 0
        for item in self.items:
            self.total += item['price'] * item['quantity'] * (1 - self.employee_discount)

        return self.total

    def void_last_item(self):
        if len(self.items) == 0:
            return 'There are no items in your cart!'

        self.items.pop()
        self.apply_discount()

        return self.total
