"""
Provides archetypes and engine with gear classes and functions
"""
from dataclasses import dataclass, field
from . import elements as el
from . import name_provider as namer
from random import choices, choice
from abc import ABC


@dataclass
class GearItemData:
    name: str = None
    element: el.Element = None
    level: int = 1
    requirements: dict = None
    stats: dict = None

    def __init__(self, element: el.Element = None):
        if element is not None:
            self.element = element
        else:
            self.element = el.get_random_element()


class GearItem(ABC):
    def __init__(self, element: el.Element = None):
        self.data = GearItemData(element)


class Armor(GearItem):
    def __init__(self, element: el.Element = None):
        super().__init__(element=element)
        element_word = el.get_random_element_word(self.data.element)
        self.data.name = namer.create_name(namer.ARMOR_FORMATS,
                                           element_word)

class Weapon(GearItem):
    def __init__(self, element: el.Element = None):
        super().__init__(element=element)
        element_word = el.get_random_element_word(self.data.element)
        self.data.name = namer.create_name(namer.WEAPON_FORMATS,
                                           element_word)


class SpecialItem(GearItem):
    def __init__(self, element: el.Element = None):
        super().__init__(element=element)
        element_word = el.get_random_element_word(self.data.element)
        self.data.name = namer.create_name(namer.SPECIAL_ITEM_FORMATS,
                                           element_word)


class GearSet:
    """
    Container for equippables
    """
    armor: 'list[Armor]' = []
    left_hand_weapon: Weapon = None
    right_hand_weapon: Weapon = None
    special: 'list[SpecialItem]' = []
    special_max_size = 5
    armor_max_size = 5

    def equip_armor(self, item: Armor):
        if len(self.armor) >= self.armor_max_size:
            return "Armor slots full"
        else:
            self.armor.append(item)
            return f"Equipped {item.name}"

    def __repr__(self):
        return f"""
        Armor:
            {[item for item in self.armor]}
        Left Hand:
            {self.left_hand_weapon}
        Right Hand:
            {self.right_hand_weapon}
        Special:
            {[item for item in self.special]}
        """
