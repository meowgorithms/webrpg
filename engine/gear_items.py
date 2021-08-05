"""
Provides gear items for GearSet module
"""
from dataclasses import dataclass, field
from abc import ABC

@dataclass(init=True)
class ArcaneGearItem(ABC):
    """
    Base class for arcane gear items - 
    ALL arcane gear items inherit first from this class
    """
    name: str
    level: int = 1
    max_level: int = 10

@dataclass(init=True)
class ArcaneFocus(ArcaneGearItem):
    """
    Base class for arcane focus items
    """
    magic_attack: int = 0
    magic_defense: int = 0


@dataclass(init=True)
class Hood(ArcaneGearItem):
    """
    Base class for Hoods
    """
    health: int = 0
    magic_defense: int = 0


@dataclass(init=True)
class Robe(ArcaneGearItem):
    """
    Base class for Robes
    """
    health: int = 0
    magic_defense: int = 0
    physical_defense: int = 0


@dataclass(init=True)
class Gloves(ArcaneGearItem):
    """
    Base class for Gloves
    """
    magic_attack: int = 0
    magic_defense: int = 0
