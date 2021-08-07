"""
Provides spell class definitions, damage types, and other related helper
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


class Spell:
    """
    Base class for all abilities
    """

    def __init__(self, user):
        self.name = create_spell_name(SPELL_FORMATS)
        self.level = 1
        self.user = user
        self.max_level = 10

    @abstractmethod
    def cast(self):
        pass

    @abstractmethod
    def __call__(self):
        return self.cast

    def __repr__(self):
        return f"{self.name}: Level {self.level}"
