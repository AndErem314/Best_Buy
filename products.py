class Product:

    def __init__(self, name, price, quantity):
        if not name:  # checks for empty string
            raise ValueError("Name cannot be empty")
        if price < 0:
            raise ValueError("Price cannot be negative")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self) -> int:
        """Returns the current quantity of the product"""
        return self.quantity

    def set_quantity(self, quantity):
        """Sets the quantity and deactivates product if quantity reached 0"""
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")

        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()

    def is_active(self) -> bool:
        """Returns True if product is active, False otherwise"""
        return self.active

    def activate(self):
        """Activates the product"""
        self.active = True

    def deactivate(self):
        """Deactivates the product"""
        self.active = False

    def show(self) -> str:
        """Returns a string representation of the product"""
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"

    def buy(self, quantity) -> float:
        """Buys the product with the given quantity"""
        if not self.active:
            raise ValueError("The product is not available to buy")
        if quantity <= 0:
            raise ValueError("Purchase quantity must be positive")
        if quantity > self.quantity:
            raise ValueError("Insufficient quantity available")

        total_price = quantity * self.price
        self.quantity -= quantity

        # Deactivate product if quantity reaches 0
        if self.quantity == 0:
            self.deactivate()

        return total_price
