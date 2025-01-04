import json
import os

class User:
    def __init__(self, username):
        self.username = username
        self.race = "Human" # Default race
        self.level = 1
        self.hit_points = 100
        self.max_hp = 100
        self.mp = 50
        self.max_mp = 50
        self.role = "Explorer"  # Default role
        self.base_armor = 5
        self.base_dodge = 5
        self.stats = {
            "strength": 10,
            "dexterity": 10,
            "wisdom": 10,
            "intelligence": 10,
            "constitution": 10,
            "charisma": 10,
            "agility": 10
        }
        self.inventory = []
        self.skills = {
            "Blacksmithing": {"level": 1, "skill_XP": 0, "dependent_stat": "Strength"},
            "Tactics": {"level": 1, "skill_XP": 0, "dependent_stat": "Intelligence"},
            "Heavy Armor": {"level": 1, "skill_XP": 0, "dependent_stat": "Strength"},
            "Medium Armor": {"level": 1, "skill_XP": 0, "dependent_stat": "Dexterity"},
            "Light Armor": {"level": 1, "skill_XP": 0, "dependent_stat": "Agility"}
        }


    def set_role(self, role):
        valid_roles = ["Explorer", "Champion", "Merchant", "Craftsman", "Raid Leader", "Guild Leader", "Noble"]
        if role in valid_roles:
            self.role = role
        else:
            raise ValueError(f"Invalid role. Valid roles are: {', '.join(valid_roles)}")

    def set_race(self, race):
        valid_races = ["Human", "Elf", "Dwarf", "Halfling"]
        if race in valid_races:
            self.race = race
        else:
            raise ValueError(f"Invalid race. Valid races are: {', '.join(valid_races)}")

# Function to create and initialize client data file
def create_client_data_file(user):
    filename = f"{user.username}.json"
    if not os.path.exists(filename):
        data = {
            "name": user.username,
            "race": user.race,
            "level": user.level,
            "hit_points": user.hit_points,
            "max_hp": user.max_hp,
            "mp": user.mp,
            "max_mp": user.max_mp,
            "role": user.role,
            "base_armor": user.base_armor,
            "base_dodge": user.base_dodge,
            "stats": user.stats,
            "inventory": user.inventory
        }
        with open(filename, "w") as file:
            json.dump(data, file)
        print(f"Created new data file for {user.username}")
    else:
        print(f"Data file for {user.username} already exists")