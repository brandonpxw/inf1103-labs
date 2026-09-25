import os


def get_valid_input():
    product_input = str(input("\nEnter Product Name: ")).strip()
    
    if product_input.lower() == "quit":
        return "quit"
    
    if product_input.isdigit() or product_input == "":
        print("Invalid input. Product name cannot be empty or purely numbers.")
        return None

    try:
        quantity_input = int(input("Enter Quantity: "))
    except ValueError:
        print("Invalid input. Quantity must be an integer.")
        return None

    if quantity_input > 0:
        if quantity_input > 500:
            print("Warning: Stock quantity exceeds 500!")
        return product_input, quantity_input
    else:
        print("Invalid input. Quantity must be greater than 0.")
        return None


def display_inventory():
    if os.path.exists("orders.txt"):
        with open("orders.txt", "r") as file:
            orders_data = file.read().strip()
            if not orders_data:
                print("\nNo orders available.\n")
                return 1001
            else:
                print("\nCurrent Orders:")
                print(orders_data)
                # Count existing lines to calculate next order ID
                line_count = len(orders_data.splitlines())
                return 1001 + line_count
    else:
        print("\nNo inventory data available.")
        return 1001


def display_new_order(product_id, product, quantity):
    print(f"\nNew Order Added:\n{product_id}, {product}, {quantity}\n")


def append_to_inventory(orderid, product, quantity):
    with open("orders.txt", "a") as file:
        file.write(f"{orderid}, {product}, {quantity}\n")


def main():
    while True:
        next_order_id = display_inventory()
        user_input = get_valid_input()

        if user_input == "quit":
            print("Exiting the program.")
            break
        elif user_input is None:
            continue

        product, quantity = user_input
        display_new_order(next_order_id, product, quantity)
        append_to_inventory(next_order_id, product, quantity)
main()