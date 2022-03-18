from product import Product

class Shopping_Cart:
    def __init__(self):
        self.product_list = []

    def current_cart_total(self):
        total = 0
        for item in self.product_list:
            total += item.price
        return total

    def add_new_product(self, product):
        self.product_list.append(product)
        print(f"{product.name} was added to shopping cart")

    def empty_shopping_cart(self):
        self.product_list.clear()
        