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
# con, str, int, ?
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


@dataclass(init=True)
class CharacterData:
    """
    Data container for archetypes
    """
    first_name: str = field(init=True)
    last_name: str = field(init=True)
    level = 1
    money: float = 0
    spells = []
    inventory = []
    gear: 'g.GearSet' = g.GearSet()

    experience = 0
    # Attributes
    strength = 1
    constitution = 1
    intelligence = 1

    # 2 points granted upon leveling up
    attribute_points = 0

    # Base stats
    base_health: int = BASE_STATS["health"]
    base_physical_attack: int = BASE_STATS["physical_attack"]
    base_physical_defense: int = BASE_STATS["physical_defense"]
    base_magic_attack: int = BASE_STATS["magic_attack"]
    base_magic_defense: int = BASE_STATS["magic_defense"]

    # Initialize stats from base stats
    max_health: int = base_health
    physical_attack: int = base_physical_attack
    physical_defense: int = base_physical_defense
    magic_attack: int = base_magic_attack
    magic_defense: int = base_magic_defense

    # An extra bit to track current stats vs max / normal
    current_health: int = max_health
    current_physical_attack: int = physical_attack
    current_physical_defense: int = physical_defense
    current_magic_attack: int = magic_attack
    current_magic_defense: int = magic_defense


    def __repr__(self):
        return f"""
        {(self.first_name.capitalize() 
        + " "
        + self.last_name.capitalize()).strip()}: Level {self.level}
        {self.gear}
        Abilities: {self.spells}
        Health: {self.current_health}/{self.max_health}
        Current Physical Attack: {self.current_physical_attack}
        Current Physical Defense: {self.current_physical_defense}
        Current Magic Attack: {self.current_magic_attack}
        Current Magic Defense: {self.current_magic_defense}
        """


class Character:
    """
    Base class for all archetypes
    """
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

    def level_up(self):
        # exp requirement per level
        required_exp = round(1000 / (1 + np.e ** (-.1 * (self.data.level - 50))))
        if self.data.experience >= required_exp:
            self.data.level += 1
            self.data.attribute_points += 2
            self.data.experience -= required_exp

    # combat utils
    def take_damage(self, damage):
        self.data.current_health -= round(damage)
        if self.data.current_health < 0:
            self.data.current_health = 0

    def recover_health(self, amount):
        self.data.current_health += round(amount)
        if self.data.current_health >= self.data.max_health:
            self.data.current_health = self.data.max_health



    # dunders
    def __repr__(self):
        return str(self.data)
