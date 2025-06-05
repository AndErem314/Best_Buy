from products import Product
from colors import RED, RESET

class Store:

    list_of_products = []

    def __init__(self, list_of_products):
        self.list_of_products = list_of_products

    def add_product(self, product):
        """Add a new product to the list of products"""
        if not isinstance(product, Product):
            raise ValueError("Product must be of type Product")
        self.list_of_products.append(product)

    def remove_product(self, product):
        """Remove a product from the list of products"""
        if product not in self.list_of_products:
            raise ValueError("Product not found in store")
        self.list_of_products.remove(product)

    def get_total_quantity(self) -> int:
        """Get the total quantity of the products in the store"""
        return sum(product.get_quantity() for product in self.list_of_products)

    def get_all_products(self):
        """Get the list of products in the store, that are active"""
        return [product for product in self.list_of_products if product.is_active()]

    def order(self, shopping_list) -> float:
        """
        Arg: list of tuples (product, quantity).
        Return the total price of order
        """
        total_price = 0

        for product, quantity in shopping_list:
            if product not in self.list_of_products:
                raise ValueError(f"{RED}Product {product.name} not found in store{RESET}")

            total_price += product.buy(quantity)

        return total_price

