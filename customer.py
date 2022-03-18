from shopping_cart import Shopping_Cart

class Customer:
    def __init__(self, name):
        self.name = name
        self.shopping_cart = Shopping_Cart()

    def add_to_shopping_cart(self, product):
        self.shopping_cart.add_new_product(product)

    def view_shopping_cart_contents(self):
        for item in self.shopping_cart.product_list:
            print(item.name)

    