from abc import ABC, abstractmethod


class CanBeShipped(ABC):
    # Interface-style ABC: a contract for anything that can be shipped.
    # No attributes or implementation details - only the required behaviour.

    @abstractmethod
    def calculate_shipping_cost(self):
        # Return the cost of shipping this item, in dollars.
        pass
