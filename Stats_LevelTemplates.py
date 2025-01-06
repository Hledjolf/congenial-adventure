# Effects.py


def add_effect(character, effect):
    '''Add an effect to the character.'''
    if not hasattr(character, 'effects'):
        character.effects = []
    character.effects.append(effect)

def remove_effect(character, effect):
    '''Remove an effect from the character.'''
    if hasattr(character, 'effects'):
        character.effects = [e for e in character.effects if e != effect]

def nullify_effect(character, effect):
    '''Nullify a specific effect on the character.'''
    if hasattr(character, 'effects'):
        character.effects = [e for e in character.effects if e != effect]
        character.effects.append(f'Nullified {effect}')