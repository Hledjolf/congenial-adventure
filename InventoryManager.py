# InventoryManager.py
import tkinter as tk
from PIL import Image, ImageTk

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
        
