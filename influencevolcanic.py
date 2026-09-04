import json

skip = [
"Spire of Dominion",
"Sentarch Mind-Drones",
"T.O. Colony Ark",
"Throne of the Revered",
"Bio-Luminous Orb",
"Verdant Estate",
"Custodian's Villa",
"Caustic Pit-Spire",
"Hyperluminal Sat-Grid Mesh",
"Empyreal Ice-Citadel",
"Empyreal Garden-Citadel",
"Vygos Aquaseeker",
"Gene-Root Pavilion",
"Sirocco Sandspire",
"Xecti Brood-Nest",
"Morphogenic Shift-Gate",
"Cryonic Xynapse",
"Propaganda Plex",
"Cognitor Forum",
"Tree of Harmony",
"Exotic Miners Guildhall",
"Scruuge Frost Tribunal",
"Spectral Conclave",
"Tower of Independence",
"Rhodic Prism",
"Temple of Radiance",
"Jeweled Labyrinth",
"Aeon Spire",
"Aeon Relay Tower",
"Aeon Processor Core",
"Drannik Holo-Sanctum",
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

        if 'ip' in structure or 'bip' in structure and not 'restrictions' in structure:
            #print(f"{structure['name']} {structure['size']}")
            volcInfStructs.append(structure)

orderedStructs = []
currentRaw: float = 0
currentBonus = 1.0

rawCloak = 7500
cloakBonus = 1.0

size0 = []
for struct in volcInfStructs:
    if struct['size'] == 0:
        size0.append(struct)

for struct in size0:
    volcInfStructs.remove(struct)
    orderedStructs.append(struct)

while size0.__len__() > 0:
    max = 0
    maxStruct = size0[0]
    for struct in size0:
        
        prod = 0
        if 'ip' in struct:
            prod += struct['ip']
        if 'bip' in struct:
            prod += currentRaw * float(struct['bip'] / 100.0)

        if prod > max:
            max = prod
            maxStruct = struct
    
    orderedStructs.append(maxStruct)
    currentRaw += maxStruct['ip'] if 'ip' in maxStruct else 0
    currentBonus *= (1.0 + (maxStruct['bip'] / 100.0)) if 'bip' in maxStruct else 1.0
    rawCloak += maxStruct['c'] if 'c' in maxStruct else 0
    cloakBonus *= (1.0 + (maxStruct['bc'] / 100.0)) if 'bc' in maxStruct else 1.0
    print(f"{maxStruct['name']} {max}")
    size0.remove(maxStruct)
    base = maxStruct['base'] if 'base' in maxStruct else maxStruct['name']
    toRemove = []
    for struct in size0:
        if 'base' in struct and struct['base'] == base:
            toRemove.append(struct)
        elif struct['name'] == base:
            toRemove.append(struct)

    for remove in toRemove:
        size0.remove(remove)

totalSpace = 0
maxSpace = 93
while volcInfStructs.__len__() > 0 and totalSpace < maxSpace:
    max = 0
    maxStruct = volcInfStructs[0]
    for struct in volcInfStructs:

        if struct['size'] + totalSpace > maxSpace:
            continue
        
        prod = 0
        if 'ip' in struct:
            prod += struct['ip']
        if 'bip' in struct:
            prod += currentRaw * float(struct['bip'] / 100.0)

        prodPerSize = prod / struct['size']
        if prodPerSize > max or (prodPerSize == max and struct['size'] > maxStruct['size']):
            max = prodPerSize
            maxStruct = struct
    
    orderedStructs.append(maxStruct)
    currentRaw += maxStruct['ip'] if 'ip' in maxStruct else 0
    currentBonus *= (1.0 + (maxStruct['bip'] / 100.0)) if 'bip' in maxStruct else 1.0
    rawCloak += maxStruct['c'] if 'c' in maxStruct else 0
    cloakBonus *= (1.0 + (maxStruct['bc'] / 100.0)) if 'bc' in maxStruct else 1.0
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
print(currentBonus * currentRaw)
print(cloakBonus * rawCloak)


#for struct in orderedStructs:
 #   print(f"{struct['name']}")
    
