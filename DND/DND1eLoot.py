"""
This script/program/whatever is a personal tool to generate loot using
the 1e/AD&D Loot tables.

The tables within the book (Dungeon Masters Guide for Advanced Dungeons
and Dragons by Gary Gygax) have their own weightings to them that I will try to replicate.

Sections taken directly from the book:
I. Map or Magic
II. Map Table
    .A Monetary Treasure
    .B Magic Treasure
    .C Combined Hoard
III. Magic Items
    .A Potions
    .B Scrolls
    .C Rings
    .D Rods, Staves, and Wands
    .E Miscellaneous Magic (Split into five parts and one special part by the book because of
    how many items there are)
    .F Armor and Shield
    .G Swords
    .H Miscellaneous Weapons
"""

import random 

#Book says 01-10 for Map, 11-100 for magic

options = ['Map', 'Magic']
result = random.choices(options, weights=[1,9])
result = result[0]

if result == 'Map':
    options = ['False Map', 'Map to Monetary Treasure', 'Map to Magic Treasure', 'Map to Combined Horde']
    result = random.choices(options, weights=[5,65,20,10])
    result = result[0]
    print(result)
else:
    options = ['Potions', 'Scrolls', 'Rings', 'Rods', 'Misc.1', 'Misc.2',
    'Misc.3', 'Misc.4', 'Misc.5', 'Armor', 'Swords', 'Misc. Weapons']
    result = random.choices(options, weights=[20,15,5,5,3,3,3,3,3,15,11,14])
    result = result[0]
    print(result + ":")

