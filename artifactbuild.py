import json

skip = [
    "T.O. Colony Ark",
    "Sentarch Seeker-Drones",
    "Xenotypic Mutants",
    "Verdant Estate",
    "Bio-Luminous Orb",
    "Sentiox Trilink Node",
    "Strazi Link Anchor",
    "Galaxy Elitists",
    "Bane Krow Probe",
    "Strazi Link Anchor",
    "Throne of the Revered",
    "Spectral Conclave",
    "Council Chamber",
    "SubVoid Darkdrone",
    "Cognizant Omniforge",
    "Uldri Crystal Field",
    "Uldri Power Node",
    "Seismic Shattermine (Quadrupled)",
    "Litheor Deep-Phase Sanctuary",
    "Lepus Drone",
    "Cryo-Foundry Battery (Doubled)",
    "Raix Refinery",
    "Chuhn Zenith Exchange v2",
    "Lepus C-34 Fluxgate",
    "ArcRift Tower",
    "Stryll Bioresearch Bay",
    "Jeweled Labyrinth",
    "Custodian's Villa",
    "Bainar A-Node - Advanced",
    "Thavix Reactor",
    "Exo-Rift Membrane",
    "Lepus Clone-Program Tank",
    "Alarri Comm Tower",
    "Terran-Stryll Interrogation Cell",
    "Raix Bunker",
    "Tejiar Ally HQ",
    "Sub-Tachyonic Axis",
    "Oruas Eye Chamber",
    "Chuhn Trading Hub",
    "Chuhn Trading Forum",
    "Hyperluminal Sat-Grid",
    "Litheor Core-Tunnel Shrine",
    "Bane Doom Silo",
    "Elios Solar Drill (Inverter + Heliacal)",
    "Elios Solar Drill (Heliacal)",
    "NSX Tracking Matrix",
    "Uldri Recovery Capsule",
    "Pentragulum Sparkmatter (2)",
    "Chuhn Exo-Logistics Center",
    "Chuhn Scrap Depot",
    "T.O. Frontier Redoubt",
    "Vearon Dataworks",
    "Vearon Promenade",
    "Vearon Treasury",
    "Vearon Darkpits",
    "Vearon Underforge",
    "T.O. Landfall Beacon",
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

        if 'ap' in structure or 'bap' in structure:
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
        if 'ap' in struct:
            prod += struct['ap']
        if 'bap' in struct:
            prod += currentRaw * float(struct['bap'] / 100.0)

        if prod > max:
            max = prod
            maxStruct = struct
    
    orderedStructs.append(maxStruct)
    currentRaw += maxStruct['ap'] if 'ap' in maxStruct else 0
    currentBonus *= (1.0 + (maxStruct['bap'] / 100.0)) if 'bap' in maxStruct else 1.0
    
    infRaw += maxStruct['ip'] if 'ip' in maxStruct else 0
    infBonus *= (1 + (maxStruct['bip'] / 100.0)) if 'bip' in maxStruct else 1.0
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
#      Base Spirit Chancery Ignisar Emissary Aeon   Embassy  Gravitic  Uldri  Mechanum Passion Q Catalyst Starline  Beyond  Expanse   Land Grant
space = 81 * 1.05 * 1.02 * 1.03 * 1.03 *      1.04 * 1.02 * 1.02 *      1.04 * 1.02 * 1.02 *   1.02 *      1.03    * 1.02 * 1.02     * 1.02
space = round(space)
while totalSpace < space:
    max = 0
    maxStruct = volcInfStructs[0]
    for struct in volcInfStructs:
        if struct['size'] + totalSpace > space:
            continue
        prod = 0
        if 'ap' in struct:
            prod += struct['ap']
        if 'bap' in struct:
            prod += currentRaw * float(struct['bap'] / 100.0)

        prodPerSize = prod / struct['size']
        if prodPerSize > max:
            max = prodPerSize
            maxStruct = struct
    
    orderedStructs.append(maxStruct)
    currentRaw += maxStruct['ap'] if 'ap' in maxStruct else 0
    currentBonus *= (1.0 + (maxStruct['bap'] / 100.0)) if 'bap' in maxStruct else 1.0
    infRaw += maxStruct['ip'] if 'ip' in maxStruct else 0
    infBonus *= (1.0 + (maxStruct['bip'] / 100.0)) if 'bip' in maxStruct else 1.0
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

print(f"Space: {space}")
print(currentRaw)
print(currentBonus)
print(currentRaw * currentBonus)


print(infRaw)
print(infBonus)
print(infRaw * infBonus)
#                                 development, availability, rings, aca, patronage, trade outpost, arbilon, t5, starflare, trading fortum, writ, 
totalUbuffed = currentRaw * currentBonus * 2 * 14 * 1.26 * 1.26 * 1.06 * 1.04 * 1.07 * 1.01 * 1.02 * 1.05 * 1.03
print(totalUbuffed)
print(infRaw * infBonus * 2 * 1.5 * 1.26 * 1.06 * 1.04 * 1.07 * 1.01 * 1.02 * 1.05 * 1.03 * 1.1)

# trellith, darmos, lepus, vara, xiphos, ardyne, harvest, makers, radiant, solynia, nsx, weaver, klorvis
wBasicBuffs = totalUbuffed * 1.3 * 1.2 * 1.05 * 1.04 * 1.08 * 1.06 * 1.2 * 1.2 * 1.25 * 1.02 * 1.01 * 1.04 * 1.3
print(f"Basic temp buffs: {wBasicBuffs}")

#                           suite, lepus, farselle, moons, scruuge, scrapyard, q-pedd docking, excavator, neuralese, shimmering, sentiox, chuhn prestige, tricennium, talth, well, alarri
specialBuffs = wBasicBuffs * 1.06 * 1.4 * 1.1 *     1.18 * 1.2 *     1.02 *       1.05 *         1.1 *     1.05 *      1.05 *     1.11 *      1.04 *        1.09 *    1.03 * 1.01 * 1.1
print(f"Special buffs: {specialBuffs}")
#for struct in orderedStructs:
 #   print(f"{struct['name']}")
    
totalUbuffedKwir = currentRaw * currentBonus * 2 * 14.25 * 1.3 * 1.06 * 1.04 * 1.07 * 1.01 * 1.02 * 1.05 * 1.03
print(totalUbuffedKwir)