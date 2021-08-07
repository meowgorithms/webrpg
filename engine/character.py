"""
Provides character archetypes (aka classes)
"""
from .gear import GearSet
from .spells import Spell, Spells
from dataclasses import dataclass, field


BASE_STATS = {
    "health": 100,
    "physical_attack": 5,
    "physical_defense": 5,
    "magic_attack": 5,
    "magic_defense": 5,
}


@dataclass(init=True)
class CharacterData:
    """
    Data container for archetypes
    """
    name: str = field(init=True)
    level = 1
    spells: list[Spell] = []
    gear: GearSet = GearSet()

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
        {self.name}: Level {self.level}
        {self.gear}
        Abilities: {self.abilities}
        Base Health: {self.base_health}
        Base Physical Attack: {self.base_physical_attack}
        Base Physical Defense: {self.base_physical_defense}
        Base Magic Attack: {self.base_magic_attack}
        Base Magic Defense: {self.base_magic_defense}
        Max Health: {self.max_health}
        Physical Attack: {self.physical_attack}
        Physical Defense: {self.physical_defense}
        Magic Attack: {self.magic_attack}
        Magic Defense: {self.magic_defense}
        Current Health: {self.current_health}
        Current Physical Attack: {self.current_physical_attack}
        Current Physical Defense: {self.current_physical_defense}
        Current Magic Attack: {self.current_magic_attack}
        Current Magic Defense: {self.current_magic_defense}
        """


class Character:
    """
    Base class for all archetypes
    """
    def __init__(self, name: str):
        self.data = CharacterData(name)

    def take_damage(self, damage):
        self.data.current_health -= round(damage)
        if self.data.current_health < 0:
            self.data.current_health = 0

    def recover_health(self, amount):
        self.data.current_health += round(amount)
        if self.data.current_health >= self.data.max_health:
            self.data.current_health = self.data.max_health

    def __repr__(self):
        return str(self.data)

    def learn_spell(self, spell: Spell):
        self.data.spells.append(spell)
