"""
Provides archetypes and engine with gear classes and functions
"""
from dataclasses import dataclass, field
from . import elements as el
from . import name_provider as namer


class Armor:
    level: int = 1
    element: el.Element = el.Element.NONE
    name: namer.create_name(namer.ARMOR_FORMATS)


class Weapon:
    level: int = 1
    element: el.Element = el.Element.NONE
    name: namer.create_name(namer.WEAPON_FORMATS)


class SpecialItem:
    level: int = 1
    element: el.Element = el.Element.NONE
    name = namer.create_name(namer.SPECIAL_ITEM_FORMATS)


@dataclass()
class GearSet:
    """
    Container for equippable
    """
    armor: list[Armor] = []
    left_hand_weapon: Weapon = None
    right_hand_weapon: Weapon = None
    special: list[SpecialItem] = []
    special_max_size = 5
    armor_max_size = 5

    def equip_armor(self, item: Armor):
        if len(self.armor) >= self.armor_max_size:
            return "Armor slots full"
        else:
            self.armor.append(item)
            return f"Equipped {item.name}"
    
    def __repr__(self):
        return f"""Armor:
            {[item for item in self.armor]}
        Left Hand:
            {self.left_hand_weapon}
        Right Hand:
            {self.right_hand_weapon}
        Special:
            {[item for item in self.special]}
        """
