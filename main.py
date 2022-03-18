from customer import Customer
from product import Product

customer_one = Customer("Geralt")
product_one = Product("Laptop", 1200, "electronics")
product_two = Product("Mouse", 55, "electronics")
product_three = Product("Pen", 3, "office supplies")

customer_one.add_to_shopping_cart(product_one)
customer_one.add_to_shopping_cart(product_two)
customer_one.add_to_shopping_cart(product_three)

customer_one.view_shopping_cart_contents()

cart_total = customer_one.shopping_cart.current_cart_total()
print(cart_total)

customer_one.shopping_cart.empty_shopping_cart()

if(not(customer_one.shopping_cart.product_list)):
    print("The shopping cart is empty")
else:
    print("The shopping cart is not empty")