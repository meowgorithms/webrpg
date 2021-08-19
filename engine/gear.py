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
    item_type: str
    def __init__(self, element: el.Element = None):
        self.data = GearItemData(element)

    def __repr__(self):
        return f"""
    {self.data.name}: Level {self.data.level} {self.__class__.__name__}
    Rarity: {self.data.rarity.capitalize()}
    Element: {self.data.element.name.lower().capitalize()}
    Requirements:
        {[req + ': ' + str(val) for req, val in self.data.requirements.items()]}
    Stats:
        {[stat + ': ' + str(self.data.stats[stat]) for stat in self.data.stats]}
"""


class Armor(GearItem):
    item_type = 'armor'
    def __init__(self, element: el.Element = None):
        super().__init__(element=element)
        element_word = el.get_random_element_word(self.data.element)
        self.data.name = namer.create_name(namer.ARMOR_FORMATS,
                                           element_word)

    def __repr__(self):
        return super().__repr__()


class Weapon(GearItem):
    item_type = 'weapon'
    def __init__(self, element: el.Element = None):
        super().__init__(element=element)
        element_word = el.get_random_element_word(self.data.element)
        self.data.name = namer.create_name(namer.WEAPON_FORMATS,
                                           element_word)
    
    def __repr__(self):
        return super().__repr__()


class SpecialItem(GearItem):
    item_type = 'special'
    def __init__(self, element: el.Element = None):
        super().__init__(element=element)
        element_word = el.get_random_element_word(self.data.element)
        self.data.name = namer.create_name(namer.SPECIAL_ITEM_FORMATS,
                                           element_word)

    def __repr__(self):
        return super().__repr__()

# This is really, really dumb
# TODO Refactor this garbage
class GearSet:
    """
    Container for equippables
    """

    def __init__(self):
        self.items = {
            'armor': [],
            'weapon': [],
            'special': []
        }
        self._register = []
        self.max = {
            'armor': 5,
            'weapon': 2,
            'special': 3
        }

    def equip(self, item: GearItem):
        if len(self.items[item.item_type]) >= self.max[item.item_type]:
            print(f"Max amount of {item.item_type}, please dequip one and try again")
            return True
        if item in self._register:
            print(f"{item.data.name} is already equipped")
            # equipped is true
            return True
        else:
            self._register.append(item)
            self.items[item.item_type].append(item)
            #equipped is false
            return False

    def dequip(self, item: GearItem):
        if not self._register:
            print("No items equipped")
        elif item in self._register:
            self._register.remove(item)
            self.items[item.item_type].remove(item)
        else:
            print(f'{item.data.name} not equipped?')

    def __repr__(self):
        return f"""
        {self.items}
        """
