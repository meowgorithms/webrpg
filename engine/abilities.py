"""
Provides ability class definitions, damage types, and other related helper
classes and functions
"""
from abc import abstractmethod
from dataclasses import dataclass
from enum import Enum, auto
from random import uniform, choice


class DamageType(Enum):
    """
    Provides damage types
    This class can be extended/refactored later to provide more specific damage
    types
    """
    PHYSICAL = auto()
    MAGIC = auto()


# This will future proof my lack of executive function
# IF I choose to let archetypes share abilities, this will allow for that freedom
class Ability:
    """
    Base class for all abilities
    """

    def __init__(self, name, user):
        self.name = name
        self.level = 1
        # ------ Currently weird
        self.magic_penetration = 0
        self.physical_penetration = 0
        # ------
        self.user = user
        self.archetype_bonus = False
        self.max_level = 10

    @abstractmethod
    def use_ability(self):
        pass

    @abstractmethod
    def __call__(self):
        return self.use_ability

    def __repr__(self):
        return f"{self.name}: Level {self.level}"


# Quantum
# -------
class Tunnel(Ability):
    """
    An ability primarily belonging to the Quantum Archetype
    Penetrates enemy's magic defense, dealing extra damage
    """
    # TODO: Add hard coded values to database, query here for them instead -
    # allows for easy balance changes
    def __init__(self, user):
        super().__init__("Tunnel", user)

        # TODO Query for stats from database
        self.damage_type = DamageType.MAGIC
        self.base_attack = 15
        # ability level and archetype determine amount of penetration
        self.magic_penetration = 10 + self.level * 2

        # Check user archetype and set bonus flag
        if user.data.name == "Quantum":
            self.archetype_bonus = True


    def use_ability(self, target):
        # Check archetype bonus flag
        if self.archetype_bonus:
            self.magic_penetration *= 2

        # calculate scaled ability damage
        damage = (self.base_attack + self.user.data.current_magic_attack) \
            * (self.user.level + self.level)
        # calculate damage received
        damage = damage * (damage / (damage + target.data.current_magic_defense))
        damage = round(damage)
        target.take_damage(damage)
        print(f"{self.user.data.name} dealt {damage} damage to {target.data.name}!")

    def __call__(self, target):
        return self.use_ability(target)


class Collapse(Ability):
    """
    Deals a random amount of damage with a random damage type
    """

    def __init__(self, user):
        super().__init__("Collapse", user)
        # TODO Query DB for stats

        self.base_attack = 10
        self.damage_bonus = self.user.data.magic_attack * 1.75
        # Check user archetype and set bonus flag
        if user.data.name == "Quantum":
            self.archetype_bonus = True

        # Used to define the bounds for the random damage modifier
        self.base_random_lower = 10 - self.level
        self.base_random_upper = self.user.data.magic_attack * \
            (self.level + self.user.data.level)

    def use_ability(self, target):
        self.damage_type = choice([damage_type for damage_type in DamageType])
        print(self.damage_type)
        # calculate normal damage amount
        damage = (self.base_attack + self.user.data.magic_attack) * self.level
        # Apply damage bonus
        if self.archetype_bonus:
            damage += self.damage_bonus

        # Do the random damage thing
        damage += uniform(self.base_random_lower, self.base_random_upper)

        # Calculate received damage
        if self.damage_type == DamageType.MAGIC:
            damage = damage * (damage / (damage + target.data.magic_defense))
        elif self.damage_type == DamageType.PHYSICAL:
            damage = damage * (damage / (damage + target.data.physical_defense))
        damage = round(damage)
        target.take_damage(damage)
        print(f"{self.user.data.name} dealt {damage} damage to {target.data.name}!")

    def __call__(self, target):
        return self.use_ability(target)


class Disintegrate(Ability):
    """
    Quantum Ability
    Primes the next attack for double damage
    """
    # TODO FIX USED FLAG SHIT
    def __init__(self, user):
        super().__init__("Disintegrate", user)
        self.damage_type = DamageType.MAGIC
        self.base_attack = 10
        # Check user archetype and set bonus flag
        if user.data.name == "Quantum":
            self.archetype_bonus = True
        self.damage_multiplier = 2
        self.used = False

    def use_ability(self, target):
        damage = (self.base_attack + self.user.data.magic_attack) \
            * (self.user.data.level + self.level)
        # Check archetype bonus
        if self.archetype_bonus:
            self.damage_multiplier += 0.5
        # Apply multiplier after flag check
        if self.used:
            damage *= self.damage_multiplier
        # Calculate received damage
        damage = damage * (damage / (damage + target.data.magic_defense))
        damage = round(damage)
        target.take_damage(damage)
        print(f"{self.user.data.name} dealt {damage} damage to {target.data.name}!")
        # invert flag
        self.used = ~self.used

    def __call__(self, target):
        return self.use_ability(target)


@dataclass(init=True)
class Abilities:
    """
    Container for abilities
    """
    abilities = []
    def add_ability(self, ability: Ability):
        setattr(self, f"{ability.name}", ability)
        self.abilities.append(ability)

    def __repr__(self):
        return f"{[ability for ability in self.abilities]}"
