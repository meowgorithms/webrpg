"""
Provides character archetypes (aka classes)
"""
from engine.gear import *
from app import db
from engine.queries import *

class Archetype:
    """
    Base class for all archetypes
    """

    # TODO
    def __init__(self, name: str, archetype_name: str):
        self.name = name
        self.archetype_name = archetype_name
        self.abilities = set()
        self.gear = GearSet
        self.level = 1

        base_stats = get_base_stats(self.archetype_name)
        self.base_health = base_stats[1]
        self.base_physical_attack = base_stats[2]
        self.base_physical_defense = base_stats[3]
        self.base_magic_attack = base_stats[4]
        self.base_magic_defense = base_stats[5]
    
    def __repr__(self):
        return f"Name: {self.name}, \
             Gear: {self.gear}, \
             Archetype: {self.archetype_name}, \
             Abilities: {self.abilities}, \
             Base Health: {self.base_health}, \
             Base Physical Attack: {self.base_physical_attack}, \
             Base Physical Defense: {self.base_physical_defense}, \
             Base Magic Attack: {self.base_magic_attack}, \
             Base Magic Defense: {self.base_magic_defense}"


class Quantum(Archetype):
    """
    Archetype themed around quantum behavior
    """

    # TODO
    def __init__(self, name: str):
        super().__init__(name, "Quantum")
        
        

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