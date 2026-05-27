import json

skip = [
    "Cryo-Foundry Ice Drill (Doubled)",
    "Throne of the Revered",
    "Exotic Miners Guildhall",
    "Court of Eternity",
    "Monolith of Miracles v4",
    "Bio-Luminous Orb",
    "Forum of Realms",
    "Scruuge Cargo Launcher",
    "Sentarch Seeker-Drones",
    "Xenotypic Mutants",
    "T.O. Colony Ark"
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

        if 'mp' in structure or 'bmp' in structure:
            #print(f"{structure['name']} {structure['size']}")
            volcInfStructs.append(structure)

orderedStructs = []
currentRaw: float = 0
currentBonus = 1.0

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
        if 'mp' in struct:
            prod += struct['mp']
        if 'bmp' in struct:
            prod += currentRaw * float(struct['bmp'] / 100.0)

        if prod > max:
            max = prod
            maxStruct = struct
    
    orderedStructs.append(maxStruct)
    currentRaw += maxStruct['mp'] if 'mp' in maxStruct else 0
    currentBonus *= (1.0 + (maxStruct['bmp'] / 100.0)) if 'bmp' in maxStruct else 1.0
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
while totalSpace < 69:
    max = 0
    maxStruct = volcInfStructs[0]
    for struct in volcInfStructs:
        
        prod = 0
        if 'mp' in struct:
            prod += struct['mp']
        if 'bmp' in struct:
            prod += currentRaw * float(struct['bmp'] / 100.0)

        prodPerSize = prod / struct['size']
        if prodPerSize > max:
            max = prodPerSize
            maxStruct = struct
    
    orderedStructs.append(maxStruct)
    currentRaw += maxStruct['mp'] if 'mp' in maxStruct else 0
    currentBonus *= (1.0 + (maxStruct['bmp'] / 100.0)) if 'bmp' in maxStruct else 1.0
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


#for struct in orderedStructs:
 #   print(f"{struct['name']}")
    
