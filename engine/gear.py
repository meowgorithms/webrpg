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

@dataclass(init=True)
class ArcaneSet(GearSet):
    """
    Base class for arcane gearsets
    """
    # TODO FIX THIS - CURRENT IS TEMPORARY
    arcane_focus: ArcaneFocus = ArcaneFocus("ArcaneFocus")
    hood: Hood = Hood("Hood")
    robe: Robe = Robe("Robe")
    gloves: Gloves = Gloves("Gloves")
  

    def __repr__(self) -> str:
        return f"""
        Hood: {self.hood}
        Robe: {self.robe}
        Gloves: {self.gloves}
        Arcane Focus: {self.arcane_focus}
        """
class QuantumGearSet(ArcaneSet):
    """
    Gear set specifically for Quantum
    """
    arcane_focus: ArcaneFocus


    def __init__(self):
        super().__init__("Quantum Set")

    def __repr__(self) -> str:
        return super().__repr__()
