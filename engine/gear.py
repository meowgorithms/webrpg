"""
Provides archetypes and engine with gear classes and functions
"""
from dataclasses import dataclass, field
from . import elements as el
from . import name_provider as namer
from random import choices, choice
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from engine import character


class GearItemData:
    def __init__(self, element: el.Element = None):
        self.name: str = ''
        self.level: int = 1
        self.experience: int = 0
        self.requirements: dict = {}
        self.stats: dict = {}
        self.rarity: str = ''
        if element is not None:
            self.element = element
        else:
            self.element = el.get_random_element()


class GearItem(ABC):
    def __init__(self, element: el.Element = None):
        self.data = GearItemData(element)

    def __repr__(self):
        return f"""{self.data.name}: Level {self.data.level} {self.__class__.__name__}
    Rarity: {self.data.rarity.capitalize()}
    Element: {self.data.element.name.lower().capitalize()}
    Requirements:
        {[req + ': ' + str(val) for req, val in self.data.requirements.items()]}
    Stats:
        {[stat + ': ' + str(self.data.stats[stat]) for stat in self.data.stats]}
"""


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

    def __init__(self):
        self.armor: 'list[Armor]' = []
        self.weapons: 'list[Weapon]' = []
        self.special: 'list[SpecialItem]' = []
        self.special_max_size = 5
        self.armor_max_size = 5
        self.weapon_max = 2

    def equip(self, item: GearItem):
        if type(item) is Armor:
            self.__equip_armor__(item)
        elif type(item) is Weapon:
            self.__equip_weapon__(item)
        elif type(item) is SpecialItem:
            self.__equip_special_item__(item)

    def __equip_special_item__(self, special_item: SpecialItem):
        if len(self.special) >= self.special_max_size:
            return "Special Item slots full"
        else:
            self.special.append(special_item)

    def __equip_weapon__(self, weapon: Weapon):
        if len(self.weapons) >= self.weapon_max:
            print("Oh noes! You've got your hands full!! D:")
            return "Weapon slots full"
        else:
            self.weapons.append(weapon)
            return f"Equipped {weapon.data.name}"    

    def __equip_armor__(self, armor_item: Armor):
        if len(self.armor) >= self.armor_max_size:
            return "Armor slots full"
        else:
            self.armor.append(armor_item)
            return f"Equipped {armor_item.data.name}"

    def __repr__(self):
        return f"""
        Armor:
            {[item.data for item in self.armor]}
        Weapons:
            {[item.data for item in self.weapons]}
        Special:
            {[item.data for item in self.special]}
        """

