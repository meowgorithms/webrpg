"""
Provides character archetypes (aka classes)
"""
from .gear import ArcaneSet, GearSet, QuantumGearSet
from .queries import get_base_stats
from .abilities import Ability, Collapse, Disintegrate, Tunnel


class Archetype:
    """
    Base class for all archetypes
    """

    # TODO
    def __init__(self, name: str, archetype_name: str):
        # Define attributes
        self.name = name
        self.archetype_name = archetype_name
        self.abilities = {}
        self.gear = None
        self.level = 1

        # Define base stats
        base_stats = get_base_stats(self.archetype_name)
        self.base_health = base_stats[1]
        self.base_physical_attack = base_stats[2]
        self.base_physical_defense = base_stats[3]
        self.base_magic_attack = base_stats[4]
        self.base_magic_defense = base_stats[5]

        # Initialize stats from base stats
        self.max_health = base_stats[1]
        self.physical_attack = base_stats[2]
        self.physical_defense = base_stats[3]
        self.magic_attack = base_stats[4]
        self.magic_defense = base_stats[5]

        # An extra bit to track current stats vs max / normal
        self.current_health = base_stats[1]
        self.current_physical_attack = base_stats[2]
        self.current_physical_defense = base_stats[3]
        self.current_magic_attack = base_stats[4]
        self.current_magic_defense = base_stats[5]

    def take_damage(self, damage):
        self.current_health -= round(damage)
        if self.current_health < 0:
            self.current_health = 0

    def recover_health(self, amount):
        self.current_health += round(amount)
        if self.current_health >= self.max_health:
            self.current_health = self.max_health

    def __repr__(self):
        return f"""
        {self.name}: Level {self.level}
        {self.gear}
        Archetype: {self.archetype_name}
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

    def add_ability(self, ability: Ability):
        self.abilities[ability.name] = ability


class Quantum(Archetype):
    """
    Archetype themed around quantum behavior
    """

    # TODO
    def __init__(self, name: str):
        super().__init__(name, "Quantum")
        self.gear = QuantumGearSet()

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