# Skills.py

def sword_slash(targeted_monster):
    if targeted_monster:
        targeted_monster.hit_points -= 5
        return f"Sword Slash hits {targeted_monster.username} for 5 HP!"
    return "No targeted monster."

def magic_missile(targeted_monster):
    if targeted_monster:
        targeted_monster.hit_points -= 5
        return f"Magic Missile hits {targeted_monster.username} for 5 HP!"
    return "No targeted monster."