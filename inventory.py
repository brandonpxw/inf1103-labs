class Inventory:
    """Manages a collection of Product objects (SRP: the collection only)."""

    def __init__(self):
        self.__products = []

    def add_product(self, product):
        """Add a Product. Returns False if that product ID already exists."""
        if self.search_product(product.get_product_id()) is not None:
            return False
        self.__products.append(product)
        return True

    def search_product(self, product_id):
        """Return the Product with this ID, or None if it isn't found."""
        for product in self.__products:
            if product.get_product_id().lower() == product_id.lower():
                return product
        return None

    def display_all(self):
        print("\nCurrent Inventory:")
        print("------------------------------------------------")
        if not self.__products:
            print("No products in inventory.")
        for product in self.__products:
            product.display_information()
        print("------------------------------------------------")

    def get_products(self):
        """A copy of the list, so outside code can't change the inventory directly."""
        return list(self.__products)
