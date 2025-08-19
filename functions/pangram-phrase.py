# a pangram is a phrase that uses every
# letter of the alphabet at least once.

import re


def pangram(phrase):
    letters = re.sub('[^a-zA-Z]', '', phrase)
    letter_set = set(letters.lower())
    if len(letter_set) == 26:
        return True
    else:
        return False


string1 = 'Zippy hackers quickly debug JavaScript fixing vexing bugs while exploring new tech trends'
string2 = 'Jumpy wizard vexed Brock’s quaint flying toad, blazing hex over nymphs with quick zeal'
print(pangram(string1))
print(pangram(string2))
