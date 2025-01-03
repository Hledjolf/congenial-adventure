import json
import os

class User:
    def __init__(self, username):
        self.username = username
        self.level = 1
        self.hit_points = 100
        self.inventory = []

# Function to create and initialize client data file
def create_client_data_file(user):
    filename = f"{user.username}.json"
    if not os.path.exists(filename):
        data = {
            "name": user.username,
            "level": user.level,
            "hit_points": user.hit_points,
            "inventory": user.inventory
        }
        with open(filename, "w") as file:
            json.dump(data, file)
        print(f"Created new data file for {user.username}")
    else:
        print(f"Data file for {user.username} already exists")

