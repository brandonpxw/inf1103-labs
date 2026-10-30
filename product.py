from abc import ABC, abstractmethod


class Product(ABC):
    # Abstract base class for every product (SRP: one product only).
    # It can't be created directly - every product must be Physical or Digital.

    def __init__(self, product_id, name, price, stock):
        self.__product_id = product_id
        name = str(name).strip()
        if not any(char.isalpha() for char in name):
            raise ValueError("Product name must contain at least one letter.")
        self.__name = name
        price = float(price)
        if price < 0:
            raise ValueError("Price cannot be negative.")
        self.__price = price
        self.__stock = 0
        self.update_stock(stock)  # validate the starting stock through the same rule

    # --- read-only access for outside code (no direct setters) ---
    def get_product_id(self):
        return self.__product_id

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def get_stock(self):
        return self.__stock

    # --- behaviour that changes state ---
    def update_stock(self, quantity):
        # Set the stock to a new quantity. The Product decides what is valid.
        quantity = int(quantity)
        if quantity < 0:
            raise ValueError("Stock cannot be negative.")
        self.__stock = quantity

    def display_information(self):
        # Common information. Subclasses call this with super() and add their own details.
        print(f"ID: {self.__product_id} | Name: {self.__name} | "
              f"Price: ${self.__price:.2f} | Stock: {self.__stock}")

    def to_dict(self):
        # Plain-data form of the common attributes. Subclasses add their own fields.
        return {
            "id": self.__product_id,
            "name": self.__name,
            "price": self.__price,
            "stock": self.__stock,
        }

    @abstractmethod
    def get_fulfilment_info(self):
        # Every subclass must say how the product reaches the customer.
        pass
