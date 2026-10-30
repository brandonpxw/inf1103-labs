import json
import os

from inventory import Inventory
from product import Product


def load_inventory(file_path):
    """Build an Inventory of Product objects from the JSON file."""
    inventory = Inventory()
    if not os.path.exists(file_path):
        print("\nNo inventory data available.")
        return inventory

    with open(file_path, "r") as file:
        data = file.read().strip()

    if not data:
        print("\ninventory.json is empty.\n")
        return inventory

    for item in json.loads(data):
        inventory.add_product(Product(item["id"], item["name"], item["price"], item["stock"]))
    print("\ninventory.json found.")
    print("Inventory loaded successfully.\n")
    return inventory


def save_inventory(inventory, file_path):
    """Write every Product in the Inventory back to the JSON file."""
    folder = os.path.dirname(file_path)
    if folder:
        os.makedirs(folder, exist_ok=True)
    with open(file_path, "w") as file:
        json.dump([product.to_dict() for product in inventory.get_products()], file, indent=4)
