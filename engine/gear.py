"""
Provides archetypes and engine with gear classes and functions
"""

from os import name


class GearSet:
    """
    Container for a full set of gear, may also serve as a base class for
    special gear sets
    """
    def __init__(self, name):
        self.name = name

class ArcaneSet(GearSet):
    """
    Base class for arcane gearsets
    """
    def __init__(self):
        super().__init__(self, "Arcane Set")
        self.robe