from can_be_shipped import CanBeShipped
from digital_product import DigitalProduct
from file_handler import load_inventory, save_inventory
from physical_product import PhysicalProduct

FILE = "data/inventory.json"


def display_menu():
    print("----------- MENU -----------")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")
    print("----------------------------")


def ask_text(prompt):
    # Keep asking until something non-blank is entered.
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("This field cannot be empty.")


def ask_number(prompt, number_type, minimum, allow_minimum=True):
    # Keep asking until a valid number at/above the minimum is entered.
    while True:
        try:
            value = number_type(input(prompt))
        except ValueError:
            kind = "whole number" if number_type is int else "number"
            print(f"Invalid input. Please enter a {kind}.")
            continue
        if value > minimum or (allow_minimum and value == minimum):
            return value
        rule = "0 or more" if allow_minimum else "greater than 0"
        print(f"Invalid input. Value must be {rule}.")


def add_product(inventory):
    print("\nAdd New Product:")
    print("1. Physical Product")
    print("2. Digital Product")
    product_type = input("Choose product type: ").strip()
    if product_type not in ("1", "2"):
        print("Invalid product type. Please enter 1 or 2.")
        return

    while True:
        product_id = ask_text("Product ID: ")
        if inventory.search_product(product_id) is None:
            break
        print(f"A product with ID {product_id} already exists. Please enter a different ID.")

    while True:
        name = ask_text("Product Name: ")
        if any(char.isalpha() for char in name):
            break
        print("Invalid name. It must contain at least one letter.")
    price = ask_number("Price: $", float, 0)
    stock = ask_number("Stock Quantity: ", int, 0)

    try:
        if product_type == "1":
            weight = ask_number("Weight (kg): ", float, 0, allow_minimum=False)
            product = PhysicalProduct(product_id, name, price, stock, weight)
        else:
            download_size = ask_number("Download Size (MB): ", float, 0, allow_minimum=False)
            product = DigitalProduct(product_id, name, price, stock, download_size)
    except ValueError as error:  # the product classes still have the final say
        print(f"Invalid input. {error}")
        return

    if inventory.add_product(product):
        print("Product added successfully!")
    else:
        print(f"A product with ID {product_id} already exists.")


def update_stock(inventory):
    print("\nUpdate Stock:")
    product = inventory.search_product(input("Enter Product ID: ").strip())
    if product is None:
        print("Product ID not found.")
        return

    print("Product Found:")
    print(f"Name: {product.get_name()}")
    print(f"Current Stock: {product.get_stock()}")
    try:
        product.update_stock(int(input("\nEnter New Stock Quantity: ")))
        print("Stock updated successfully!")
    except ValueError:
        print("Invalid input. Stock must be a whole number of 0 or more.")


def search_product(inventory):
    print("\nSearch Product:")
    product = inventory.search_product(input("Enter Product ID: ").strip())
    if product is None:
        print("Product ID not found.")
        return
    print("Product Found:")
    print("------------------------------------------------")
    product.display_information()
    print(f"Fulfilment: {product.get_fulfilment_info()}")
    if isinstance(product, CanBeShipped):
        print(f"Shipping Cost: ${product.calculate_shipping_cost():.2f}")
    print("------------------------------------------------")


def main():
    print("========================================")
    print("INVENTORY MANAGEMENT SYSTEM (OOP)")
    print("========================================")
    inventory = load_inventory(FILE)

    while True:
        display_menu()
        choice = input("\nEnter option: ").strip()
        if choice == "1":
            inventory.display_all()
        elif choice == "2":
            add_product(inventory)
        elif choice == "3":
            update_stock(inventory)
        elif choice == "4":
            search_product(inventory)
        elif choice == "5":
            print("Saving inventory...")
            save_inventory(inventory, FILE)
            print("Inventory saved successfully to inventory.json.")
        elif choice == "6":
            print("\nSaving inventory before exit...")
            save_inventory(inventory, FILE)
            print("Inventory saved successfully.")
            print("Thank you for using Inventory Management System.")
            print("Program terminated.")
            break
        else:
            print("Invalid input. Please enter a number between 1 and 6.")


if __name__ == "__main__":
    main()
