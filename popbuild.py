import json

skip = [
    "Galakis Monument",
    "Visage of the Dark One",
    "Dark Phage Entity",
    "Crystalline Portal",
    "Affection Disseminator Ultracore",
    "Affection Disseminator",
    "Chuhn Trading Hub (Upgraded)",
    "Chuhn Trading Hub",
    "Chuhn Trading Post (Doubled)",
    "Orion Menagerie",
    "Crownspire, Spectral Palace",
    "Lepus C-34 Fluxgate",
    "Lepus C-34 Gateway",
    "Lepus C-34 Hypergate",
    "Lepus Bio-Mech Hypergate",
    "Lepus Bio-Mech Gateway",
    "Lepus Chromatic Gateway",
    "Stryll Bioresearch Bay",
    "Scruuge Growth Vats",
    "Argent Consulate",
    "Argent Sector-Embassy",
    "Lepus Gateway",
    "Supel Microhaven (VT)",
    "Supel Microhaven (T)",
    "Supel Microhaven (VS)",
    "Human Tactical Barracks",
]

artifacts = []
with open("config/artifacts.json", "r") as file:
    artifacts = json.load(file)

volcInfStructs = []
with open("config/structures.json", "r") as file:
    structures = json.load(file)

    for structure in structures:
        if structure['name'] in skip:
            continue

        if 'base' in structure and structure['base'] in skip:
            continue

        if 'p' in structure or 'bp' in structure:
            #print(f"{structure['name']} {structure['size']}")
            volcInfStructs.append(structure)

orderedStructs = []
currentRaw: float = 0
currentBonus = 1.0
infRaw = 0
infBonus = 1.0

size0 = []
for struct in volcInfStructs:
    if struct['size'] == 0:
        size0.append(struct)

for struct in size0:
    volcInfStructs.remove(struct)

while size0.__len__() > 0:
    max = 0
    maxStruct = size0[0]
    for struct in size0:
        
        prod = 0
        if 'p' in struct:
            prod += struct['p']
        if 'bp' in struct:
            prod += currentRaw * float(struct['bp'] / 100.0)

        if prod > max:
            max = prod
            maxStruct = struct
    
    orderedStructs.append(maxStruct)
    currentRaw += maxStruct['p'] if 'p' in maxStruct else 0
    currentBonus *= (1.0 + (maxStruct['bp'] / 100.0)) if 'bp' in maxStruct else 1.0
    
    print(f"{maxStruct['name']} {max}")
    
    base = maxStruct['base'] if 'base' in maxStruct else maxStruct['name']
    toRemove = []
    existing = 0
    for struct in orderedStructs:
        if struct['name'] == base or ('base' in struct and struct['base'] == base):
            existing += 1

    if existing >= maxStruct['limit']:
        for struct in size0:
            if 'base' in struct and struct['base'] == base:
                toRemove.append(struct)
            elif struct['name'] == base:
                toRemove.append(struct)

    for remove in toRemove:
        size0.remove(remove)

totalSpace = 0
space = 57
while totalSpace < space:
    max = 0
    maxStruct = volcInfStructs[0]
    for struct in volcInfStructs:
        if struct['size'] + totalSpace > space:
            continue
        prod = 0
        if 'p' in struct:
            prod += struct['p']
        if 'bp' in struct:
            prod += currentRaw * float(struct['bp'] / 100.0)

        prodPerSize = prod / struct['size']
        if prodPerSize > max:
            max = prodPerSize
            maxStruct = struct
    
    orderedStructs.append(maxStruct)
    currentRaw += maxStruct['p'] if 'p' in maxStruct else 0
    currentBonus *= (1.0 + (maxStruct['bp'] / 100.0)) if 'bp' in maxStruct else 1.0
    
    print(f"{maxStruct['name']} {max}")
    
    base = maxStruct['base'] if 'base' in maxStruct else maxStruct['name']
    toRemove = []
    totalSpace += maxStruct['size']
    existing = 0
    for struct in orderedStructs:
        if struct['name'] == base or ('base' in struct and struct['base'] == base):
            existing += 1

    if existing >= maxStruct['limit']:
        for struct in volcInfStructs:
            if 'base' in struct and struct['base'] == base:
                toRemove.append(struct)
            elif struct['name'] == base:
                toRemove.append(struct)

    for remove in toRemove:
        volcInfStructs.remove(remove)

print(currentRaw)
print(currentBonus)
print(currentRaw * currentBonus)


print(infRaw)
print(infBonus)
print(infRaw * infBonus)
# development, availability, rings, aca, patronage, trade outpost, arbilon, t5, starflare, trading fortum, writ, 
totalUbuffed = currentRaw * currentBonus * 2 * 13.75 * 1.3 * 1.3 * 1.06 * 1.04 * 1.07 * 1.01 * 1.02 * 1.05 * 1.03
print(totalUbuffed)
print(infRaw * infBonus * 2 * 1.5 * 1.26 * 1.06 * 1.04 * 1.07 * 1.01 * 1.02 * 1.05 * 1.03 * 1.1)

# trellith, darmos, lepus, vara, xiphos, ardyne, harvest, makers, radiant, solynia, nsx, weaver, klorvis
wBasicBuffs = totalUbuffed * 1.3 * 1.2 * 1.05 * 1.04 * 1.08 * 1.06 * 1.2 * 1.2 * 1.25 * 1.02 * 1.01 * 1.04 * 1.3
print(f"Basic temp buffs: {wBasicBuffs}")

# suite, lepus, farselle, moons, scruuge, scrapyard, q-pedd docking, excavator, neuralese, shimmering, sentiox, chuhn prestige, tricennium, talth, well
specialBuffs = wBasicBuffs * 1.06 * 1.4 * 1.1 * 1.18 * 1.2 * 1.02 * 1.05 * 1.1 * 1.05 * 1.05 * 1.11 * 1.04 * 1.09 * 1.03 * 1.01
print(f"Special buffs: {specialBuffs}")
#for struct in orderedStructs:
 #   print(f"{struct['name']}")
    
