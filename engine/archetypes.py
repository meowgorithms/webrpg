"""
Provides character archetypes (aka classes)
"""
from .gear import ArcaneSet, GearSet, QuantumGearSet
from .queries import get_base_stats
from .abilities import Ability, Collapse, Disintegrate, Tunnel, Abilities
from dataclasses import dataclass, field


@dataclass(init=True)
class ArchetypeData:
    """
    Data container for archetypes
    """
    archetype_name: str = field(init=True)
    name: str = field(init=True)
    abilities: Abilities = Abilities()

    base_health: int = 0
    base_physical_attack: int = 0
    base_physical_defense: int = 0
    base_magic_attack: int = 0
    base_magic_defense: int = 0

    # Initialize stats from base stats
    max_health: int = 0
    physical_attack: int = 0
    physical_defense: int = 0
    magic_attack: int = 0
    magic_defense: int = 0

    # An extra bit to track current stats vs max / normal
    current_health: int = 0
    current_physical_attack: int = 0
    current_physical_defense: int = 0
    current_magic_attack: int = 0
    current_magic_defense: int = 0

    gear: GearSet = None # TODO Build GearSet.Empty
    level = 1

    def __repr__(self):
        return f"""
        {self.name}: Level {self.level}
        Archetype: {self.archetype_name}
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


class Archetype:
    """
    Base class for all archetypes
    """
    def __init__(self, name: str, archetype_name: str):
        self.data = ArchetypeData(archetype_name,
                                  name)
        # Is there a better way to do this?
        base_stats = get_base_stats(archetype_name)

        self.data.base_health = base_stats[1]
        self.data.base_physical_attack = base_stats[2]
        self.data.base_physical_defense = base_stats[3]
        self.data.base_magic_attack = base_stats[4]
        self.data.base_magic_defense = base_stats[5]
        # Initialize stats from base stats
        self.data.max_health = base_stats[1]
        self.data.physical_attack = base_stats[2]
        self.data.physical_defense = base_stats[3]
        self.data.magic_attack = base_stats[4]
        self.data.magic_defense = base_stats[5]
        # An extra bit to track current stats vs max / normal
        self.data.current_health = base_stats[1]
        self.data.current_physical_attack = base_stats[2]
        self.data.current_physical_defense = base_stats[3]
        self.data.current_magic_attack = base_stats[4]
        self.data.current_magic_defense = base_stats[5]

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

    def add_ability(self, ability: Ability):
        return self.data.abilities.add_ability(ability)


class Quantum(Archetype):
    """
    Archetype themed around quantum behavior
    """

    # TODO
    def __init__(self, name: str):
        super().__init__(name, "Quantum")
        self.data.gear = QuantumGearSet()
        self.add_ability(Tunnel(self))
        self.add_ability(Collapse(self))
        self.add_ability(Disintegrate(self))


# These are not MVP
# Does this imply the existence of a normal dragon archetype?
class ArchDragon(Archetype):
    """
    Archetype themed around dragons
    """

    # TODO
    def __init__(self):
        super(self)


class Valence(Archetype):
    """
    Archetype themed around peace or balance or some shit
    """

    # TODO
    def __init__(self):
        super(self)


# THE BANGBROS -> FAILURE SAMURAI BROTHERS
class BangBrosuo(Archetype):
    pass


class BangBrone(Archetype):
    pass
