#define add customer
def add_customer(line, name):
    #adds a customer to the end of the line
    line.append(name)

#define place order    
def place_order(line, inventory):
    #customer places an order and takes the next available pastry
    if not line:
        return
    customer = line.pop(0)
    if inventory:
        item = inventory.pop(0)
        orders.append((customer, item))
        print(f"{customer} ordered a {item}")
    else:
        print(f"{customer} was left empty handed :(")

def is_sold_out(inventory):
    #checks if the inventory is empty
    return not inventory

def display_summary(orders, inventory):
    #displays a summary of the orders and the sold out items
    if orders:
        print("\nOrder Summary:")
        for customer, item in orders:
            print(f"{customer} - {item}")
    else:
        print("No orders placed.")
    if inventory:
        print("\nSold-out items:")
        for item in inventory:
            print(item)
    else:
        print("\nAll items are sold out!")

#define the inventory and the line        
inventory = ["Chocolate Cake", "Apple Pie", "Muffin", "Donut", "Croissant"]
line = []

#adds customers to the line
add_customer(line, "Alice")
add_customer(line, "George")
add_customer(line, "Randy")
add_customer(line, "Emma")
add_customer(line, "Elaine")

#Processes the orders
orders = []
while not is_sold_out(inventory) and line:
    place_order(line, inventory)

#display a summar of the orders    
display_summary(orders, inventory)