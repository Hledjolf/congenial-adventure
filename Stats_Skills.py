# Skills.py

class Skill:
    def __init__(self, name, dependent_stat, skill_description, skill_icon, max_level, type, skillups):
        self.name = name
        self.dependent_stat = dependent_stat
        self.skill_description = skill_description
        self.skill_icon = skill_icon
        self.max_level = max_level
        self.type = type
        self.skillups = skillups
        self.abilities = {}

    def add_ability(self, level, description):
        self.abilities[level] = description

    def use_ability(self, level):
        return self.abilities.get(level, "No ability available at this level")

# Crafting Skills
# Define Alchemy skill
alchemy = Skill(
    name="Alchemy",
    dependent_stat="Intelligence",
    skill_description="The art of crafting potions and elixirs.",
    skill_icon="alchemy_icon.png",
    max_level=100,
    type="Crafting",
    skillups=["Ability", "Action"]
)
alchemy.add_ability(1, "Create Minor Healing Potion")
alchemy.add_ability(2, "Create Major Healing Potion")
alchemy.add_ability(3, "Create Elixir of Strength")

def use_alchemy(level):
    return alchemy.use_ability(level)

# Define Archaeology skill
archaeology = Skill(
    name="Archaeology",
    dependent_stat="Wisdom",
    skill_description="The study and excavation of ancient artifacts.",
    skill_icon="archaeology_icon.png",
    max_level=100,
    type="Crafting",
    skillups=["Ability", "Action"]
)
archaeology.add_ability(1, "Excavate Minor Artifact")
archaeology.add_ability(2, "Excavate Major Artifact")
archaeology.add_ability(3, "Excavate Ancient Relic")

def use_archaeology(level):
    return archaeology.use_ability(level)

# Define Architecture skill
architecture = Skill(
    name="Architecture",
    dependent_stat="Intelligence",
    skill_description="The art of designing and constructing buildings.",
    skill_icon="architecture_icon.png",
    max_level=100,
    type="Crafting",
    skillups=["Ability", "Action"]
)
architecture.add_ability(1, "Design Basic Structure")
architecture.add_ability(2, "Design Advanced Structure")
architecture.add_ability(3, "Design Master Structure")

def use_architecture(level):
    return architecture.use_ability(level)

# Define Blacksmithing skill
blacksmithing = Skill(
    name="Blacksmithing",
    dependent_stat="Strength",
    skill_description="The art of forging tools and weapons.",
    skill_icon="blacksmith_icon.png",
    max_level=100,
    type="Crafting",
    skillups=["Ability", "Action"]
)
blacksmithing.add_ability(1, "Forge Basic Tools")
blacksmithing.add_ability(2, "Forge Weapons")
blacksmithing.add_ability(3, "Forge Armor")

def use_blacksmithing(level):
    return blacksmithing.use_ability(level)

# Define Brewing skill
brewing = Skill(
    name="Brewing",
    dependent_stat="Intelligence",
    skill_description="The art of brewing beverages.",
    skill_icon="brewing_icon.png",
    max_level=100,
    type="Crafting",
    skillups=["Ability", "Action"]
)
brewing.add_ability(1, "Brew Basic Ale")
brewing.add_ability(2, "Brew Fine Wine")
brewing.add_ability(3, "Brew Premium Whiskey")

def use_brewing(level):
    return brewing.use_ability(level)

# Define Carpentry skill
carpentry = Skill(
    name="Carpentry",
    dependent_stat="Strength",
    skill_description="The craft of building and repairing wooden structures.",
    skill_icon="carpentry_icon.png",
    max_level=100,
    type="Crafting",
    skillups=["Ability", "Action"]
)
carpentry.add_ability(1, "Build Basic Furniture")
carpentry.add_ability(2, "Build Wooden Structures")
carpentry.add_ability(3, "Build Advanced Wooden Structures")

def use_carpentry(level):
    return carpentry.use_ability(level)

