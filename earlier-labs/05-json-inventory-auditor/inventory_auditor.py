import os
import json

FILE = "data/inventory.json"
inventory = []

def add_product():
    print("\nAdd New Product:")
    try:
        product_id = input("Product ID: ")
        product_name = input("Product Name: ")
        product_price = float(input("Price: $"))
        product_stock = int(input("Stock Quantity: "))
        inventory.append({
            "id": product_id,
            "name": product_name,
            "price": product_price,
            "stock": product_stock
        })
        print("Product added successfully!")
    except ValueError:
        print("Invalid input. Please enter valid values.")

def update_stock():
    print("\nUpdate Stock:")
    product_id = input("Enter Product ID: ")
    for product in inventory:
        if product["id"] == product_id:
            print(f"Product Found:")
            print(f"Name: {product['name']}")
            print(f"Current Stock: {product['stock']}")
            try:
                new_stock = int(input("\nEnter New Stock Quantity: "))
            except ValueError:
                print("Invalid input. Please enter a valid integer.")
                return
            product["stock"] = new_stock
            print("Stock updated successfully!")
            return
    print("Product ID not found.")
    update_stock()

def search_product():
    print("\nSearch Product:")
    product_id = input("Enter Product ID: ")
    for product in inventory:
        if product["id"] == product_id:
            print(f"Product Found:")
            print("------------------------------------------------")
            print(f"ID: {product['id']}")
            print(f"Name: {product['name']}")
            print(f"Price: ${product['price']:.2f}")
            print(f"Stock: {product['stock']}")
            print("------------------------------------------------")
            return
    print("Product ID not found.")

def display_all(inventory_data):
    print("\nCurrent Inventory:")
    print("------------------------------------------------")
    for product in inventory_data:
        print(f"ID: {product['id']} | Name: {product['name']} | Price: ${product['price']:.2f} | Stock: {product['stock']}")
    print("------------------------------------------------")

def get_valid_input():
    try:
        user_input = input("\n Enter option: ")
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 6.")
    if user_input == "1":
        display_all(inventory)
    elif user_input == "2":
        add_product()
    elif user_input == "3":
        update_stock()
    elif user_input == "4":
        search_product()
    elif user_input == "5":
        print("Saving inventory...")
        save_inventory()
        print("Inventory saved successfully to inventory.json.")
    elif user_input == "6":
        print("\nSaving inventory before exit...")
        save_inventory()
        print("""Inventory saved successfully.
Thank you for using Inventory Management System.
Program terminated.
""")
        return "quit"

def load_inventory():
    global inventory
    if os.path.exists(FILE):
        with open(FILE, "r") as file:
            inventory_data = file.read().strip()
            if not inventory_data:
                print("\ninventory.json is empty.\n")
                inventory = []
            else:
                inventory = json.loads(inventory_data)
                print("\ninventory.json found.")
                print("Inventory loaded successfully.\n")
    else:
        print("\nNo inventory data available.")
        inventory = []

def save_inventory():
    os.makedirs(os.path.dirname(FILE), exist_ok=True)
    with open(FILE, "w") as file:
        json.dump(inventory, file, indent=4)


def display_new_order(product_id, product, quantity):
    print(f"\nNew Order Added:\n{product_id}, {product}, {quantity}\n")

def main():
    print("========================================")
    print("INVENTORY MANAGEMENT SYSTEM")
    print("========================================")
    load_inventory()
    print("----------- MENU -----------")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")
    print("----------------------------")
    while True:
        user_input = get_valid_input()
        if user_input == "quit":
            break
        elif user_input is None:
            continue
main()