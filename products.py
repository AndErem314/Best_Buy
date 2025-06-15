from colors import RED, RESET, GREEN


class Product:

    def __init__(self, name, price, quantity):
        if not name:  # checks for empty string
            raise ValueError(f"{RED}Name cannot be empty{RESET}")
        if price < 0:
            raise ValueError(f"{RED}Price cannot be negative{RESET}")
        if quantity < 0:
            raise ValueError(f"{RED}Quantity cannot be negative{RESET}")

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
            raise ValueError(f"{RED}Quantity cannot be negative{RESET}")

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
        return f"{GREEN}{self.name}, Price: {self.price}, Quantity: {self.quantity}{RESET}"

    def buy(self, quantity) -> float:
        """Buys the product with the given quantity"""
        if not self.active:
            raise ValueError(f"{RED}The product is not available to buy{RESET}")
        if quantity <= 0:
            raise ValueError(f"{RED}Purchase quantity must be positive{RESET}")
        if quantity > self.quantity:
            raise ValueError(f"{RED}Insufficient quantity available{RESET}")

        total_price = quantity * self.price
        self.set_quantity(self.quantity - quantity)

        return total_price
