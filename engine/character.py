"""
Provides character archetypes (aka classes)
"""
from dataclasses import dataclass
from . import gear as g
from . import spells as spells
from . import elements as el
from . import conlang
import numpy as np

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

    # --- Required EXP ---
    @property
    def required_exp(self):
        return round(10000 / (1 + np.e ** (-.1 * (self.level - 50))) + 26)

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
            self.attribute_points += 2
            self.current_health += round(self.max_health * .33)

    # -- Max Health ---
    @property
    def max_health(self):
        return self._max_health \
            + (10 * (self.attributes["constitution"] - 1)) \
            + 10 * (self.level - 1)

    @max_health.setter
    def max_health(self, value):
        self._max_health += value

    # --- Current Health ---
    @property
    def current_health(self) -> int:
        return self._current_health

    @current_health.setter
    def current_health(self, value):
        self._current_health = value
        if self._current_health > self.max_health:
            self._current_health = self.max_health
        elif self._current_health < 0:
            self._current_health = 0

    # --- Physical Attack ---
    @property
    def physical_attack(self):
        return self._physical_attack + \
            (self.attributes["strength"] - 1) * 5

    # --- Physical Defense ---
    @property
    def physical_defense(self):
        return self._physical_defense \
            + (self.attributes["strength"] - 1) * 2 \
            + (self.attributes["constitution"] - 1) * 3

    # --- Magic Attack ---
    @property
    def magic_attack(self) -> int:
        from_attributes = round((
            self.light + \
            self.dark + \
            self.electric + \
            self.fire + \
            self.water + \
            self.earth + \
            self.air + \
            self.metal + \
            self.acid + \
            self.psychic + \
            self.weird
            ) / 11)

        return self._magic_attack + \
            (self.attributes["intelligence"] - 1) * 5 + \
                from_attributes

    # --- Magic Defense ---
    @property
    def magic_defense(self) -> int:
        from_attributes = round((
            self.light + \
            self.dark + \
            self.electric + \
            self.fire + \
            self.water + \
            self.earth + \
            self.air + \
            self.metal + \
            self.acid + \
            self.psychic + \
            self.weird
            ) / 11)
        return self._magic_attack + \
            (self.attributes["intelligence"] - 1) * 5 + \
                from_attributes

    # --- Elemental ---
    @property
    def light(self) -> int:
        return (self.attributes["light"] - 1) * 10 + 1

    @property
    def dark(self) -> int:
        return (self.attributes["dark"] - 1) * 10 + 1

    @property
    def electric(self) -> int:
        return (self.attributes["electric"] - 1) * 10 + 1

    @property
    def fire(self) -> int:
        return (self.attributes["fire"] - 1) * 10 + 1

    @property
    def water(self) -> int:
        return (self.attributes["water"] - 1) * 10 + 1

    @property
    def earth(self) -> int:
        return (self.attributes["earth"] - 1) * 10 + 1

    @property
    def air(self) -> int:
        return (self.attributes["air"] - 1) * 10 + 1

    @property
    def metal(self) -> int:
        return (self.attributes["metal"] - 1) * 10 + 1

    @property
    def acid(self) -> int:
        return (self.attributes["acid"] - 1) * 10 + 1

    @property
    def psychic(self) -> int:
        return (self.attributes["psychic"] - 1) * 10 + 1

    @property
    def weird(self) -> int:
        return (self.attributes["weird"] - 1) * 10 + 1

    # An extra bit to track current stats vs max / normal


    def __init__(self, first_name: str = "", last_name: str = ""):
        self.first_name = first_name
        self.last_name = last_name
        self.level = 1
        self.money: float = 0
        self.spells = []
        self.inventory = []
        self.gear: 'g.GearSet' = g.GearSet()
        self.attributes = {
            "strength": 1,
            "constitution": 1,
            "intelligence": 1,
            # Elemental Affinities
            "light": 1,
            "dark": 1,
            "electric": 1,
            "fire": 1,
            "water": 1,
            "earth": 1,
            "air": 1,
            "metal": 1,
            "acid": 1,
            "psychic": 1,
            "weird": 1
        }
        self._experience = 0
        self._max_health = BASE_STATS["health"]
        self._current_health = BASE_STATS["health"]
        self._physical_attack = BASE_STATS["physical_attack"]
        self._physical_defense = BASE_STATS["physical_defense"]
        self._magic_attack = BASE_STATS["magic_attack"]
        self._magic_defense = BASE_STATS["magic_defense"]
        self.attribute_points = 0
        self.current_physical_attack: int = self.physical_attack
        self.current_physical_defense: int = self.physical_defense
        self.current_magic_attack: int = self.magic_attack
        self.current_magic_defense: int = self.magic_defense
        self.stat_modifiers = {}

    def apply_attribute_points(self, amount: int, target: str):
        if self.attribute_points >= amount:
            self.attribute_points -= amount
            self.attributes[target] += amount

    def __repr__(self):
        return f"""
        {(self.first_name.capitalize() 
        + " "
        + self.last_name.capitalize()).strip()}: Level {self.level}
        {self.experience} / {self.required_exp} EXP
        Attribute Points: {self.attribute_points}

        Strength: {self.attributes["strength"]}
        Intelligence: {self.attributes["intelligence"]}
        Constitution: {self.attributes["constitution"]}
        Light: {self.attributes["light"]} -> {self.light}
        Dark: {self.attributes["dark"]} -> {self.dark}
        Electric: {self.attributes["electric"]} -> {self.electric}
        Fire: {self.attributes["fire"]} -> {self.fire}
        Water: {self.attributes["water"]} -> {self.water}
        Earth: {self.attributes["earth"]} -> {self.earth}
        Air: {self.attributes["air"]} -> {self.air}
        Metal: {self.attributes["metal"]} -> {self.metal}
        Acid: {self.attributes["acid"]} -> {self.acid}
        Psychic: {self.attributes["psychic"]} -> {self.psychic}
        Weird: {self.attributes["weird"]} -> {self.weird}
        {self.gear}
        Abilities: {self.spells}
        Health: {self.current_health}/{self.max_health}
        Physical Attack: {self.physical_attack}
        Physical Defense: {self.physical_defense}
        Magic Attack: {self.magic_attack}
        Magic Defense: {self.magic_defense}
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

    def give_exp(self, amount: int):
        self.data.experience += amount

    def learn_spell(self, spell: spells.Spell):
        self.data.spells.append(spell)

    def apply_attribute_points(self, amount: int, target: str):
        return self.data.apply_attribute_points(amount, target)

    # combat utils
    def take_damage(self, damage):
        self.data.current_health -= damage

    def recover_health(self, amount):
        self.data.current_health += round(amount)

    # dunders
    def __repr__(self):
        return str(self.data)