# Define Cooking skill
cooking = Skill(
    name="Cooking",
    dependent_stat="Wisdom",
    skill_description="The art of preparing food.",
    skill_icon="cooking_icon.png",
    max_level=100,
    type="Crafting",
    skillups=["Ability", "Action"]
)
cooking.add_ability(1, "Cook Simple Meals")
cooking.add_ability(2, "Cook Gourmet Meals")
cooking.add_ability(3, "Cook Exotic Dishes")

def use_cooking(level):
    return cooking.use_ability(level)

# Define Farming skill
farming = Skill(
    name="Farming",
    dependent_stat="Strength",
    skill_description="The cultivation of crops and livestock.",
    skill_icon="farming_icon.png",
    max_level=100,
    type="Crafting",
    skillups=["Ability", "Action"]
)
farming.add_ability(1, "Plant Basic Crops")
farming.add_ability(2, "Harvest Crops")
farming.add_ability(3, "Manage Livestock")

def use_farming(level):
    return farming.use_ability(level)

# Define Fishing skill
fishing = Skill(
    name="Fishing",
    dependent_stat="Dexterity",
    skill_description="The skill of catching fish.",
    skill_icon="fishing_icon.png",
    max_level=100,
    type="Crafting",
    skillups=["Ability", "Action"]
)
fishing.add_ability(1, "Catch Small Fish")
fishing.add_ability(2, "Catch Medium Fish")
fishing.add_ability(3, "Catch Large Fish")

def use_fishing(level):
    return fishing.use_ability(level)

# Define Foraging skill
foraging = Skill(
    name="Foraging",
    dependent_stat="Dexterity",
    skill_description="The act of searching for and collecting wild food resources.",
    skill_icon="foraging_icon.png",
    max_level=100,
    type="Crafting",
    skillups=["Ability", "Action"]
)
foraging.add_ability(1, "Gather Berries")
foraging.add_ability(2, "Gather Herbs")
foraging.add_ability(3, "Gather Mushrooms")

def use_foraging(level):
    return foraging.use_ability(level)

# Define Fletching skill
fletching = Skill(
    name="Fletching",
    dependent_stat="Dexterity",
    skill_description="The art of crafting arrows and other projectiles.",
    skill_icon="fletching_icon.png",
    max_level=100,
    type="Crafting",
    skillups=["Ability", "Action"]
)
fletching.add_ability(1, "Craft Basic Arrows")
fletching.add_ability(2, "Craft Advanced Arrows")
fletching.add_ability(3, "Craft Master Arrows")

def use_fletching(level):
    return fletching.use_ability(level)

# Define Glassblowing skill
glassblowing = Skill(
    name="Glassblowing",
    dependent_stat="Dexterity",
    skill_description="The art of shaping glass.",
    skill_icon="glassblowing_icon.png",
    max_level=100,
    type="Crafting",
    skillups=["Ability", "Action"]
)
glassblowing.add_ability(1, "Create Simple Glass Objects")
glassblowing.add_ability(2, "Create Decorated Glass Objects")
glassblowing.add_ability(3, "Create Complex Glass Structures")

def use_glassblowing(level):
    return glassblowing.use_ability(level)

# Define Husbandry skill
husbandry = Skill(
    name="Husbandry",
    dependent_stat="Wisdom",
    skill_description="The care and breeding of livestock.",
    skill_icon="husbandry_icon.png",
    max_level=100,
    type="Crafting",
    skillups=["Ability", "Action"]
)
husbandry.add_ability(1, "Raise Chickens")
husbandry.add_ability(2, "Raise Sheep")
husbandry.add_ability(3, "Raise Cattle")

def use_husbandry(level):
    return husbandry.use_ability(level)

# Define Jewelrymaking skill
jewelrymaking = Skill(
    name="Jewelrymaking",
    dependent_stat="Dexterity",
    skill_description="The craft of creating jewelry.",
    skill_icon="jewelrymaking_icon.png",
    max_level=100,
    type="Crafting",
    skillups=["Ability", "Action"]
)
jewelrymaking.add_ability(1, "Create Simple Jewelry")
jewelrymaking.add_ability(2, "Create Decorated Jewelry")
jewelrymaking.add_ability(3, "Create Master Jewelry")

