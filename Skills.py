# Skills.py

class Skill:
    def __init__(self, name, dependent_stat):
        self.name = name
        self.dependent_stat = dependent_stat
        self.abilities = {}

    def add_ability(self, level, description):
        self.abilities[level] = description

    def use_ability(self, level):
        return self.abilities.get(level, "No ability available at this level")

# Define Blacksmithing skill
blacksmithing = Skill("Blacksmithing", "Strength")
blacksmithing.add_ability(1, "Forge Basic Tools")
blacksmithing.add_ability(2, "Forge Weapons")
blacksmithing.add_ability(3, "Forge Armor")

def use_blacksmithing(level):
    return blacksmithing.use_ability(level)

# Define Tactics skill
tactics = Skill("Tactics", "Intelligence")
tactics.add_ability(1, "Basic Battle Tactics")
tactics.add_ability(2, "Advanced Battle Tactics")
tactics.add_ability(3, "Master Battle Tactics")

def use_tactics(level):
    return tactics.use_ability(level)
    
    # Define Heavy Armor skill
heavy_armor = Skill("Heavy Armor", "Strength")
heavy_armor.add_ability(1, "Basic Heavy Armor Proficiency")
heavy_armor.add_ability(2, "Intermediate Heavy Armor Proficiency")
heavy_armor.add_ability(3, "Advanced Heavy Armor Proficiency")

def use_heavy_armor(level):
    return heavy_armor.use_ability(level)

# Define Medium Armor skill
medium_armor = Skill("Medium Armor", "Dexterity")
medium_armor.add_ability(1, "Basic Medium Armor Proficiency")
medium_armor.add_ability(2, "Intermediate Medium Armor Proficiency")
medium_armor.add_ability(3, "Advanced Medium Armor Proficiency")

def use_medium_armor(level):
    return medium_armor.use_ability(level)

# Define Light Armor skill
light_armor = Skill("Light Armor", "Agility")
light_armor.add_ability(1, "Basic Light Armor Proficiency")
light_armor.add_ability(2, "Intermediate Light Armor Proficiency")
light_armor.add_ability(3, "Advanced Light Armor Proficiency")

def use_light_armor(level):
    return light_armor.use_ability(level)