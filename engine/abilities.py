"""
Provides ability class definitions and helper functions
"""
from engine.archetypes import *

# Should this be coded into the archetypes?

# This will future proof my lack of executive function
# IF I choose to let archetypes share abilities, this will allow for that freedom
class Ability:
    """
    Base class for all abilities
    """
    def __init__(self, name):
        self.name = name
        self.level = 1


# Quantum
# -------
class Tunnel(Ability):
    """
    Penetrates enemy's magic defense, dealing extra damage
    """
    # TODO: Choose where the damage is decided:
    # Here or in Archetype classes
    def __init__(self, archetype: Archetype):
        super().__init__("Tunnel")
        self.damage = archetype.base_magic_attack * archetype.level * self.level
    
    def attack(self, opponent: Archetype):
        pass
