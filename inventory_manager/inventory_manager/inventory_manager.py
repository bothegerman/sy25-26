
inventory = {}
print(" --- Inventory Manager ---")

while True:
    print("\nOptions:  [1] Add item  [2] Remove item  [3] View inventory  [4] Exit")
    choice = int(input("Selcet an option (1-4): "))

    if choice == 1:
        name = input("Enter item name: ")
        qty = int(input(f"Enter quantity of {name}s: "))
        if name in inventory:
            inventory[name] += qty
        else:
            inventory[name] = qty
            print(f"Added {qty} of {name} to inventory.")

    elif choice == 2:
        if name in inventory:
            name = input("Enter item name to remove: ").strip().capitalize()

    elif choice == 3:
        if not inventory:
            print("Inventory is empty.")
        else:
            print(" - Current Inventory: - ")
            print(inventory)
            print(" ----------------------")

    elif choice == 4:
        print("Exiting Inventory Manager. Goodbye!")
        break





"""
            item_name = input("Enter item name: ")
        item_quantity = int(input("Enter item quantity: "))
        if item_name in inventory:
            inventory[item_name] += item_quantity
        else:
            inventory[item_name] = item_quantity
        print(f"Added {item_quantity} of {item_name} to inventory.")
"""