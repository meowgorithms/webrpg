"""
Provides ability class definitions, damage types, and other related helper
classes and functions
"""
from abc import abstractmethod
from dataclasses import dataclass
from enum import Enum, auto
from random import uniform, choice
from .name_provider import SPELL_FORMATS, create_spell_name


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
        # ------ Currently weird
        self.magic_penetration = 0
        self.physical_penetration = 0
        # ------
        self.user = user
        self.archetype_bonus = False
        self.max_level = 10

    @abstractmethod
    def use_ability(self):
        pass

    @abstractmethod
    def __call__(self):
        return self.use_ability

    def __repr__(self):
        return f"{self.name}: Level {self.level}"


@dataclass(init=True)
class Abilities:
    """
    Container for abilities
    """
    abilities = []
    def add_ability(self, ability: Ability):
        setattr(self, f"{ability.name}", ability)
        self.abilities.append(ability)

    def __repr__(self):
        return f"{[ability for ability in self.abilities]}"
