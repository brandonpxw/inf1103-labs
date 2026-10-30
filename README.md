# INF1103 DevOps Labs

Weekly lab work for **INF1103 – DevOps** at the Singapore Institute of Technology (BEng (Hons) ICT, Software Engineering).

The main project is a command-line **Inventory Management System** written in Python using object-oriented design. Earlier labs, which build up to it, are kept in [`earlier-labs/`](earlier-labs/).

## Inventory Management System

A menu-driven app to view, add, search and update products, with data saved to JSON.

**Features**
- Two product types: **physical** (has weight, can be shipped) and **digital** (has download size)
- Shipping cost for physical products (flat fee + rate per kg)
- Input validation on every field
- Inventory loads from and saves to `data/inventory.json`

### Design

| File | Responsibility |
|------|----------------|
| `product.py` | `Product` – abstract base class with encapsulated common fields |
| `physical_product.py` | `PhysicalProduct` – extends `Product`, implements `CanBeShipped` |
| `digital_product.py` | `DigitalProduct` – extends `Product` |
| `can_be_shipped.py` | `CanBeShipped` – interface (abstract base class) for shippable items |
| `inventory.py` | `Inventory` – manages the collection of products |
| `file_handler.py` | Loads/saves the inventory as JSON |
| `oop_inventory_system.py` | Entry point and menu |

```mermaid
classDiagram
    direction TB
    class Inventory {
        -__products : list~Product~
        +#95;#95;init#95;#95;()
        +add_product(product: Product) bool
        +search_product(product_id: str) Product
        +display_all() void
        +get_products() list~Product~
    }
    class Product {
        <<abstract>>
        -__product_id : str
        -__name : str
        -__price : float
        -__stock : int
        +#95;#95;init#95;#95;(product_id: str, name: str, price: float, stock: int)
        +get_product_id() str
        +get_name() str
        +get_price() float
        +get_stock() int
        +update_stock(quantity: int) void
        +display_information() void
        +to_dict() dict
        +get_fulfilment_info()* str
    }
    class CanBeShipped {
        <<interface>>
        +calculate_shipping_cost()* float
    }
    class PhysicalProduct {
        +TYPE : str = "physical"
        -__weight : float
        +#95;#95;init#95;#95;(product_id: str, name: str, price: float, stock: int, weight: float)
        +get_weight() float
        +display_information() void
        +get_fulfilment_info() str
        +calculate_shipping_cost() float
        +to_dict() dict
        +from_dict(data: dict)$ PhysicalProduct
    }
    class DigitalProduct {
        +TYPE : str = "digital"
        -__download_size : float
        +#95;#95;init#95;#95;(product_id: str, name: str, price: float, stock: int, download_size: float)
        +get_download_size() float
        +display_information() void
        +get_fulfilment_info() str
        +to_dict() dict
        +from_dict(data: dict)$ DigitalProduct
    }
    Inventory "1" o-- "0..*" Product : contains
    Product <|-- PhysicalProduct
    Product <|-- DigitalProduct
    CanBeShipped <|.. PhysicalProduct
```

OOP concepts used: abstraction, encapsulation (private attributes with getters), inheritance, polymorphism and an interface-style ABC.

### Run it

With Python 3.10+:

```bash
python oop_inventory_system.py
```

With Docker:

```bash
docker build -t inventory-system .
docker run -it inventory-system
```

## Earlier labs

| Folder | What it covers |
|--------|----------------|
| `01-hello-profile` | Variables, input and conditionals |
| `02-stock-auditor` | Loops and input validation |
| `03-modular-auditor` | Breaking a program into functions |
| `04-persistent-auditor` | Reading and writing text files |
| `05-json-inventory-auditor` | JSON persistence for an inventory |
