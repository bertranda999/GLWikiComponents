import json

skip = [
    "Affection Disseminator Ultracore",
    "Bane Krow Probe",
    "Azure Prism",
    "Orbisbarrier HyperNexus",
    "Barrier HyperNexus",
    "Barrier Nexus",
    "Chuhn Zenith Exchange",
    "Scruuge Cargo Launcher",
    "Jeweled Labyrinth",
    "Lepus Hatchery",
    "Shardveil, Spectral Citadel",
    "Cygnusis AI-Core",
    "Lutuma Command Module",
    "Affection Disseminator",
    "NSX Tracking Matrix",
]

rawKey = "d"
bonusKey = "bd"

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

        if rawKey in structure or bonusKey in structure:
            #print(f"{structure['name']} {structure['size']}")
            volcInfStructs.append(structure)

orderedStructs = []
currentRaw: float = 7000
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
        if rawKey in struct:
            prod += struct[rawKey]
        if 'bp' in struct:
            prod += currentRaw * float(struct[bonusKey] / 100.0)

        if prod > max:
            max = prod
            maxStruct = struct
    
    orderedStructs.append(maxStruct)
    currentRaw += maxStruct[rawKey] if rawKey in maxStruct else 0
    currentBonus *= (1.0 + (maxStruct[bonusKey] / 100.0)) if bonusKey in maxStruct else 1.0
    
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
space = 69
while totalSpace < space:
    max = 0
    maxStruct = volcInfStructs[0]
    for struct in volcInfStructs:
        if struct['size'] + totalSpace > space:
            continue
        prod = 0
        if rawKey in struct:
            prod += struct[rawKey]
        if bonusKey in struct:
            prod += currentRaw * float(struct[bonusKey] / 100.0)

        prodPerSize = prod / struct['size']
        if prodPerSize > max:
            max = prodPerSize
            maxStruct = struct
    
    orderedStructs.append(maxStruct)
    currentRaw += maxStruct[rawKey] if rawKey in maxStruct else 0
    currentBonus *= (1.0 + (maxStruct[bonusKey] / 100.0)) if bonusKey in maxStruct else 1.0
    totalSpace += maxStruct['size']
    
    print(f"{maxStruct['name']} {max}")

    if maxStruct['limit'] > 0:
        base = maxStruct['base'] if 'base' in maxStruct else maxStruct['name']
        toRemove = []
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


