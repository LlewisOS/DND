"""
This is the script to generate scrolls and their effects. It is divorced from the main script because
it would add too much bulk and make the main script less readable.

Generate the number of spells and level.

1. Generate number of spells per scroll, or select a cursed scroll
2. Determine spell level range randomly
3. Assign the scrolls their spells

much easier said than done. This uses first edition spells.
"""

import random

options = ['ScrollRand', 'ScrollSet', 'Curse']

result = random.choices(options, weights=[30,19,1])
result = result[0]

if result == 'ScrollRand':
    options = { 
    '1 Spell': ['1-4', '1-6', '2-9 or 2-7'], 
    '2 Spells': ['1-4', '1-8 or 1-6'],
    '3 Spells': ['1-4', '2-9 or 2-7'],
    '4 Spells': ['1-6', '1-8 or 1-6'],
    '5 Spells': ['1-6', '1-8 or 1-6'],
    '6 Spells': ['1-6', '3-8 or 3-6'],
    '7 Spells': ['1-8', '2-9', '4-9 or 4-7']}

    
elif result == 'ScrollSet':
    options = ['Protection - Demons', 'Protection - Devils', 'Protection - Elementals', 'Protection - Lycanthropes',
    'Protection - Magic', 'Protection - Petrification', 'Protection - Possession', 'Protection - Undead']
     
    result = random.choices(options, weights=[2,2,6,6,6,5,5,5])
    result = result[0]
    print(result)

else:
    print('You can make your own curse, but here is also a generated one:\n')

    options = [
        'Reader polymorphed to monster of equal level which attacks any creatures nearby',
        'Reader turned to liquid and drains away',
        "Reader and all within 20' radius transported 200 to 1,200 miles in a random direction",
        "Reader and all within 20' radius transported to another planet, plane or continuum",
        'Disease fatal to reader in 2-8 turns unless cured',
        'Explosive Runes',
        'Magic item nearby is "de-magicked"',
        'randomly rolled spell affects reader at 12th level of magic use (Hit the reader with a random 12th level spell)']

    result = random.choices(options, weights=[25,5,10,10,15,15,9,1])
    result = result[0]
    print(result)