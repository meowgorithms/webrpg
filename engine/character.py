"""
Provides character archetypes (aka classes)
"""
from . import gear as g
from . import spells as spells
from . import elements as el
from . import conlang
from . import items
import numpy as np
from dataclasses import dataclass, field

# TODO Create leveling system
# con, str, int, elemental affinity
# needs to be done first,
# item requirement generation depends on level system
# item stat generation depends on item requirements


BASE_STATS = {
    "health": 100,
    "physical_attack": 5,
    "physical_defense": 5,
    "magic_attack": 5,
    "magic_defense": 5
}



class CharacterData:
    """
    Data container for archetypes
    """
    first_name: str = ""
    last_name: str = ""
    level = 1
    money: float = 0
    spells = []
    inventory = []
    gear: 'g.GearSet' = g.GearSet()

    # --- Required EXP ---
    @property
    def required_exp(self):
        return round(10000 / (1 + np.e ** (-.1 * (self.level - 50))) + 26)

    # --- EXP ---
    _experience = 0
    @property
    def experience(self):
        return self._experience

    @experience.setter
    def experience(self, value):
        self._experience = value
        while self._experience >= self.required_exp:
            self._experience -= self.required_exp
            self.level += 1
            self.attribute_points += 2
            self.current_health += round(self.max_health * .33)



    # Attributes
    _strength = 1
    @property
    def strength(self):
        return self._strength
    
    @strength.setter
    def strength(self, value):
        if self.attribute_points >= value:
            self._strength = value
            self.attribute_points -= value

    constitution = 1
    intelligence = 1 # -> extra attack and defense for ALL elements
    # TODO expand into elements
    electric_affinity = 1 # -> extra electric attack and defense

    # 2 points granted upon leveling up
    attribute_points = 0

    # Base stats
    base_health: int = BASE_STATS["health"]
    base_physical_attack: int = BASE_STATS["physical_attack"]
    base_physical_defense: int = BASE_STATS["physical_defense"]
    base_magic_attack: int = BASE_STATS["magic_attack"]
    base_magic_defense: int = BASE_STATS["magic_defense"]

    # -- Max Health ---
    @property
    def max_health(self):
        return self.base_health \
            + (5 * (self.constitution - 1)) \
            + 2 * (self.level - 1)

    # --- Current Health ---
    _current_health = base_health + (5 * (constitution - 1))
    @property
    def current_health(self) -> int:
        return self._current_health

    # --- Physical Attack ---
    @property
    def physical_attack(self):
        return self.base_physical_attack + (self.strength - 1) * 5

    # --- Physical Defense ---
    @property
    def physical_defense(self):
        return self.base_physical_defense \
            + (self.strength - 1) * 2 \
            + (self.constitution - 1) * 3

    magic_attack: int = base_magic_attack
    magic_defense: int = base_magic_defense

    # An extra bit to track current stats vs max / normal
    

    @current_health.setter
    def current_health(self, value):
        self._current_health = value
        if self._current_health > self.max_health:
            self._current_health = self.max_health
        elif self._current_health < 0:
            self._current_health = 0

    current_physical_attack: int = physical_attack
    current_physical_defense: int = physical_defense
    current_magic_attack: int = magic_attack
    current_magic_defense: int = magic_defense


    def __init__(self, first_name: str = "", last_name: str = ""):
        self.first_name = first_name
        self.last_name = last_name


    def __repr__(self):
        return f"""
        {(self.first_name.capitalize() 
        + " "
        + self.last_name.capitalize()).strip()}: Level {self.level}
        {self.experience} / {self.required_exp} EXP
        Attribute Points: {self.attribute_points}
        
        Strength: {self.strength}
        Intelligence: {self.intelligence}
        Constitution: {self.constitution}
        {self.gear}
        Abilities: {self.spells}
        Health: {self.current_health}/{self.max_health}
        Current Physical Attack: {self.current_physical_attack}
        Current Physical Defense: {self.current_physical_defense}
        Current Magic Attack: {self.current_magic_attack}
        Current Magic Defense: {self.current_magic_defense}
        """


class Character:
    def __init__(self,
                 first_name: str = '',
                 last_name: str = '',
                 random_name: bool = False):
        self.data = CharacterData(first_name, last_name)

        if random_name \
        or (first_name == '' and last_name == ''):
            self.data.first_name = conlang.create_conlang_word(length=8)
            self.data.last_name = conlang.create_conlang_word(length=8)

    # data utils
    def equip(self, item: g.GearItem):
        self.data.gear.equip(item)

    def learn_spell(self, spell: spells.Spell):
        self.data.spells.append(spell)

    def apply_attribute_point(self, target: str):
        attr_dict = {
            "strength": self.data.strength,
            "constitution": self.data.constitution,
            "intelligence": self.data.intelligence
        }
        attr_dict[target] += 5

    # combat utils
    def take_damage(self, damage):
        self.data.current_health -= damage

    def recover_health(self, amount):
        self.data.current_health += round(amount)

    # dunders
    def __repr__(self):
        return str(self.data)
