"""
Provides archetypes and engine with gear classes and functions
"""
import numpy as np
from . import elements as el
from . import name_provider as namer
from abc import ABC
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from engine import character

RARITY_MULT = {
    "common": 1,
    "uncommon": 1.1,
    "rare": 1.2,
    "unique": 1.3,
    "legendary": 1.5
}

class GearItemData:
    stats_per_level = {
        "max_health": 30,
        "physical_attack": 10,
        "physical_defense": 10,
        "magic_attack": 10,
        "magic_defense": 10,
        "strength": 1,
        "constitution": 1,
        "intelligence": 1,
        "light": 2,
        "dark": 2,
        "electric": 2,
        "fire": 2,
        "water":2,
        "earth": 2,
        "air": 2,
        "metal": 2,
        "acid": 2,
        "psychic": 2,
        "weird": 2
    }
    @property
    def required_exp(self):
        return round(10_000 / (1 + np.e ** (-.1 * (self.level - 25))))

    # --- EXP ---
    @property
    def experience(self):
        return self._experience

    @experience.setter
    def experience(self, value):
        self._experience = value
        while self._experience >= self.required_exp:
            self._experience -= self.required_exp
            self.level += 1
            for stat in self.stats:
                self.stats[stat] = round(self.stats[stat] \
                    + self.stats_per_level[stat] * RARITY_MULT[self.rarity])


    def __init__(self, element: el.Element = None):
        self.name: str = ''
        self.level: int = 1
        self._experience: int = 0
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
    
    def give_exp(self, amount: int):
        self.data.experience += amount

    def __repr__(self):
        return f"""
    {self.data.name}: Level {self.data.level} {self.__class__.__name__}
    {self.data.experience} / {self.data.required_exp} EXP
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
