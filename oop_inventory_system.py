from file_handler import load_inventory, save_inventory
from product import Product

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


def add_product(inventory):
    print("\nAdd New Product:")
    try:
        product_id = input("Product ID: ").strip()
        name = input("Product Name: ").strip()
        price = float(input("Price: $"))
        stock = int(input("Stock Quantity: "))
        product = Product(product_id, name, price, stock)
    except ValueError as error:
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
