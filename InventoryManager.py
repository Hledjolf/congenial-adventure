# InventoryManager.py

class InventoryManager:
    def __init__(self):
        self.inventories = {}

    def add_item(self, username, item):
        if username not in self.inventories:
            self.inventories[username] = []
        self.inventories[username].append(item)
        return f"Added {item} to {username}'s inventory."

    def remove_item(self, username, item):
        if username in self.inventories and item in self.inventories[username]:
            self.inventories[username].remove(item)
            return f"Removed {item} from {username}'s inventory."
        return f"Item {item} not found in {username}'s inventory."

    def view_inventory(self, username):
        if username in self.inventories:
            return self.inventories[username]
        return f"{username} has no inventory."
        
    def create_inventory_grid(frame, inventory_manager, username):
        inventory_frame = tk.Frame(frame, relief=tk.RAISED, bd=2)
        inventory_frame.grid(row=4, column=0, columnspan=10, padx=5, pady=5)

        inventory_label = tk.Label(inventory_frame, text="Inventory:")
        inventory_label.grid(row=0, column=0, columnspan=5)

        icons = {}
    
    def add_item_to_inventory(item):
        inventory_manager.add_item(username, item)
        update_inventory_grid()

    def remove_item_from_inventory(item):
        inventory_manager.remove_item(username, item)
        update_inventory_grid()

    def update_inventory_grid():
        for widget in inventory_frame.winfo_children():
            if isinstance(widget, tk.Button):
                widget.destroy()
                
        inventory = inventory_manager.view_inventory(username)
        for index, item in enumerate(inventory):
            icon = icons.get(item, None)
            if not icon:
                # Create a placeholder icon for the item
                image = Image.new('RGB', (50, 50), color = 'gray')
                icon = ImageTk.PhotoImage(image)
                icons[item] = icon

            item_button = tk.Button(inventory_frame, image=icon, command=lambda item=item: remove_item_from_inventory(item))
            item_button.grid(row=(index // 5) + 1, column=index % 5, padx=5, pady=5)

    add_item_button = tk.Button(inventory_frame, text="Add Item", command=lambda: add_item_to_inventory("New Item"))
    add_item_button.grid(row=1, column=6, padx=5, pady=5)

    update_inventory_grid()