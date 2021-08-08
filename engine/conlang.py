import lemminflect as lem
import spacy
from random import choice, randint, random

# There needs to be more rules for this to be how I imagine it, but this
# is a pretty good start

# Common consonants
CONSONANTS = ['s', 'z', 'v', 'l', 'k', 't', 'r', 'sh', 'zh', 'th', 'y', 'n', 'f']

STARTS = ['s', 'z', 'v', 'l', 'k', 't', 'r', 'zh', 'y', 'n', 'w']

VOWELS = ['a', 'i', 'u', 'e', 'o', 'ei', 'ai']

STOPS = ['s', 'l', 'k', 't', 'v', 'sh', 'n']

PRE_STOPS = ['l', 'r']

# These are allowed as starts of the second syllable
POST_STOPS = ['r', 's', 'k', 'n', 'v', 'z']

SIBILANTS = ['sh', 's', 'zh', 'sh']

PLOSIVES = ['t', 'k', 'r'] # r isn't a plosive but it fits in the same group for
# this conlang

LANG_DICT = {
    "V": VOWELS,
    "S": STOPS,
    "POST": POST_STOPS,
    "PRE": PRE_STOPS,
    "SIB": SIBILANTS,
    "PLOS": PLOSIVES,
    "START": STARTS
}

MAX_LENGTH = 12

RULES = {
    "START": ["V"],
    "V": ["S", "START", "PRE"],
    "PRE": ["POST", "S"],
    "S": ["POST", "V"],
    "POST": ["V"],
}



def create_conlang_word(length: int = MAX_LENGTH,
                        rand: bool = True,
                        debug: bool = False):
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
        candidate = choice(LANG_DICT[syl])
        # AI may only appear at end of word
        if i < len(form):
            while candidate == 'ai':
                candidate = choice(LANG_DICT[syl])
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
                candidate = choice(LANG_DICT[syl])
        # No successive dupes
        if word:
            while word[-1] == candidate:
                candidate = choice(LANG_DICT[syl])
        word.append(candidate)

    # Apply extra filtering rules
    for i in range(len(word) - 1):
        # sibilants may not be successive, must be followed by plosive
        if word[i + 1] in SIBILANTS and word[i] in SIBILANTS:
            word[i + 1] = choice(LANG_DICT["PLOS"])

    if debug == True:
        return f'{"".join(word)}: [{" ".join(form)}]', word
    else:
        return "".join(word)
