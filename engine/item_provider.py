from typing import TYPE_CHECKING
from . import elements, conlang, spells
from .gear import GearItem, GearItemData, Armor, Weapon, SpecialItem
from random import choice, random, uniform, randint, choices

if TYPE_CHECKING:
    from . import character
# item stats depend on item level and attribute requirements

# item level depends on dropper's level and stats, or character's level and
# stats if being purchased from the store -> this points to a generator object
# which will allow this sort of abstraction

# item attribute requirement intensity depends on item level

class ItemProvider:
    """
    Creates random items with requirements and stats appropriate to the context,
    i.e. if the context is the market, the player character should be passed
    if the context is a battle, the loser should be passed.
    """
    item_types = [
        Armor,
        Weapon,
        SpecialItem,
        # TODO? spells.SpellBook,
    ]

    rarities = {
        "common": 60,
        "uncommon": 20,
        "rare": 15,
        "unique": 4,
        "legendary": 1,
    }

    def __init__(self, entity: 'character.Character'):
        # get entity data
        self.data = entity.data

    def generate_items(self, n: int) -> 'list[GearItem]':
        """
        Generates a list of n items
        ### Parameters
        n: int
            number of items to generate
        ### Returns
        a list of equippable items with (hopefully/mostly) fair stats compared
        to the provided entity
        """
        items = []
        for _ in range(n):
            item = choice(self.item_types)()
            self.__give_rarity__(item)
            self.__give_requirements__(item)
            self.__give_stats__(item)
            items.append(item)
        return items

    def __give_rarity__(self,
                        item: 'GearItem',
                        weights: 'list[int]' = None):
        if weights == None:
            weights = list(self.rarities.values())
        item.data.rarity = choices(list(self.rarities.keys()), weights=weights)[0]

    def __give_requirements__(self, item: GearItem, level_range: int = 3):
        level_req = self.__level_requirement__(item, level_range)
        self.__attribute_requirements__(item, level_req)

    def __level_requirement__(self, item: 'GearItem', level_range: int):
        level_mod = {
            "common": -2,
            "uncommon": 0,
            "rare": 1,
            "unique": 3,
            "legendary": 5
        }
        lower = self.data.level - level_range
        upper = self.data.level + level_range
        level_req = randint(lower, upper) + level_mod[item.data.rarity]
        if level_req < 1:
            level_req = 1
        item.data.requirements["level"] = level_req
        return level_req

    def __attribute_requirements__(self,
                                   item: 'GearItem',
                                   level_requirement: int):
        """
        Uses level requirement, entity's provided attributes and item element to
        produce attribute requirements.
        """
        n_reqs_from_rarity = {
            "common": 0,
            "uncommon": 0,
            "rare": 1,
            "unique": 2,
            "legendary": 3
        }
        attributes = list(self.data.attributes.keys())
        n_reqs = n_reqs_from_rarity[item.data.rarity]
        if item.data.element != elements.Element.NONE:
            if n_reqs >= 1:
                req = item.data.element.name
                val = randint(level_requirement, level_requirement * 2)
                n_reqs -= 1
                item.data.requirements[req] = val

        for _ in range(n_reqs):
            req = choice(attributes)
            val = randint(level_requirement, level_requirement * 2)
            item.data.requirements[req] = val

    def __give_stats__(self, item: 'GearItem'):
        n_stats_from_rarity = {
            "common": 1,
            "uncommon": 2,
            "rare": 3,
            "unique": 4,
            "legendary": 5
        }
        stats = list(self.data.attributes.keys())
        NONE_stats = [
            "max_health",
            "physical_attack",
            "physical_defense",
            "magic_attack",
            "magic_defense",
            "strength",
            "constitution",
            "intelligence"
        ]
        stats.extend([
            "max_health",
            "physical_attack",
            "physical_defense",
            "magic_attack",
            "magic_defense",
        ])
        stat_multipiers = {
            "max_health": 10,
            "physical_attack": 5,
            "physical_defense": 5,
            "magic_attack": 5,
            "magic_defense": 5,
            "strength": .33,
            "constitution": .33,
            "intelligence": .33,
            "light": .5,
            "dark": .5,
            "electric": .5,
            "fire": .5,
            "water": .5,
            "earth": .5,
            "air": .5,
            "metal": .5,
            "acid": .5,
            "psychic": .5,
            "weird": .5
        }
        rarity_multipliers = {
            "common": 1,
            "uncommon": 1.1,
            "rare": 1.2,
            "unique": 1.4,
            "legendary": 1.8
        }
        
        # TODO Guarantee element stat from item
        for i in range(n_stats_from_rarity[item.data.rarity]):
            rand_upper = max(1, round((item.data.requirements["level"] * random())))
            if i == 0:
                if item.data.element != item.data.element.NONE:
                    stat = item.data.element.name.lower()
                else:
                    stat = choice(NONE_stats)
            else:
                stat = choice(stats)

            val = stat_multipiers[stat] \
                * rarity_multipliers[item.data.rarity] \
                * item.data.requirements["level"] \
                + randint(1, rand_upper)
            item.data.stats[stat] = round(val)
