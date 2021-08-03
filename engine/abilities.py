"""
Provides ability class definitions, damage types, and other related helper
classes and functions
"""
from abc import abstractmethod
from enum import Enum, auto
from typing import TYPE_CHECKING

# Should this be coded into the archetypes?

class DamageType(Enum):
    """
    Provides damage types

    This class can be extended/refactored later to provide more specific damage
    types
    """
    PHYSICAL = auto()
    MAGIC = auto()


# This will future proof my lack of executive function
# IF I choose to let archetypes share abilities, this will allow for that freedom
class Ability:
    """
    Base class for all abilities
    """
    


    def __init__(self, name, user):
        self.name = name
        self.level = 1
        self.magic_penetration = 0
        self.physical_penetration = 0
        self.user = user
        self.archetype_bonus = False
    
    @abstractmethod
    def use_ability(self):
        pass

# Quantum
# -------
class Tunnel(Ability):
    """
    An ability primarily belonging to the Quantum Archetype
    Penetrates enemy's magic defense, dealing extra damage
    """
    # TODO: Choose where the damage is decided:
    # Here or in Archetype classes
    # TODO: Add hard coded values to database, query here for them instead -
    # allows for easy balance changes
    def __init__(self, user):
        super().__init__("Tunnel", user)
        self.max_level = 10 # arbitrary max level
        self.damage_type = DamageType.MAGIC
        self.base_attack = 5
        # ability level and archetype determine amount of penetration
        self.magic_penetration = self.level * 2

        # Check user archetype and set bonus flag
        if user.name == "Quantum":
            self.archetype_bonus = True


    def use_ability(self, target):
        # Check archetype bonus flag
        if self.archetype_bonus:
            self.magic_penetration *= 2

        # calculate scaled ability damage
        damage = (self.base_attack + self.user.base_magic_attack) * self.user.level * self.level
        # calculate damage received
        damage = damage * (damage / (damage + target.magic_defense))
        target.take_damage(damage)



