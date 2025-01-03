import json

class Monster:
    def __init__(self, monster_name):
        self.username = monster_name
        self.is_user = 0
        self.level = 1
        self.hit_points = 100
        self.max_hp = 100
        self.mp = 50
        self.max_mp = 50
        self.base_armor = 5
        self.base_dodge = 5
        self.stats = {
            "strength": 10,
            "dexterity": 10,
            "wisdom": 10,
            "intelligence": 10,
            "constitution": 10,
            "charisma": 10
        }
        self.inventory = []

def add_monster_user(client_usernames, broadcast_clients, update_gui):
    with open('MonsterManual.json', 'r') as file:
        monster_manual = json.load(file)
    
    monster_template = monster_manual['monsters'][0]  # Select the first monster template, for example
    monster = Monster(monster_template['name'])
    monster.level = monster_template['level']
    monster.hit_points = monster_template['hit_points']
    monster.max_hp = monster_template['max_hp']
    monster.mp = monster_template['mp']
    monster.max_mp = monster_template['max_mp']
    monster.base_armor = monster_template['base_armor']
    monster.base_dodge = monster_template['base_dodge']
    monster.stats = monster_template['stats']
    monster.inventory = monster_template['inventory']
    
    client_usernames[f"monster_{len(client_usernames)}"] = monster
    broadcast_clients()
    update_gui(f"Monster user {monster.username} added.")