match result:
    case 'Potions':
        options = ['Animal Control', 'Clairaudience', 'Clairvoyance', 'Climbing', 'Delusion', 
        'Diminution', 'Dragon Control', 'ESP', 'Extra-Healing', 'Fire Resistance', 'Flying',
        'Gaseous Form', 'Giant Control', 'Giant Strength', 'Growth', 'Healing', 'Heroism',
        'Human Control', 'Invisibility', 'Invulnerability', 'Levitation', 'Longevity',
        'Oil of Etherealness', 'Oil of Slipperiness', 'Philter of Love', 'Philter of Persuasiveness',
        'Plant Control', 'Polymorph', 'Poison', 'Speed', 'Super-Heroism', 'Sweet Water',
        'Treasure Finding', 'Undead Control', 'Water Breathing']
        result = random.choices(options, weights=[3,3,3,3,3,3,2,3,3,3,3,2,2,3,2,6,2,2,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,1,3])
        result = result[0]
        print(result)
    
    case 'Scrolls':
        #options = ['']
        #result = random.choices(options, weights=[])
        #result = result[0]
        #print(result)
        print('Use DND1eScrolls.py to generate scrolls')
    
    case 'Rings':
        options = ['Contrariness', 'Delusion', 'Djinni Summoning', 'Elemental Command',
        'Feather Falling', 'Fire Resistance', 'Free Action', 'Human Influence', 'Invisibility',
        'Mammal Control', 'Multiple Wishes', 'Protection', 'Regeneration', 'Shooting Stars',
        'Spell Storing', 'Spell Turning', 'Swimming', 'Telekinesis', 'Three Wishes', 'Warmth',
        'Water Walking', 'Weakness', 'Wizardry', 'X-Ray Vision']
        result = random.choices(options, weights=[6,6,2,1,6,6,3,3,7,3,1,16,1,2,2,4,6,2,2,6,5,8,1,1])
        result = result[0]
        print(result)
    
    case 'Rods':
        options = ['Rod of Absorption', 'Rod of Beguiling', 'Rod of Cancellation',
        'Rod of Lordly Might', 'Rod of Resurrection', 'Rod of Rulership', 'Rod of Smithing',
        'Staff of Command', 'Staff of Curing', 'Staff of the Magi', 'Staff of Power',
        'Staff of the Serpent', 'Staff of Striking', 'Staff of Withering', 'Wand of Conjuration',
        'Wand of Enemy Detection', 'Wand of Fear', 'Wand of Fire', 'Wand of Frost',
        'Wand of Illumination', 'Wand of Illusion', 'Wand of Lightning', 'Wand of Magic Detection',
        'Wand of Metal & Mineral Detection', 'Wand of Magic Missiles', 'Wand of Negation',
        'Wand of Paralyzation', 'Wand of Polymorphing', 'Wand of Secret Door & Trap Location',
        'Wand of Wonder']
        result = random.choices(options, weights=[3,1,10,2,1,1,1,1,2,1,1,3,4,2,1,4,3,3,3,5,4,3,9,5,5,8,3,3,2,6])
        result = result[0]
        print(result)
    
    case 'Misc.1':
        options = ['Alchemy Jug', 'Amulet of Inescapable Location', 'Amulet of Life Protection',
        'Amulet of the Planes', 'Amulet of Proof Against Detection and Location', 'Apparatus of Kwalish',
        'Arrow of Direction', 'Artifact or Relic', 'Bag of Beans', 'Bag of Devouring', 'Bag of Holding', 
        'Bag of Transmuting', 'Bag of Tricks', 'Beaker of Plentiful Potions', 'Boat, Folding', 'Book of Exalted Deeds',
        'Book of Infinite Spells', 'Book of Vile Darkness', 'Boots of Dancing', 'Boots of Elvenkind', 'Boots of Levitation',
        'Boots of Speed', 'Boots of Striding and Springing', 'Bowl Commanding Water Elementals',
        'Bowl of Watery Death', 'Bracers of Defense', 'Bracers of Defenselessness', 'Brazier Commanding Fire Elementals',
        'Brazier of Sleep Smoke', 'Brooch of Shielding', 'Broom of Animated Attack', 'Broom of Flying', "Bucknard'd Everfull Purse"]
        result = random.choices(options, weights=[2,2,1,2,4,2,3,1,3,1,5,1,2,2,1,1,1,1,1,6,5,4,4,3,1,20,2,3,1,7,1,5,2])
        result = result[0]
        print(result)
    
    case 'Misc.2':
        options = ['Candle of Invocation', 'Carpet of Flying', 'Censer of Controlling Air Elementals',
        'Censer of Summoning Hostile Air Elementals','Chime of Opening', 
        'Chime of Hunger', 'Cloak of Displacement', 'Cloak of Elvenkind', 'Cloak of Manta Ray',
        'Cloak of Poisonousness', 'Cloak of Protection', 'Crystal Ball', 'Crystal Hypnosis Ball', 'Cube of Force',
        'Cube of Frost Resistance', 'Cubic Gate', "Daern's Instant Fortress", 'Decanter of Endless Water', 
        'Deck of Many Things', 'Drums of Deafening', 'Drums of Panic', 'Dust of Appearance', 'Dust of Disappearance',
        'Dust of Sneezing and Chocking', 'Efreeti Bottle', 'Eversmoking Bottle', 'Eyes of Charming', 'Eyes of the Eagle',
        'Eyes of Minute Seeing', 'Eyes of Petrification']
        result = random.choices(options, weights=[6,2,2,1,2,1,4,9,3,2,23,5,1,2,2,2,2,3,4,1,2,6,6,1,1,1,1,2,2,1])
        result = result[0]
        print(result)
    
    case 'Misc.3':
        options = ['Figurine of Wondrous Power', 'Flask of Curses', 'Gauntlets of Dexterity', 'Gauntlets of Fumbling',
        'Gauntlets of Ogre Power', 'Gauntlets of Swimming and Climbing', 'Gem of Brightness', 'Gem of Seeing',
        'Girdle of Femininity/Masculinity', 'Girdle of Giant Strength', 'Helm of Brilliance', 
        'Helm of Comprehending Languages & Reading Magic', 'Helm of Opposite Alignment', 'Helm of Telepathy',
        'Helm of Teleportation', 'Helm of Underwater Action', 'Horn of Blasting', 'Horn of Bubbles', 'Horn of Collapsing',
        'Horn of the Tritons', 'Horn of Valhalla', 'Horseshoes of Speed', 'Horseshoes of the Zephyr', 'Incense of Meditation',
        'Incense of Obsession', 'Ioun Stones', 'Instrument of the Bards', ' Iron Flask', 'Javelin of Lightning',
        'Javelin of Piercing', 'Jewel of Attacks', 'Jewel of Flawlessness', "Keoghtom's Ointment"]        
        result = random.choices(options, weights=[15,1,2,2,2,3,1,1,1,1,1,5,2,2,1,5,1,2,1,4,7,3,2,5,1,1,6,2,5,5,1,1,8])
        result = result[0]
        print(result)
    
    case 'Misc.4':
        options = ['Libram of Gainful Conjuration', 'Libram of Ineffable Damnation', 'Libram of Silver Magic',
        'Lyre of Building', 'Manual of Bodilt Health', 'Manual of Gainful Exercise', 'Manual of Golems',
        'Manual of Puissant Skill at Arms', 'Manual of Quickness of Action', 'Manual of Stealthy Pilfering',
        'Mattock of the Titans', 'Maul of the Titands', 'Medallion of ESP', 'Medallion of Thought Projection',
        'Mirror of Life Trapping', 'Mirror of Mental Prowess', 'Mirror of Opposition', 'Necklace of Adaptation', 
        'Necklace of Missiles', 'Necklace of Prayer Beads', 'Necklace of Strangulation', 
        'Net of Entrapment', 'Net of Snaring', "Nolzur's Marvelous Pigments", 'Pearl of Power', 'Pearl of Wisdom',
        'Periapt of Foul Rotting', 'Peripant of Health', 'Peripant of Proof Against Healing', 'Peripant of Wound Closure',
        'Phylactery of Faithfulness', 'Phylactery of Long Years', 'Phylactery of Monstrous Attention', 'Pipes of the Sewers',
        'Portable Hole', "Quaal's Feather Token"]
        result = random.choices(options, weights=[1,1,1,1,1,1,1,1,1,1,1,1,3,2,1,1,1,3,4,6,2,3,4,2,2,2,2,3,7,4,6,4,2,8,1,15])
        result = result[0]
        print(result)
    
    case 'Misc.5':
        options = ['Robe of the Archmagi', 'Robe of the Blending', 'Robe of Eyes', 'Robe of Powerlessness',
        'Robe of Scintillating Colours', 'Robe of Useful Items', 'Rope of Climbing', 'Rope of Constriction',
        'Rope of Entanglement', 'Rug of Smothering', 'Rug of Welcome', 'Saw of Mighty Cutting', 'Scarab of Death',
        'Scarab of Enraging Enemies', 'Scarab of Insanity', 'Scarab of Protection', 'Spade of Colossal Excavation', 
        'Sphere of Annihilation', 'Stone of Controlling Earth Elementals', 'Stone of Good Luck (Luckstone)', 
        'Stone of Weight (Loadstone)', 'Talisman of Pure Good', 'Talisman of the Sphere', 'Talisman of Ultimate Evil',
        'Talisman of Zagy', 'Tome of Clear Thought', 'Tome of Leadership and Influence', 
        'Tome of Understanding', 'Trident of Fish Command', 'Trident of Submission', 'Trident of Warning', 
        'Trident of Yearning', 'Vacuous Grimoire', 'Well of Many Worlds','Wings of Flying']
        result = random.choices(options, weights=[1,7,1,1,1,8,6,2,4,1,1,1,1,3,2,6,1,1,2,2,2,3,1,2,6,1,1,1,7,2,5,2,2,3,10])
        result = result[0]
        print(result)
    
    case 'Special':
        options = []
        result = random.choices(options, weights=[])
        result = result[0]
        print(result)
    
    case 'Armor':
        options = ['Chain Mail +1', 'Chain Mail +2', 'Chain Mail +3', 'Leather Armor +1', 'Plate Mail +1',
        'Plate Mail +2', 'Plate Mail +3', 'Plate Mail +4', 'Plate Mail +5', 'Plate Mail of Etherealness', 
        'Plate Mail of Vulnerability', 'Ring Mail +1', 'Scale Mail +1', 'Scale Mail +2', 'Splint Mail +1',
        'Splint Mail +2', 'Splint Mail +3', 'Splint Mail +4', 'Studded Armor +1', 'Shield +1', 'Shield +2',
        'Shield +3', 'Shield +4', 'Shield +5', 'Shield, large, +1, +4 vs. missiles', 'Shield -1, missile attractor']
        result = random.choices(options, weights=[5,4,2,8,7,6,3,2,1,1,5,6,5,4,4,3,2,1,6,9,5,4,2,1,1,3])
        result = result[0]
        print(result)
    
    case 'Swords':
        options = ['Sword +1', 'Sword +1, +2 vs. magic-using & enchanted creatures', 'Sword +1, +3 vs. lycanthropes & shape changers',
        'Sword +1, +3 vs. regenerating creatures', 'Sword +1, +4 vs. reptiles', 
        'Sword +1, Flame Tongue:\n  +2 vs. regenerating creatures\n  +3 vs. cold-using, inflammable, or avian creatures\n  +4 vs. undead', #christ almighty
        'Sword +1, Luck Blade', 'Sword +2', 'Sword +2, Giant Slayer', 'Sword +2, Dragon Slayer', 'Sword +2, Nine Lives Stealer', 
        'Sword +3', 'Sword +3, Frost Brand:\n  +6 vs. fire using/dwelling creatures', 'Sword +4', 'Sword +4, Defender',
        'Sword +5', 'Sword +5, Defender', 'Sword +5, Holy Avenger', 'Sword of Dancing', 'Sword of Wounding', 'Sword of Life Stealing',
        'Sword of Sharpness', 'Sword, Vorpal Weapon', 'Sword +1, Cursed', 'Sword -2, Cursed', 'Sword, Cursed Berserking' ]
        result = random.choices(options, weights=[25,5,5,5,5,4,1,8,4,4,1,4,3,2,1,1,1,1,1,1,1,1,1,5,5,5])
        result = result[0]
        print(result)
    
    case 'Misc. Weapons':
        options = ['Arrow +1, 2-24 in number', 'Arrow +2, 2-16 in number', 'Arrow +3, 2-12 in number', 'Arrow of Slaying',
        'Axe +1', 'Axe +2', 'Axe +2, Throwing', 'Axe +3', 'Battle Axe +1', 'Bolt +2, 2-20 in number', 'Bow +1', 
        'Crossbow of Accuracy, +3', 'Crossbow of Distance', 'Crossbow of Speed', 'Dagger +1, +2 vs. creatures smaller than man-sized',
        'Dagger +2, +3 vs. creatures larger than man-sized', 'Dagger of Venom', 'Flail +1', 'Hammer +2', 'Hammer +3',
        'Hammer +3, Dwarven Thrower', 'Hammer of Thunderbolts', 'Javelin +2', 'Mace +1', 'Mace +2', 'Mace of Disruption',
        'Mace +4', 'Military Pick +1', 'Morning Star +1', 'Scimitar +2', 'Sling of Seeking +2', 'Spear +1', 'Spear +2',
        'Spear +3', 'Spear, Cursed Backbiter', 'Trident (Military Fork) +3']
        result = random.choices(options, weights=[8,4,2,1,5,2,1,1,3,5,3,1,1,1,8,4,1,5,4,2,1,1,3,5,3,1,1,3,3,5,1,5,2,1,2,1])
        result = result[0]
        print(result)

