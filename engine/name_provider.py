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
    "SN SN",
    "PADJ SN",
    "NADJ SN",
    "ADJ SN",
    "VBG SN"
]

ARMOR_FORMATS = [
    "AN",
    "ADJ AN",
    "PADJ AN",
    "NADJ AN",
    "AN of TN",
    "VBG AN",
]

WEAPON_FORMATS = [
    "PADJ WN",
    "NADJ WN",
    "PADJ WN of TN",
    "NADJ WN of TN",
    "WN of TN",
    "VBG WN",
    "VBG WN of TN",
    "WN",
    "ADJ WN",
    "N WN",
    "WN of VBG",
    "VBG WN",
    "ADJ N"
]

SPECIAL_ITEM_FORMATS = [
    "N",
    "TN N",
    "VBG N",
    "N of TN",
    "The N",
    "The N of TN",
    "The VBG",
    "The TN",
    "N N",
    "NADJ N",
    "PADJ N",
    "ADJ N",
    "ADJ N of TN",
    "ADJ TN",
]

POS_DICT = {
    "N": "words/nouns.txt",
    "ADJ": "words/all_adj.txt",
    "PADJ": "words/positive_adjectives.txt",
    "NADJ": "words/negative_adjectives.txt",
    "TN": "words/tion_nouns.txt",
    "VBG": "words/gerunds.txt",
    "AN": "words/armor_nouns.txt",
    "SN": "words/spell_words.txt",
    "WN": "words/weapon_nouns.txt",
    "VB": "words/verbs.txt"
}


def create_name(name_formats: 'list[str]'):
    name_format = choice(name_formats)
    name = name_format.split()
    for i, pos in enumerate(name):
        if pos != 'of':
            name[i] = choice(read_from_file(POS_DICT[pos]))
            if name[i] in name[:i]:
                while name[i] in name[:i]:
                    name[i] = choice(read_from_file(POS_DICT[pos]))
    return " ".join(name)