def use_jewelrymaking(level):
    return jewelrymaking.use_ability(level)

# Define Leatherworking skill
leatherworking = Skill(
    name="Leatherworking",
    dependent_stat="Strength",
    skill_description="The craft of working with leather.",
    skill_icon="leatherworking_icon.png",
    max_level=100,
    type="Crafting",
    skillups=["Ability", "Action"]
)
leatherworking.add_ability(1, "Create Simple Leather Items")
leatherworking.add_ability(2, "Create Durable Leather Items")
leatherworking.add_ability(3, "Create Master Leather Items")

def use_leatherworking(level):
    return leatherworking.use_ability(level)

# Define Lumberjacking skill
lumberjacking = Skill(
    name="Lumberjacking",
    dependent_stat="Strength",
    skill_description="The skill of cutting down trees and processing wood.",
    skill_icon="lumberjacking_icon.png",
    max_level=100,
    type="Crafting",
    skillups=["Ability", "Action"]
)
lumberjacking.add_ability(1, "Chop Down Small Trees")
lumberjacking.add_ability(2, "Chop Down Medium Trees")
lumberjacking.add_ability(3, "Chop Down Large Trees")

def use_lumberjacking(level):
    return lumberjacking.use_ability(level)

# Define Mining skill
mining = Skill(
    name="Mining",
    dependent_stat="Strength",
    skill_description="The skill of extracting minerals from the earth.",
    skill_icon="mining_icon.png",
    max_level=100,
    type="Crafting",
    skillups=["Ability", "Action"]
)
mining.add_ability(1, "Mine Stone")
mining.add_ability(2, "Mine Iron Ore")
mining.add_ability(3, "Mine Precious Gems")

def use_mining(level):
    return mining.use_ability(level)

# Define Pottery skill
pottery = Skill(
    name="Pottery",
    dependent_stat="Dexterity",
    skill_description="The art of making ceramic objects.",
    skill_icon="pottery_icon.png",
    max_level=100,
    type="Crafting",
    skillups=["Ability", "Action"]
)
pottery.add_ability(1, "Create Simple Pots")
pottery.add_ability(2, "Create Decorated Pots")
pottery.add_ability(3, "Create Complex Ceramic Objects")

def use_pottery(level):
    return pottery.use_ability(level)

# Define Runecarving skill
runecarving = Skill(
    name="Runecarving",
    dependent_stat="Wisdom",
    skill_description="The art of carving magical runes.",
    skill_icon="runecarving_icon.png",
    max_level=100,
    type="Crafting",
    skillups=["Ability", "Action"]
)
runecarving.add_ability(1, "Carve Simple Runes")
runecarving.add_ability(2, "Carve Complex Runes")
runecarving.add_ability(3, "Carve Master Runes")

def use_runecarving(level):
    return runecarving.use_ability(level)

# Define Scavenging skill
scavenging = Skill(
    name="Scavenging",
    dependent_stat="Dexterity",
    skill_description="The act of searching for and collecting useful items.",
    skill_icon="scavenging_icon.png",
    max_level=100,
    type="Crafting",
    skillups=["Ability", "Action"]
)
scavenging.add_ability(1, "Find Basic Items")
scavenging.add_ability(2, "Find Rare Items")
scavenging.add_ability(3, "Find Legendary Items")

def use_scavenging(level):
    return scavenging.use_ability(level)

# Define Stoneworking skill
stoneworking = Skill(
    name="Stoneworking",
    dependent_stat="Strength",
    skill_description="The craft of shaping and working with stone.",
    skill_icon="stoneworking_icon.png",
    max_level=100,
    type="Crafting",
    skillups=["Ability", "Action"]
)
stoneworking.add_ability(1, "Shape Simple Stone Objects")
stoneworking.add_ability(2, "Shape Detailed Stone Objects")
stoneworking.add_ability(3, "Shape Complex Stone Structures")

def use_stoneworking(level):
    return stoneworking.use_ability(level)

