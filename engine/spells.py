from . import elements as el
from abc import abstractmethod
from dataclasses import dataclass
from enum import Enum, auto
from random import uniform, choice
from .name_provider import SPELL_FORMATS, create_name


class Spell:
    def __init__(self, user):
        self.name = create_name(SPELL_FORMATS)
        self.level = 1
        self.user = user

    def __repr__(self):
        return f"{self.name}: Level {self.level}"
