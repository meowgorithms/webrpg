"""
Provides character archetypes (aka classes)
"""
import gear


class Archetype:
    """
    Base class for all archetypes
    """

    # TODO
    def __init__(self, name):
        self.name = name
        self.abilities = set()


class Quantum(Archetype):
    """
    Archetype themed around quantum behavior
    """

    # TODO
    def __init__(self):
        super(self)


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
