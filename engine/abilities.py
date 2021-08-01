"""
Provides ability class definitions and helper functions
"""
# Should this be coded into the archetypes?

# This will future proof my lack of executive function
# IF I choose to let archetypes share abilities, this will allow for that freedom
class Ability:
    """
    Base class for all abilities
    """
    def __init__(self, name):
        self.name = name
        