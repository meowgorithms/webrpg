"""
Provides procedural generation for names
"""
from random import choice

def read_from_file(filepath):
    with open(filepath, 'r') as file:
        words = file.read()
        words = words.replace("\n", " ")
    return words.split()

SPELL_FORMATS = [
    "N N",
    "PADJ N",
    "NADJ N",
    "ADJ N",
    "VBG N"
]

WEAPON_FORMATS = [
    "PADJ N",
    "NADJ N",
    "PADJ N of VBG",
    "NADJ N of VBG",
    "N of VBG",
    "VBG N",
    "VBG N of VBG"
]

def create_spell_name(name_format: str = choice(SPELL_FORMATS)):
    if name_format == "N N":
        nouns = read_from_file("spell_words.txt")
        first = choice(nouns)
        second = choice(nouns)
        if second == first:
            while second == first:
                second = choice(nouns)
        return f"{first.capitalize()} {second.capitalize()}"
    elif name_format == "PADJ N":
        adjectives = read_from_file("positive_adjectives.txt")
        nouns = read_from_file("spell_words.txt")
        first = choice(adjectives)
        second = choice(nouns)
        return f"{first.capitalize()} {second.capitalize()}"
    elif name_format == "NADJ N":
        adjectives = read_from_file("negative_adjectives.txt")
        nouns = read_from_file("spell_words.txt")
        first = choice(adjectives)
        second = choice(nouns)
        return f"{first.capitalize()} {second.capitalize()}"
    elif name_format == "ADJ N":
        adjectives = read_from_file("all_adj.txt")
        nouns = read_from_file("spell_words.txt")
        first = choice(adjectives)
        second = choice(nouns)
        return f"{first.capitalize()} {second.capitalize()}"
    elif name_format == "VBG N":
        gerunds = read_from_file("gerunds.txt")
        nouns = read_from_file("spell_words.txt")
        first = choice(gerunds)
        second = choice(nouns)
        return f"{first.capitalize()} {second.capitalize()}"


def create_weapon_name(name_format: str = choice(WEAPON_FORMATS)):
    if name_format == "PADJ N":
        adjectives = read_from_file("positive_adjectives.txt")
        nouns = read_from_file("weapon_nouns.txt")
        first = choice(adjectives).capitalize()
        second = choice(nouns).capitalize()
        return f"{first} {second}"
    elif name_format == "NADJ N":
        adjectives = read_from_file("negative_adjectives.txt")
        nouns = read_from_file("weapon_nouns.txt")
        first = choice(adjectives).capitalize()
        second = choice(nouns).capitalize()
        return f"{first} {second}"
    elif name_format == "PADJ N of VBG":
        adjectives = read_from_file("positive_adjectives.txt")
        nouns = read_from_file("weapon_nouns.txt")
        gerunds = read_from_file("gerunds.txt")
        first = choice(adjectives).capitalize()
        second = choice(nouns).capitalize()
        third = choice(gerunds).capitalize()
        return f"{first} {second} of {third}"
    elif name_format == "NADJ N of VBG":
        adjectives = read_from_file("negative_adjectives.txt")
        nouns = read_from_file("weapon_nouns.txt")
        gerunds = read_from_file("gerunds.txt")
        first = choice(adjectives).capitalize()
        second = choice(nouns).capitalize()
        third = choice(gerunds).capitalize()
        return f"{first} {second} of {third}"
    elif name_format == "N of VBG":
        nouns = read_from_file("weapon_nouns.txt")
        gerunds = read_from_file("gerunds.txt")
        first = choice(nouns).capitalize()
        second = choice(gerunds).capitalize()
        return f"{first} of {second}"
    elif name_format == "VBG N":
        nouns = read_from_file("weapon_nouns.txt")
        gerunds = read_from_file("gerunds.txt")
        first = choice(gerunds).capitalize()
        second = choice(nouns).capitalize()
        return f"{first} of {second}"
    elif name_format == "VBG N of VBG":
        nouns = read_from_file("weapon_nouns.txt")
        gerunds = read_from_file("gerunds.txt")
        first = choice(gerunds).capitalize()
        third = choice(gerunds).capitalize()
        second = choice(nouns).capitalize()
        if third == first:
            while third == first:
                third = choice(gerunds).capitalize()
        return f"{first} {second} of {third}"

