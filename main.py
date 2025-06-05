import products
import store

# Color definitions
LIGHT_PURPLE = "\033[1;35m"
BLINK = "\033[5m"
RESET = "\033[0m"  # reset colors settings
MENU = "\033[0;32m"  # green color
ENT_TO_CONT = "\033[1;34m"  # light blue
RED = "\033[0;31m"
YELLOW = "\033[1;33m"



# setup initial stock of inventory
list_of_products = [
    products.Product("MacBook Air M2", price=1450, quantity=100),
    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
    products.Product("Google Pixel 7", price=500, quantity=250)
    ]

my_store = store.Store(list_of_products)

def show_menu():
    """Display the main menu of the store app"""
    print("\nStore Menu")
    print("1. List products")
    print("2. Show total inventory")
    print("3. Make order")
    print("4. Quit")


def list_products():
    """Show all active products in the store use the enumerate method"""
    print("-" * 40)
    print("\nAll active Products:")
    for i, product in enumerate(my_store.get_all_products(), 1):
        print(f"{i}. {product.show()}")
    print("-" * 40)


def show_total_inventory():
    """Show total inventory of the store"""
    print("-" * 40)
    print(f"\nTotal items in store: {my_store.get_total_quantity()}")
    print("-" * 40)


def make_order():
    """Handle the order process"""
    available_products = my_store.get_all_products()
    list_products() # Shows available products
    shopping_list = []

    while True:
        try:
            user_input = input("\nWhich product # do you want? (or 'done' to finish").strip()
            if user_input.lower() == 'done':
                break

            product_index = int(user_input) - 1
            if product_index >= len(available_products) or product_index < 0:
                print("Invalid input. Try again.")
                continue

            quantity = int(input("\nWhat amount do you want: "))
            if quantity <= 0:
                print("Invalid amount.")
                continue

            selected_product = available_products[product_index]
            shopping_list.append((selected_product, quantity))
            print(f"Added {quantity} x {selected_product.name} to your order")

        except ValueError:
            print("Invalid input. Try again.")
            continue

    if shopping_list:
        total = my_store.order(shopping_list)
        print("-" * 40)
        print(f"Order successfully made, total cost: ${total:.2f}")
        print("=" * 40 + "\n")

def quit_app():
    """Exit the app"""
    print("\nThank you for shopping with us!")
    return False


def start():
    """Initiate the store app using dispatch pattern"""
    dispatch_func = {
        "1": list_products,
        "2": show_total_inventory,
        "3": make_order,
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
            print("Invalid input. Please enter a number between 1 and 4.")



if __name__ == "__main__":
    start()