"""
Provides procedural generation for names
"""
from random import choice,  choices
from . import elements as el

# TODO
# Words are currently very crude,
# consider more filtering and potentially
# some word2vec math to tune into the right words

# Get root words and (lemm)inflect to ensure correctness

def read_from_file(filepath):
    with open(filepath, 'r') as file:
        words = file.read()
        words = words.replace("\n", " ")
    return words.split()

SPELL_FORMATS = [
    "E SN SN",
    "PADJ E SN",
    "NADJ E SN",
    "ADJ E SN",
    "E VBG SN"
]

ARMOR_FORMATS = [
    "E AN",
    "ADJ E AN",
    "PADJ E AN",
    "NADJ E AN",
    "E AN of TN",
    "E VBG AN",
]

WEAPON_FORMATS = [
    "PADJ E WN",
    "NADJ E WN",
    "PADJ E WN of TN",
    "NADJ E WN of TN",
    "E WN of TN",
    "E VBG WN",
    "E VBG WN of TN",
    "E WN",
    "ADJ E WN",
    "E N WN",
    "E WN of VBG",
    "E VBG WN",
    "ADJ E N"
]

SPECIAL_ITEM_FORMATS = [
    "E N",
    "E TN N",
    "E VBG N",
    "E N of TN",
    "The E N",
    "The E N of TN",
    "The E VBG",
    "The E TN",
    "E N N",
    "NADJ E N",
    "PADJ E N",
    "ADJ E N",
    "ADJ E N of TN",
    "ADJ E TN",
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
    "VB": "words/verbs.txt",
}


def create_name(name_formats: 'list[str]', element_word: str=""):
    name = choice(name_formats).split()
    if element_word == "":
        if "E" in name:
            name.remove("E")
    for i, pos in enumerate(name):
        if pos in POS_DICT:
            name[i] = choice(read_from_file(POS_DICT[pos])).capitalize()
            if name[i] in name[:i]:
                while name[i] in name[:i]:
                    name[i] = choice(read_from_file(POS_DICT[pos])).capitalize()
        # TODO Fix inflections here
        if pos == "E":
            name[i] = element_word.capitalize()
    return " ".join(name).strip()
