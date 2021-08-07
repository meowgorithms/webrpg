"""
Provides archetypes and engine with gear classes and functions
"""
from dataclasses import dataclass, field
from .gear_items import ArcaneFocus, Robe, Hood, Gloves

@dataclass()
class GearSet:
    """
    Container for a full set of gear, may also serve as a base class for
    special gear sets
    """
    name: str = field(init=True)
