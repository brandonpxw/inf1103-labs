from can_be_shipped import CanBeShipped
from product import Product


class PhysicalProduct(Product, CanBeShipped):
    # A product that is stored and shipped.
    # Inherits from Product (is-a) and implements the CanBeShipped interface.

    TYPE = "physical"
    BASE_SHIPPING_FEE = 5.00  # flat handling fee in $
    RATE_PER_KG = 2.00        # extra $ per kg

    def __init__(self, product_id, name, price, stock, weight):
        super().__init__(product_id, name, price, stock)  # reuse the Product constructor
        weight = float(weight)
        if weight <= 0:
            raise ValueError("Weight must be greater than 0 kg.")
        self.__weight = weight

    def get_weight(self):
        return self.__weight

    def display_information(self):
        super().display_information()  # common details come from Product
        print(f"    Type: Physical | Weight: {self.__weight:.2f} kg")

    def get_fulfilment_info(self):
        return "This product requires physical shipping."

    def calculate_shipping_cost(self):
        # Simple rule: flat fee + rate per kg.
        return round(self.BASE_SHIPPING_FEE + self.RATE_PER_KG * self.__weight, 2)

    def to_dict(self):
        data = super().to_dict()
        data["type"] = self.TYPE
        data["weight"] = self.__weight
        return data

    @classmethod
    def from_dict(cls, data):
        return cls(data["id"], data["name"], data["price"], data["stock"], data["weight"])
