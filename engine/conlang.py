import lemminflect as lem
import spacy
from random import choice, randint

# There needs to be more rules for this to be how I imagine it, but this
# is a pretty good start

# Common consonants
CONSONANTS = ['s', 'z', 'v', 'l', 'k', 't', 'r', 'sh', 'zh', 'th', 'y', 'n']

VOWELS = ['a', 'i', 'u', 'e', 'o', 'ei']

STOPS = ['s', 'l', 'k', 't', 'v', 'sh', 'n']

# These are allowed as starts of the second syllable
POST_STOPS = ['r', 's', 'k', 'n', 'v', 'z']

SYLLABLE_DICT = {
    "C": CONSONANTS,
    "V": VOWELS,
    "S": STOPS,
    "P": POST_STOPS
}

# Define conlang word/syllable structure
SYLLABLE_STRUCTURES = [
    "CVS",
    "VS",
    "CV"
]

MAX_SYLLABLES = 3 # per word

def create_conlang_word(length: int = MAX_SYLLABLES, rand: bool = True):
    if rand:
        length = randint(1, MAX_SYLLABLES)
    word = ""
    prev_syl = ""
    prev_form = ""
    for _ in range(length):
        form = choice(SYLLABLE_STRUCTURES)

        if form[-1] == "V" and prev_syl == "V":
            while form[-1] == "V" and prev_syl == "V":
                form = choice(SYLLABLE_STRUCTURES)

        if prev_form == form:
            while prev_form == form:
                form = choice(SYLLABLE_STRUCTURES)

        for syl in form:
            if prev_syl == "S" and syl == "C":
                syl = "P"
            candidate = choice(SYLLABLE_DICT[syl])
            if word:
                if candidate == word[-1]:
                    while candidate == word[-1]:
                        candidate = choice(SYLLABLE_DICT[syl])
            word += candidate
            prev_syl = syl

        prev_form = form
    
    completed_word = ""
    # for i in range(0, len(word) - 1):
    #     if word[i] != word[i + 1]:
    #         completed_word += word[i]
    return word