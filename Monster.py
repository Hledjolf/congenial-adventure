class Monster:
    def __init__(self, username):
        self.username = "GenericMob"
        self.level = 1
        self.hit_points = 100
        self.max_hp = 100
        self.mp = 50
        self.max_mp = 50
        self.stats = {
            "strength": 10,
            "dexterity": 10,
            "wisdom": 10,
            "intelligence": 10,
            "constitution": 10,
            "charisma": 10
        }
        self.inventory = []