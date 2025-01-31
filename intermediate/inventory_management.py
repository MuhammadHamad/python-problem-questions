
#! Create a more complex program that manages a store's inventory:

#! Create a dictionary where:

#! Keys are product IDs
#! Values are dictionaries containing:

#! product name
#! price
#! quantity in stock
#! category


#! Implement functions to:

#! Add new products
#! Update product quantities
#! Calculate total inventory value
#! Find all products in a specific category
#! Handle products that don't exist
#! Print a formatted inventory report

inventory = {
    "P001": {
        "name": "Laptop",
        "price": 999.99,
        "quantity": 10,
        "category": "Electronics"
    },
    "P002": {
        "name": "Mobile",
        "price": 799.99,
        "quantity": 20,
        "category": "Electronics"
    },
    "P003": {
        "name": "Football",
        "price": 99.99,
        "quantity": 30,
        "category": "Sports"
    }
}

print("Current Inventory:")
for pid, details in inventory.items():
    print(f"{pid}: {details}")

def add_new_product(inventory_dict, pid, name, price, quantity, category):
    """Add a single new product to the inventory"""
    inventory_dict[pid] = {
        "name": name,
        "price": price,
        "quantity": quantity,
        "category": category
    }

question = input("Do you want to add new products? (y/n): ")

if question.lower() == 'y':
    while True:
        product_id = input("Enter product ID (or 'q' to quit): ").strip()
        if product_id.lower() == 'q':
            break
            
        if product_id in inventory:
            print("Product ID already exists.")
            continue
            
        try:
            name = input("Enter product name: ").strip()
            price = float(input("Enter product price: ").strip())
            quantity = int(input("Enter product quantity: ").strip())
            category = input("Enter product category: ").strip()
            
            # Add the new product directly to inventory
            add_new_product(inventory, product_id, name, price, quantity, category)
            print(f"Product {product_id} added successfully!")
            
        except ValueError:
            print("Invalid input for price or quantity. Please enter numbers only.")
            continue

print("\nUpdated Inventory:")
for pid, details in inventory.items():
    print(f"{pid}: {details}")
