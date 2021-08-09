import lemminflect as lem
import spacy
from random import choice, randint, choices


# mostly a reference for all consonants
CONSONANTS = ['s', 'z', 'v', 'l', 'k', 't', 'r', 'sh', 'zh', 'th', 'y', 'n', 'f']
CONSONANT_WEIGHTS = [10, 10, 10, 10, 10, 10, 10, 6, 8, 9, 8, 10, 4]

STARTS = ['s', 'z', 'v', 'l', 'k', 't', 'r', 'zh', 'y', 'n']
START_WEIGHTS = [10, 8, 10, 10, 10, 10, 10, 10, 8, 8]

VOWELS = ['a', 'i', 'u', 'e', 'o', 'ei', 'ai']
VOWEL_WEIGHTS = [10, 7, 7, 10, 10, 7, 5]

# not linguistic stops, just syllable ends
STOPS = ['s', 'l', 'k', 't', 'v', 'sh', 'n']
STOP_WEIGHTS = [10, 10, 10, 10, 10, 8, 10]

PRE_STOPS = ['l', 'r']

# These are allowed as starts of the second syllable
POST_STOPS = ['r', 's', 'k', 'n', 'v', 'z', 'sh', 'zh']
POST_STOP_WEIGHTS = [10, 7, 8, 10, 7, 8, 7, 7]

SIBILANTS = ['sh', 's', 'zh', 'sh', 'z']

PLOSIVES = ['t', 'k', 'r'] # r isn't a plosive but it fits in the same group for
# this conlang


LANG_DICT = {
    "START": (STARTS, START_WEIGHTS),
    "V": (VOWELS, VOWEL_WEIGHTS),
    "S": (STOPS, STOP_WEIGHTS),
    "POST": (POST_STOPS, POST_STOP_WEIGHTS),
    "PRE": (PRE_STOPS, [1, 1]),
    "SIB": SIBILANTS,
    "PLOS": PLOSIVES,
}

MAX_LENGTH = 12

# The key must be followed by one of its values
RULES = {
    "START": ["V"],
    "V": ["S", "START", "PRE"],
    "PRE": ["POST", "S"],
    "S": ["POST", "V"],
    "POST": ["V"],
}

def get_letter(syl: str):
    """
    Helper function for create_conlang_word
    """
    return choices(LANG_DICT[syl][0], LANG_DICT[syl][1], k=1)[0]


def create_conlang_word(length: int = MAX_LENGTH,
                        rand: bool = True,
                        debug: bool = False):
    """
    Generates a word based on rules defined in conlang.py
    """
    if rand:
        length = randint(3, length)

    form = [choice(["START", "V"])]

    while len(form) < length:
        candidate = choice(RULES[form[-1]])
        # ------Extra form rules------
        # End of form 
        if len(form) == length - 1:
            # May not be POST
            while candidate == "POST":
                candidate = choice(RULES[form[-1]])
        form.append(candidate)

    word = []
    for i, syl in enumerate(form):
        candidate = get_letter(syl)

        # AI may only appear at end of word
        if i < len(form):
            while candidate == 'ai':
                candidate = get_letter(syl)

        # must be at end of word rules
        if i == len(form) - 1:
            # S and Z must be SH and ZH
            if candidate == 's':
                candidate = 'sh'
            if candidate == 'z':
                candidate = 'zh'
            # E becomes EI
            if candidate == 'e':
                candidate = 'ei'
            # y can't exist
            while candidate == 'y':
                candidate = get_letter(syl)

        # No successive dupes
        if word:
            while word[-1] == candidate:
                candidate = get_letter(syl)
        word.append(candidate)

    # Apply extra filtering rules
    for i in range(len(word) - 1):
        # sibilants may not be successive, must be followed by plosive
        if word[i + 1] in SIBILANTS and word[i] in SIBILANTS:
            word[i + 1] = choice(LANG_DICT["PLOS"])

    if word[-2] in PRE_STOPS \
    and word[-1] not in SIBILANTS:
        word.pop(-2)

    if word[-2] in VOWELS \
    and word[-1] in VOWELS:
        word.pop()
   
    # Get rid of y's at the end of words. They just..don't vibe right
    # with this conlang
    if word[-1] == "y":
        word.pop(-1)

    if debug == True:
        return f'{"".join(word)}: [{" ".join(form)}]', word
    else:
        return "".join(word)


def count_syllables(word: str):
    pass
