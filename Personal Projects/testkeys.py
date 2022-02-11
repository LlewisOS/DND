import random

options = { 
    '1 Spell': ['1-4', '1-6', '2-9 or 2-7'], 
    '2 Spells': ['1-4', '1-8 or 1-6'],
    '3 Spells': ['1-4', '2-9 or 2-7'],
    '4 Spells': ['1-6', '1-8 or 1-6'],
    '5 Spells': ['1-6', '1-8 or 1-6'],
    '6 Spells': ['1-6', '3-8 or 3-6'],
    '7 Spells': ['1-8', '2-9', '4-9 or 4-7']
    }

KeyIndex = ['1 Spell','2 Spells','3 Spells','4 Spells','5 Spells','6 Spells','7 Spells']
KeyIndex = random.choices(KeyIndex, weights=[19,8,8,7,7,5,6])

KeyIndex = KeyIndex[0]
print(KeyIndex)
options = options[KeyIndex]
print(options)
"""This block finds the Key within the options dictionary.
Then it prints out the name of the key, and then all values within"""


if KeyIndex == '1 Spell':
    SpellLevelRange = random.choices(options, weights=[10,6,3])
    print(SpellLevelRange)
    pass

elif KeyIndex == '2 Spells':
    SpellLevelRange = random.choices(options, weights=[5,3])
    print(SpellLevelRange)
    pass

elif KeyIndex == '3 Spells':
    SpellLevelRange = random.choices(options, weights=[5,3])
    print(SpellLevelRange)
    pass

elif KeyIndex == '4 Spells':
    SpellLevelRange = random.choices(options, weights=[4,3])
    print(SpellLevelRange)
    pass

elif KeyIndex == '5 Spells':
    SpellLevelRange = random.choices(options, weights=[4,3])
    print(SpellLevelRange)
    pass

elif KeyIndex == '6 Spells':
    SpellLevelRange = random.choices(options, weights=[3,2])
    print(SpellLevelRange)
    pass

elif KeyIndex == '7 Spells':
    SpellLevelRange = random.choices(options, weights=[3,2,1])
    print(SpellLevelRange)
    pass
