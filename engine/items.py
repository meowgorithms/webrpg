"""
"""
from . import name_provider as namer
from . import elements as el
from random import uniform, choice, randint, randrange
from abc import ABC

class Item(ABC):
    name: str