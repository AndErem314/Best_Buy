import products
import store
from colors import *


def show_menu():
    """Display the main menu of the store app"""
    print(f"{BLUE}\nStore Menu\n1. List products\n2. Show total inventory"
          f"\n3. Make order\n4. Quit{RESET}")


def list_products(store):
    """Show all active products in the store use the enumerate method"""
    print("-" * 40)
    print("\nAll active Products:")
    for i, product in enumerate(store.get_all_products(), 1):
        print(f"{i}. {product.show()}")
    print("-" * 40)


def show_total_inventory(store):
    """Show total inventory of the store"""
    print("-" * 40)
    print(f"{GREEN}\nTotal items in store: {store.get_total_quantity()}{RESET}")
    print("-" * 40)


def make_order(store):
    """Handle the order process"""
    shopping_list = []

    while True:
        available_products = store.get_all_products()
        list_products(store)

        try:
            user_input = input("\nWhich product # do you want? (or 'done' to finish) ").strip()
            if user_input.lower() == 'done':
                break

            product_index = int(user_input) - 1
            if product_index >= len(available_products) or product_index < 0:
                print(f"{RED}Invalid input. Try again.{RESET}")
                continue

            quantity = int(input("\nWhat amount do you want: "))
            if quantity <= 0:
                print(f"{RED}Invalid amount.{RESET}")
                continue

            selected_product = available_products[product_index]
            if quantity > selected_product.get_quantity():
                print(f"{RED}Only {selected_product.get_quantity()} of {selected_product.name} left in stock.{RESET}")
                continue

            shopping_list.append((selected_product, quantity))
            print(f"{YELLOW}Added {quantity} x {selected_product.name} to your order{RESET}")

        except ValueError:
            print(f"{RED}Invalid input. Try again.{RESET}")
            continue

    if shopping_list:
        total = store.order(shopping_list)
        print("-" * 40)
        print(f"{YELLOW}Order successfully made, total cost: ${total:.2f}{RESET}")
        print("=" * 40 + "\n")

def quit_app():
    """Exit the app"""
    print(f"{GREEN}\nThank you for shopping with us!{RESET}")
    return False


def start(store):
    """Initiate the store app using dispatch pattern"""
    dispatch_func = {
        "1": lambda: list_products(store),
        "2": lambda: show_total_inventory(store),
        "3": lambda: make_order(store),
        "4": quit_app

    }

    while True:
        show_menu()
        user_choice = input("Choose option (1-4): ").strip()

        if user_choice in dispatch_func:
            result = dispatch_func[user_choice]()
            if result is False:
                break

        else:
            print(f"{RED}Invalid input. Please enter a number between 1 and 4.{RESET}")


if __name__ == "__main__":
    initial_products = [
        products.Product("MacBook Air M2", price=1450, quantity=100),
        products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        products.Product("Google Pixel 7", price=500, quantity=250)
    ]
    my_store = store.Store(initial_products)
    start(my_store)