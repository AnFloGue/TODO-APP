'''Here's a new exercise that incorporates inheritance and dictionaries, with the
twist of using an external dictionary to populate an internal class dictionary:

Scenario:

Imagine you're building a system to manage customer orders for a clothing store. You have a base class ClothingItem and derived classes for different types of clothing. Each clothing item has attributes like size, color, and brand. Customers can place orders with multiple items, with each item having a specific quantity.

Assignment:

Create a base class ClothingItem:

Attributes:
size (string)
color (string)
brand (string)
Method:
__init__(self, size, color, brand): Constructor to initialize common attributes.
Create derived classes for different clothing types:

You can create separate classes for Shirt, Pants, Shoes, etc., each inheriting from ClothingItem and potentially adding specific attributes.
External Dictionary:

Create a dictionary outside the class named item_prices that maps clothing size-color combinations (strings) to their respective prices (floats).
Internal Dictionary in ClothingItem (optional):

Consider adding an internal dictionary (item_details) to the ClothingItem class (or derived classes) during object creation. This dictionary can hold additional details like the clothing type (shirt, pants, etc.) and a reference to the price from the item_prices dictionary based on size and color.
Order Class:

Create a class Order that can hold multiple ClothingItem objects.
Attributes:
customer_name (string)
items (list) - Initialize with an empty list to store ClothingItem objects
Methods:
__init__(self, customer_name): Constructor to initialize customer_name.
add_item(self, clothing_item, quantity): Adds a specific clothing_item (object) with a given quantity (integer) to the items list.
Example Code:

Python
# External dictionary (replace with actual price data)
item_prices = {"S-Red": 19.99, "M-Blue": 24.99, "L-Green": 32.50}'''

class ClothingItem:
    def __init__(self, size, color, brand):
        self.size = size
        self.color = color
        self.brand = brand

class Order:
    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.items = []

    def add_item(self, clothing_item, quantity):
        # Optional: Populate internal dictionary here
        # item_details = {"type": "Shirt", "price": item_prices[f"{clothing_item.size}-{clothing_item.color}"]}
        # clothing_item.item_details = item_details  # Assuming ClothingItem has this attribute
        self.items.append((clothing_item, quantity))  # Add item and quantity tuple

# Create clothing items
shirt1 = ClothingItem("S", "Red", "BrandX")
pants1 = ClothingItem("M", "Blue", "BrandY")

# Create order
order1 = Order("Alice")
order1.add_item(shirt1, 2)
order1.add_item(pants1, 1)

# Calculate total order amount (assuming internal item_details is used)
total_amount = 0
for item, quantity in order1.items():
    total_amount += quantity * item.item_details["price"]  # Access price from internal dictionary

print(f"Order for {order1.customer_name}:")
for item, quantity in order1.items():
    print(f"- {quantity}x {item.size}-{item.color} {item.brand}")
print(f"Total amount: ${total_amount:.2f}")

'''
Use code with caution.
This is a basic example. You can extend it by:

Adding more clothing types and attributes
Implementing a function in ClothingItem to access the price based on size and
color from the item_prices dictionary
Including functionalities for order management (calculating total cost
without internal dictionary, applying discounts, etc.)'''