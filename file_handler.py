import json
import os

from digital_product import DigitalProduct
from inventory import Inventory
from physical_product import PhysicalProduct

# Maps the "type" saved in JSON to the class that rebuilds it.
PRODUCT_TYPES = {
    PhysicalProduct.TYPE: PhysicalProduct,
    DigitalProduct.TYPE: DigitalProduct,
}


def load_inventory(file_path):
    """Build an Inventory of the correct product subclasses from the JSON file."""
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
        product_class = PRODUCT_TYPES.get(item.get("type"))
        if product_class is None:
            print(f"Skipping {item.get('id')}: unknown product type '{item.get('type')}'.")
            continue
        inventory.add_product(product_class.from_dict(item))
    print("\ninventory.json found.")
    print("Inventory loaded successfully.\n")
    return inventory


def save_inventory(inventory, file_path):
    """Write every product (including its type and extra attributes) to the JSON file."""
    folder = os.path.dirname(file_path)
    if folder:
        os.makedirs(folder, exist_ok=True)
    with open(file_path, "w") as file:
        json.dump([product.to_dict() for product in inventory.get_products()], file, indent=4)