# Define Tailoring skill
tailoring = Skill(
    name="Tailoring",
    dependent_stat="Dexterity",
    skill_description="The craft of making clothing and fabric items.",
    skill_icon="tailoring_icon.png",
    max_level=100,
    type="Crafting",
    skillups=["Ability", "Action"]
)
tailoring.add_ability(1, "Sew Simple Garments")
tailoring.add_ability(2, "Sew Decorated Garments")
tailoring.add_ability(3, "Sew Master Garments")

def use_tailoring(level):
    return tailoring.use_ability(level)

# Define Tinkering skill
tinkering = Skill(
    name="Tinkering",
    dependent_stat="Dexterity",
    skill_description="The craft of creating mechanical devices.",
    skill_icon="tinkering_icon.png",
    max_level=100,
    type="Crafting",
    skillups=["Ability", "Action"]
)
tinkering.add_ability(1, "Create Simple Mechanisms")
tinkering.add_ability(2, "Create Complex Mechanisms")
tinkering.add_ability(3, "Create Master Mechanisms")

def use_tinkering(level):
    return tinkering.use_ability(level)


# Combat Skills
# Define Heavy Armor skill
heavy_armor = Skill(
    name="Heavy Armor",
    dependent_stat="Strength",
    skill_description="Proficiency in wearing heavy armor.",
    skill_icon="heavy_armor_icon.png",
    max_level=100,
    type="Combat",
    skillups=["Ability", "Action"]
)
heavy_armor.add_ability(1, "Basic Heavy Armor Proficiency")
heavy_armor.add_ability(2, "Intermediate Heavy Armor Proficiency")
heavy_armor.add_ability(3, "Advanced Heavy Armor Proficiency")

def use_heavy_armor(level):
    return heavy_armor.use_ability(level)

# Define Light Armor skill
light_armor = Skill(
    name="Light Armor",
    dependent_stat="Agility",
    skill_description="Proficiency in wearing light armor.",
    skill_icon="light_armor_icon.png",
    max_level=100,
    type="Combat",
    skillups=["Ability", "Action"]
)
light_armor.add_ability(1, "Basic Light Armor Proficiency")
light_armor.add_ability(2, "Intermediate Light Armor Proficiency")
light_armor.add_ability(3, "Advanced Light Armor Proficiency")

def use_light_armor(level):
    return light_armor.use_ability(level)

# Define Medium Armor skill
medium_armor = Skill(
    name="Medium Armor",
    dependent_stat="Dexterity",
    skill_description="Proficiency in wearing medium armor.",
    skill_icon="medium_armor_icon.png",
    max_level=100,
    type="Combat",
    skillups=["Ability", "Action"]
)
medium_armor.add_ability(1, "Basic Medium Armor Proficiency")
medium_armor.add_ability(2, "Intermediate Medium Armor Proficiency")
medium_armor.add_ability(3, "Advanced Medium Armor Proficiency")

def use_medium_armor(level):
    return medium_armor.use_ability(level)

# Define Tactics skill
tactics = Skill(
    name="Tactics",
    dependent_stat="Intelligence",
    skill_description="Strategies for effective combat.",
    skill_icon="tactics_icon.png",
    max_level=100,
    type="Combat",
    skillups=["Ability", "Discipline"]
)
tactics.add_ability(1, "Basic Battle Tactics")
tactics.add_ability(2, "Advanced Battle Tactics")
tactics.add_ability(3, "Master Battle Tactics")

def use_tactics(level):
    return tactics.use_ability(level)

# Faith Skills
# Define Mercy skill
mercy = Skill(
    name="Mercy",
    dependent_stat="Wisdom",
    skill_description="The virtue of showing compassion and forgiveness.",
    skill_icon="mercy_icon.png",
    max_level=100,
    type="Faith",
    skillups=["Hobby", "Discipline"]
)
mercy.add_ability(1, "Show Compassion")
mercy.add_ability(2, "Forgive Sins")
mercy.add_ability(3, "Blessing")

def use_mercy(level):
    return mercy.use_ability(level)

# Define Vengeance skill
vengeance = Skill(
    name="Vengeance",
    dependent_stat="Wisdom",
    skill_description="The act of seeking retribution.",
    skill_icon="vengeance_icon.png",
    max_level=100,
    type="Faith",
    skillups=["Hobby", "Discipline"]
)
vengeance.add_ability(1, "Seek Retribution")
vengeance.add_ability(2, "Curse")
vengeance.add_ability(3, "Divine Wrath")

