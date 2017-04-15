# -  human names

OUTPUT_FOLDER = "NPCs"

import random, os

import info as info




# roll between 0-6, split randomly between strength and weaknesses
d4 = [1, 2, 3, 4]
d3 = [1, 2, 3]
Flip = [1, 0]
strweaknum = random.choice(d4) + random.choice(d4) - 2
abilities = True
strengthnum = 0
weaknessnum = 0
# print(strweaknum)
strength = True
weakness = True

while abilities:
    if strweaknum is 0:
        abilities = False
    else:
        strweak = random.choice(Flip)
        if strweak is 1:
            strengthnum +=1
        elif strweak is 0:
            weaknessnum +=1
        strweaknum -=1

# print(strengthnum)
# print(weaknessnum)

possibleability = {'Str', 'Dex', 'Con', 'Wis', 'Int', 'Cha'}
strengths = {'Str', 'Dex', 'Con', 'Wis', 'Int', 'Cha'}

print(possibleability)
print(strengths)

while strength:
    if strengthnum is 0:
        # print('in set strengths')
        # print(strengths)
        strengths -= possibleability
        strength = False
    else:
        possibleability.pop()
        strengthnum -=1

# possibleability -= strengths
# print('strengths')
print(strengths)
# print('remaining possibilities')
# print(possibleability)

weaknesses = {'Str', 'Dex', 'Con', 'Wis', 'Int', 'Cha'} - strengths

# print('weakness possibilities')
# print(weaknesses)
# print('possible abilities')
# print(possibleability)


while weakness:
    if weaknessnum is 0:
        weaknesses -= possibleability
        weakness = False
    else:
        possibleability.pop()
        weaknessnum -=1

# print('weaknesses')
print(weaknesses)

talent = random.choice(info.talent_list)

mannerisms = random.choice(info.mannerisms_list)

interaction = random.choice(info.interaction_list)


bonds = info.bond_list
bond = []
bond.append(random.choice(bonds))

if 10 in bond:
    bonds.remove(10)
    bond.remove(10)
    bond.append(random.choice(bonds))
    bond.append(random.choice(bonds))

flaw = random.choice(info.flaw_list)

appearance = random.choice(info.appearance_list)


order = random.choice(info.alignmentOrderList)
moral = random.choice(info.alignmentMoralList)


roll = random.choice(d3)

if roll is 1:
    if moral is 'Good':
        ideal = random.choice(info.good)
    elif moral is 'Neutral':
        ideal = random.choice(info.neutral)
    elif moral is 'Evil':
        ideal = random.choice(info.evil)
elif roll is 2:
    if order is 'Lawful':
        ideal = random.choice(info.lawful)
    elif order is 'Neutral':
        ideal = random.choice(info.neutral)
    elif order is 'Chaotic':
        ideal = random.choice(info.chaotic)
elif roll is 3:
    ideal = random.choice(info.otherideal)


sexes = ['male', 'female']
sex = random.choice(sexes)

race = random.choice(list(info.racelist.keys()))

Race = info.racelist[race]

if Race.name is not 'Half-Elf':
    Male = Race.M
    Female = Race.F
    Lastname = Race.L
elif Race.name is 'Half-Elf':
    roll = random.choice(Flip)
    if roll is 1:
        Male = info.human.M
        Female = info.human.F
        Lastname = info.human.L
    elif roll is 2:
        Male = info.elf.M
        Female = info.elf.F
        Lastname = info.elf.L

if sex is 'male':
    Fname = random.choice(Male)
else:
    Fname = random.choice(Female)
Lname = random.choice(Lastname)



filename = '{} {}.txt'.format(Fname, Lname)

# file write
file = open(filename, 'w')
# name&sex&race
file.write('{} {} the {}\n'.format(Fname, Lname, Race.name))
file.write('<{}>\n\n'.format(sex))
# occupation/history
file.write('<choose an Occupation and history>\n\n')
# appearance
file.write('Appearance: {}\n\n'.format(appearance))
# abilities
file.write('ABILITIES\n')
file.write('High Ability(ies) \nStrength-powerful, brawny, strong as an ox \nDexterity-lithe, agile, graceful \nConstitution-hardy, hale, healthy \nIntelligence-studious, learned, inquisitive \nWisdom-perceptive, spiritual, insightful \nCharisma-persuasive, forceful, born leader\n\n')
file.write('Strengths= {}\n\n'.format(strengths))
file.write('Low Ability(ies) \nStrength-feeble, scrawny \nDexterity-clumsy, fumbling \nConstitution-sickly, pale \nIntelligence-dim-witted, slow \nWisdom-oblivious, absentminded \nCharisma-dull, boring \n\n')
file.write('Weaknesses= {}\n\n'.format(weaknesses))
# talent
file.write('Talent: {}\n'.format(talent))
# mannerisms
file.write('Mannerisms: {}\n'.format(mannerisms))
# Interaction with others
file.write('Interaction trait: {}\n'.format(interaction))
# useful knowledge
file.write('<DM chooses useful knowledge that character knows>\n\n')
# Ideal
if order is 'Neutral':
    if moral is 'Neutral':
        file.write('ALIGNMENT: True Neutral\n')
else:
    file.write('ALIGNMENT: {} {}\n'.format(order, moral))
file.write('Ideal: {}\n'.format(ideal))
# Bond
file.write('Bond: {}\n'.format(bond))
# Flaw or secret
file.write('Flaw or secret: {}\n'.format(flaw))

file.close()

print('\nFile {} is complete\n'.format(filename))

os.rename(filename, '{}/{}'.format(OUTPUT_FOLDER, filename))
