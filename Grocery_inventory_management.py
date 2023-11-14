class GroceryInventory:
    def _init_(self):
        self.inventory = {}

    def add_item(self, name, quantity, price):
        if name not in self.inventory:
            self.inventory[name] = {'quantity': quantity, 'price': price}
            print(f"{name} added to the inventory.")
        else:
            print(f"{name} is already in the inventory. You can update quantities and prices.")

    def update_quantity(self, name, new_quantity):
        if name in self.inventory:
            self.inventory[name]['quantity'] = new_quantity
            print(f"Quantity of {name} updated to {new_quantity}.")
        else:
            print(f"{name} is not in the inventory. Add it first.")

    def remove_item(self, name):
        if name in self.inventory:
            del self.inventory[name]
            print(f"{name} removed from the inventory.")
        else:
            print(f"{name} is not in the inventory. Cannot remove.")

    def display_inventory(self):
        print("\n Inventory:")
        print("Name \t\t Quantity\t Price")
        
        for item, details in self.inventory.items():
            print(f"{item}\t\t{details['quantity']}\t\t{details['price']}")
    

# Example Usage with User Input:
if __name__ == "_main_":
    grocery_manager = GroceryInventory()

    while True:
        print("\n1. Add Item")
        print("2. Update Quantity")
        print("3. Remove Item")
        print("4. Display Inventory")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            name = input("Enter item name: ")
            quantity = int(input("Enter quantity: "))
            price = float(input("Enter price: "))
            grocery_manager.add_item(name, quantity, price)

        elif choice == '2':
            name = input("Enter item name to update quantity: ")
            new_quantity = int(input("Enter new quantity: "))
            grocery_manager.update_quantity(name, new_quantity)

        elif choice == '3':
            name = input("Enter item name to remove: ")
            grocery_manager.remove_item(name)

        elif choice == '4':
            grocery_manager.display_inventory()

        elif choice == '5':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please enter a number between 1and 5.")