def use_vengeance(level):
    return vengeance.use_ability(level)

# Magic Skills
# Define Air Magic skill
air_magic = Skill(
    name="Air Magic",
    dependent_stat="Intelligence",
    skill_description="The power to control and conjure air.",
    skill_icon="air_magic_icon.png",
    max_level=100,
    type="Magic",
    skillups=["Ability", "Action"]
)
air_magic.add_ability(1, "Cast Wind Blade")
air_magic.add_ability(2, "Summon Air Elemental")
air_magic.add_ability(3, "Hurricane")

def use_air_magic(level):
    return air_magic.use_ability(level)

# Define Dark Magic skill
dark_magic = Skill(
    name="Dark Magic",
    dependent_stat="Intelligence",
    skill_description="The power to control and conjure darkness.",
    skill_icon="dark_magic_icon.png",
    max_level=100,
    type="Magic",
    skillups=["Ability", "Action"]
)
dark_magic.add_ability(1, "Cast Shadow Bolt")
dark_magic.add_ability(2, "Summon Dark Elemental")
dark_magic.add_ability(3, "Eclipse")

def use_dark_magic(level):
    return dark_magic.use_ability(level)

# Define Earth Magic skill
earth_magic = Skill(
    name="Earth Magic",
    dependent_stat="Intelligence",
    skill_description="The power to control and conjure earth.",
    skill_icon="earth_magic_icon.png",
    max_level=100,
    type="Magic",
    skillups=["Ability", "Action"]
)
earth_magic.add_ability(1, "Cast Rock Throw")
earth_magic.add_ability(2, "Summon Earth Elemental")
earth_magic.add_ability(3, "Earthquake")

def use_earth_magic(level):
    return earth_magic.use_ability(level)

# Define Fire Magic skill
fire_magic = Skill(
    name="Fire Magic",
    dependent_stat="Intelligence",
    skill_description="The power to control and conjure fire.",
    skill_icon="fire_magic_icon.png",
    max_level=100,
    type="Magic",
    skillups=["Ability", "Action"]
)
fire_magic.add_ability(1, "Cast Fireball")
fire_magic.add_ability(2, "Summon Flame Elemental")
fire_magic.add_ability(3, "Inferno")

def use_fire_magic(level):
    return fire_magic.use_ability(level)

# Define Healing Magic skill
healing_magic = Skill(
    name="Healing Magic",
    dependent_stat="Intelligence",
    skill_description="The power to heal wounds and ailments.",
    skill_icon="healing_magic_icon.png",
    max_level=100,
    type="Magic",
    skillups=["Ability", "Action"]
)
healing_magic.add_ability(1, "Heal Wounds")
healing_magic.add_ability(2, "Cure Disease")
healing_magic.add_ability(3, "Revive")

def use_healing_magic(level):
    return healing_magic.use_ability(level)

# Define Light Magic skill
light_magic = Skill(
    name="Light Magic",
    dependent_stat="Intelligence",
    skill_description="The power to control and conjure light.",
    skill_icon="light_magic_icon.png",
    max_level=100,
    type="Magic",
    skillups=["Ability", "Action"]
)
light_magic.add_ability(1, "Cast Light Beam")
light_magic.add_ability(2, "Summon Light Elemental")
light_magic.add_ability(3, "Radiance")

def use_light_magic(level):
    return light_magic.use_ability(level)

# Define Water Magic skill
water_magic = Skill(
    name="Water Magic",
    dependent_stat="Intelligence",
    skill_description="The power to control and conjure water.",
    skill_icon="water_magic_icon.png",
    max_level=100,
    type="Magic",
    skillups=["Ability", "Action"]
)
water_magic.add_ability(1, "Cast Water Bolt")
water_magic.add_ability(2, "Summon Water Elemental")
water_magic.add_ability(3, "Tsunami")

def use_water_magic(level):
    return water_magic.use_ability(level)