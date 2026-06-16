import json
import asyncio
import aiofiles

from pathlib import Path

configPath = "config/"
outPath = "C:/Omnipedia/GLDB/"
imgPath = "https://static.galaxylegion.com/images/"
artifactIcon = f"{imgPath}icons/special/artifact.png"

planetBuilderData = {"structures": [], "artifacts": [], "sizes": [], "types": []}

def normalizeName(name):
    return name.replace(" ", "").replace("?", "").replace(":", "")

def structureSourceLink(structure):
    if structure['sources']['artifacts'].__len__() > 0:
        return "./artifacts/" + normalizeName(structure['sources']['artifacts'][0][0]['name']) + ".html"
    else:
        return ""

def structureValue(structure, field):
    if field in structure:
        return structure[field]
    else:
        return ""

professions = {}
with open(configPath + "professions.json", "r") as file:
    professionsJson = json.load(file)
    for profession in professionsJson:
        professions[profession['name']] = profession

planetBasedAbilities = []
with open(configPath + "planet-based_abilities.json", "r") as file:
    planetBasedAbilities = json.load(file)

designs = []
with open(configPath + "ship_designs.json", "r") as designsFile:
    designs = json.load(designsFile)

modules = {}
with open(configPath + "modules.json", "r") as modulesFile:
    modulesJson = json.load(modulesFile)
    for module in modulesJson:
        modules[module['name']] = module

medals = []
with open(configPath + "medals.json", "r") as medalsFile:
    medals = json.load(medalsFile)

artifacts = {}
with open(configPath + "artifacts.json", "r") as file:
    artifactsJson = json.load(file)
    for artifact in artifactsJson:
        sources = {"medals": [], "planetBasedAbilities": [], "council": [], "artifacts": [], "legionMissions": []}
        artifacts[artifact['name']] = { **artifact, "sources": sources}

giveaways = []
with open(configPath + "giveaways.json", "r") as file:
    giveaways = json.load(file)

planetSizes = {}
with open(configPath + "planet_sizes.json", "r") as file:
    planetSizesJson = json.load(file)
    for size in planetSizesJson:
        planetSizes[size['name']] = size

galacticCouncil = []
with open(configPath + "galactic_council.json", "r") as file:
    galacticCouncil = json.load(file)

structures = {}
with open(configPath + "structures.json", "r") as file:
    structuresJson = json.load(file)
    for structure in structuresJson:
        planetBuilderData['structures'].append({k: v for k, v in structure.items() if k not in ['limited']})
        sources = {"artifacts": []}
        structures[structure['name']] = {**structure, "sources": sources}

resources = []
with open(configPath + "resources.json", "r") as file:
    resources = json.load(file)

seasonals = {}
with open(configPath + "seasonal_events.json", "r") as file:
    seasonalsJson = json.load(file)
    for seasonal in seasonalsJson:
        seasonals[seasonal['name']]  = seasonal

commonArtis = []
with open(configPath + "common_artifacts.json", "r") as file:
    commonArtis = json.load(file)

medals = []
with open(configPath + "medals.json", "r") as file:
    medals = json.load(file)

flairs = []
with open(configPath + "flairs.json", "r") as file:
    flairs = json.load(file)

ascendancyTree = []
with open(configPath + "ascendancy.json", "r") as file:
    ascendancyTree = json.load(file)

sortedMedalLines = []
with open(configPath + "medal_sorting.txt", "r") as file:
    sortedMedalLines = file.readlines()

races = {}
with open(configPath + "races.json", "r") as file:
    racesJson = json.load(file)
    for race in racesJson:
        races[race['name']] = {**race, 'legionMedals': []}

planetTypes = {}
with open(configPath + "planet_types.json", "r") as file:
    planetTypesJson = json.load(file)
    planetTypesJson = sorted(planetTypesJson, key=lambda planetType: planetType['name'])
    for planetType in planetTypesJson:
        planetTypes[planetType['name']] = planetType

petitionersSuite = {}
with open(configPath + "petitioners_suite_actions.json", "r") as file:
    actionsJson = json.load(file)
    for action in actionsJson:
        petitionersSuite[action['name']] = action

talents = {}
with open(configPath + "ascendancy.json", "r") as file:
    talentsJson = json.load(file)
    for talent in talentsJson:
        talents[talent['name']] = talent

allies = {}
with open(configPath + "allies.json", "r") as file:
    alliesJson = json.load(file)
    for ally in alliesJson:
        allies[ally['name']] = ally

initiatives = {}
with open(configPath + "voting.json", "r") as file:
    initiativesJson = json.load(file)
    for initiative in initiativesJson:
        initiatives[initiative['name']] = initiative

legionMissions = {}
with open(configPath + "legion_missions.json", "r") as file:
    legionMissionsJson = json.load(file)
    for mission in legionMissionsJson:
        legionMissions[mission['name']] = mission

councilToolData = {"levels":[], "costMods":[]}

genesEffects = []
startCharters = []

for (name, mission) in legionMissions.items():
    for task in mission['tasks']:
        artifacts[task['reward']['artifact']]['sources']['legionMissions'].append((mission, task))

for (name, ally) in allies.items():
    for unlockable in ally['unlockables']:
        if 'playerEffects' in unlockable:
            for effect in unlockable['playerEffects']:
                if effect['type'] == "Increase Genes Production":
                    genesEffects.append(("Boost", "Ally", ally['name'], effect['value'], "-"))
                elif effect['type'] == "Decrease Grow Genes Cooldown":
                    genesEffects.append(("Cooldown", "Ally", name, effect['value'], "-"))
                elif effect['type'] == "Reduce Council Cost":
                    councilToolData['costMods'].append({"name": name, "value": float(effect['value'].replace("%", ""))})

for (name, talent) in talents.items():
    if 'playerEffects' in talent:
        for effect in talent['playerEffects']:
            if effect['type'] == "Increase Genes Production":
                genesEffects.append(("Boost", "Talent", talent['name'], effect['value'], "-"))
            elif effect['type'] == "Decrease Grow Genes Cooldown":
                genesEffects.append(("Cooldown", "Talent", talent['name'], effect['value'], "-"))
    

for (name, seasonal) in seasonals.items():
    if 'playerEffects' in seasonal:
            for effect in seasonal['playerEffects']:
                if effect['type'] == "Increase Genes Production":
                    genesEffects.append(("Boost", "Seasonal", seasonal['name'], effect['value'], "-"))

for (name, race) in races.items():
    if 'evolutions' in race:
        for evolution in race['evolutions']:
            if 'playerEffects' in evolution:
                for effect in evolution['playerEffects']:
                    if effect['type'] == "Increase Genes Production":
                        genesEffects.append(("Boost", f"Evolution - {name}", evolution['name'], effect['value'], "-"))
                    elif effect['type'] == "Increase Genes Amount":
                        genesEffects.append(("Amount", f"Evolution - {name}", evolution['name'], effect['value'], "-"))
                    elif effect['type'] == "Decrease Grow Genes Cooldown":
                        genesEffects.append(("Cooldown", f"Evolution - {name}", evolution['name'], effect['value'], "-"))
                    elif effect['type'] == "Reset Grow Genes Cooldown":
                        genesEffects.append(("Reset", f"Evolution - {name}", evolution['name']))

for (name, action) in petitionersSuite.items():
    if 'playerEffects' in action:
        for effect in action['playerEffects']:
            if effect['type'] == "Increase Genes Production":
                genesEffects.append(("Boost", "Petitioners Suite", name, effect['value'], effect['duration']))
            elif effect['type'] == "Increase Genes Amount":
                genesEffects.append(("Amount", "Petitioners Suite", name, effect['value'], effect['duration']))
            elif effect['type'] == "Decrease Grow Genes Cooldown":
                genesEffects.append(("Cooldown", "Petitioners Suite", name, effect['value'], effect['duration']))
            elif effect['type'] == "Reset Grow Genes Cooldown":
                genesEffects.append(("Reset", "Petitioners Suite", name))
            
for (name, profession) in professions.items():
    if 'playerEffects' in profession:
        for effect in profession['playerEffects']:
            if effect['type'] == "Increase Genes Production":
                genesEffects.append(("Boost", "Profession", name, effect['value'], "-"))

for (name, module) in modules.items():
    if 'playerEffects' in module:
        for effect in module['playerEffects']:
            if effect['type'] == "Increase Genes Amount":
                genesEffects.append(("Amount", "Module", module['name'], effect['value'], "-", int(module['limit'])))

for (name, planetType) in planetTypes.items():
    if name == "Prismatic":
        continue
    newType = { 'name': name }
    if 'hasSpecialImage' in planetType:
        newType['hasSpecialImage'] = planetType['hasSpecialImage']
    planetBuilderData['types'].append(newType)

for ability in planetBasedAbilities:
    if "playerEffects" in ability:
        for effect in ability['playerEffects']:
            if effect['type'] == "Grants":
                if not effect['artifact'] in artifacts:
                    print(f"Missing artifact: {effect['artifact']}")
                else:
                    artifacts[effect['artifact']]['sources']['planetBasedAbilities'].append((ability, "Guaranteed"))
            elif effect['type'] == "Increase Genes Production":
                genesEffects.append(("Boost", "Planet-Based Ability", ability['name'], effect['value'], effect['duration']))
            elif effect['type'] == "Decrease Grow Genes Cooldown":
                genesEffects.append(("Cooldown", "Planet-Based Ability", ability['name'], effect['value'], effect['duration']))
            elif effect['type'] == "Reset Grow Genes Cooldown":
                genesEffects.append(("Reset", "Planet-Based Ability", ability['name']))

    if "playerEffectsRandom" in ability:
        for effect in ability['playerEffectsRandom']:
            if effect['type'] == "Grants":
                if not effect['artifact'] in artifacts:
                    print(f"Missing artifact: {effect['artifact']}")
                else:
                    artifacts[effect['artifact']]['sources']['planetBasedAbilities'].append((ability, "Chance"))

for level in galacticCouncil:
    if 'councilors' in level:
        for councilor in level['councilors']:
            artifacts[councilor['reward']]['sources']['council'].append((councilor, councilor['min'] if 'min' in councilor else 1, councilor['max'] if 'max' in councilor else 1))


for (name, seasonal) in seasonals.items():
    if 'playerEffects' in seasonal:
        for effect in seasonal['playerEffects']:
            if effect['type'] == "Reduce Council Cost":
                councilToolData['costMods'].append({"name":f"Seasonal: {seasonal['name']}", "value": float(effect['value'].replace("%", ""))})

for (name, size) in planetSizes.items():
    planetBuilderData['sizes'].append(size)

for (name, artifact) in artifacts.items():
    if not 'target' in artifact:
        print(f"Missing target: {artifact['name']}")
    if artifact['target'] == "Your Planet":
        planetBuilderData['artifacts'].append({k: v for k, v in artifact.items() if k not in ["img", "target", "buttonText", "scrap", 'requiresConfirmation', 'send', 'share']})

    if 'restrictions' in artifact:
        for restriction in artifact['restrictions']:
            if restriction['type'] == "Influence Availability" and 'max' in restriction and restriction['max'] == "None":
                startCharters.append(artifact)

    if 'planetEffects' in artifact:
        for effect in artifact['planetEffects']:
            if not 'type' in effect:
                print(f"Missing effect type: {artifact['name']}")
            if effect['type'] == 'Construct Structure':
                structures[effect['structure']]['sources']['artifacts'].append((artifact, "Guaranteed"))
            elif effect['type'] == 'Upgrade Structure':
                structures[effect['new']]['sources']['artifacts'].append((artifact, "Guaranteed"))
                for planetBuilderStructure in planetBuilderData['structures']:
                    if planetBuilderStructure['name'] == effect['new']:
                        planetBuilderStructure['base'] = effect['original']
                        break
    elif 'planetEffectsChoice' in artifact:
        for effect in artifact['planetEffectsChoice']:
            if not 'type' in effect:
                print(f"Missing effect type: {artifact['name']}")
            if effect['type'] == 'Construct Structure':
                structures[effect['structure']]['sources']['artifacts'].append((artifact, "Optional"))
            elif effect['type'] == 'Upgrade Structure':
                structures[effect['new']]['sources']['artifacts'].append((artifact, "Optional"))
                for planetBuilderStructure in planetBuilderData['structures']:
                    if planetBuilderStructure['name'] == effect['new']:
                        planetBuilderStructure['base'] = effect['original']
                        break
    elif 'planetEffectsRandom' in artifact:
        for effect in artifact['planetEffectsRandom']:
            if effect['type'] == 'Construct Structure':
                structures[effect['structure']]['sources']['artifacts'].append((artifact, "Chance"))
            elif effect['type'] == 'Upgrade Structure':
                structures[effect['new']]['sources']['artifacts'].append((artifact, "Chance"))
                for planetBuilderStructure in planetBuilderData['structures']:
                    if planetBuilderStructure['name'] == effect['new']:
                        planetBuilderStructure['base'] = effect['original']
                        break
    elif 'planetEffectsConditional' in artifact:
        for effect in artifact['planetEffectsConditional']:
            if effect['type'] == 'Construct Structure':
                structures[effect['structure']]['sources']['artifacts'].append((artifact, "Conditional"))
            elif effect['type'] == 'Upgrade Structure':
                structures[effect['new']]['sources']['artifacts'].append((artifact, "Conditional"))
                for planetBuilderStructure in planetBuilderData['structures']:
                    if planetBuilderStructure['name'] == effect['new']:
                        planetBuilderStructure['base'] = effect['original']
                        break
    elif 'playerEffects' in artifact:
        for effect in artifact['playerEffects']:
            if not 'type' in effect:
                print(f"Missing effect type: {artifact['name']}")
            if effect['type'] == 'Unlock Standard Structure':
                structures[effect['structure']]['sources']['artifacts'].append((artifact, "Unlocked"))
            elif effect['type'] == 'Decrease Grow Genes Cooldown':
                genesEffects.append(("Cooldown", "Artifact", artifact['name'], effect['value'], effect['duration'] if 'duration' in effect else "-"))
            elif effect['type'] == "Increase Genes Production":
                genesEffects.append(("Boost", "Artifact", artifact['name'], effect['value'], effect['duration'] if 'duration' in effect else "-"))
            elif effect['type'] == "Reset Grow Genes Cooldown":
                genesEffects.append(("Reset", "Artifact", artifact['name']))
            elif effect['type'] == "Deploy Structure":
                structures[effect['structure']]['sources']['artifacts'].append((artifact, "Guaranteed"))

for (name, structure) in structures.items():
    if 'base' in structure:
        finished = False
        while not finished:
            if structure['base'] in structures and 'base' in structures[structure['base']]:
                structure['base'] = structures[structure['base']]['base']
            else:
                finished = True
    if 'ability' in structure:
        if 'playerEffects' in structure['ability']:
            for effect in structure['ability']['playerEffects']:
                if effect['type'] == 'Decrease Grow Genes Cooldown':
                    genesEffects.append(("Cooldown", "Structure Ability", name, effect['value'], effect['duration'], structure))
                elif effect['type'] == "Increase Genes Production":
                    genesEffects.append(("Boost", "Structure Ability", name, effect['value'], effect['duration'], structure))
                elif effect['type'] == "Reset Grow Genes Cooldown":
                    genesEffects.append(("Reset", "Structure Ability", name, structure))
                

def generateMedalRow(medal, path="medals", includeBonus = True):
    medalRow = "<tr>"
    if 'img' in medal:
        medalRow += f"<td style=\"border: 1px solid gray;\"><img src=\"{imgPath}medals/{medal['img']}\" width=\"150\"/></td>"
    else:
        medalRow += f"<td  style=\"border: 1px solid gray;\"><img src=\"{imgPath}bg/medals-m.png\" width=\"150\"/></td>"
    medalRow += "<td id=\"" + medal['name'] + f"\" style=\"padding: 10; text-align: center; border: 1px solid gray;\"><a href=\"{path}/" + normalizeName(medal['name']) + ".html\">" + medal['name'] + "</a></td>"
    medalRow += "<td style=\"padding: 10; text-align: center; border: 1px solid gray;\">" + medal['desc'] + "</td>"
    medalRow += "<td style=\"padding: 10; text-align: center; border: 1px solid gray;width: 100\">" + medal['medalPoints'] + "</td>"
    
    if includeBonus:
        if "artifact" in medal:
            medalRow += f"<td style=\"padding: 10; text-align: center; border: 1px solid gray;\"><img src=\"{imgPath}icons/special/artifact.png\" width=\"20\"> <a href=\"artifacts/" + normalizeName(medal['artifact']) + ".html\">" + medal['artifact'] + "</a></td>"
        elif "title" in medal:
            if not 'titleCharStyle' in medal and not 'titleHtml' in medal:
                medalRow += "<td style=\"padding: 10; text-align: center; border: 1px solid gray;\">Title: <span style=\"" + ((medal['titleStyle']) + "\"" if 'titleStyle' in medal else "font-style:italic; font-weight:bold; color:#999999;\"") + ">" + medal['title'] + "</span></td>"
            elif 'titleHtml' in medal:
                medalRow += f"<style>{medal['titleCharAnimation']}</style>"
                medalRow += f"<td style=\"padding: 10; text-align: center; border: 1px solid gray;\">Title: {medal['titleHtml']}</td>"
            else:
                forward = medal['charOrder'] == "Forward"
                increment = float(medal['charDelayIncrement'])
                start = 0 if forward else (medal['title'].__len__() - 1) * increment
                medalRow += f"<style>{medal['titleCharAnimation']}</style>"
                medalRow += "<td style=\"padding: 10; text-align: center; border: 1px solid gray;\">Title: <span style=\"" + ((medal['titleStyle']) + "\"" if 'titleStyle' in medal else "font-style:italic; font-weight:bold; color:#999999;\"") + ">"
                for index, letter in enumerate(medal['title']):
                    if letter == " ":
                        medalRow += " "
                        continue
                    time = start + increment * index if forward else start - increment * index
                    medalRow += f"<span style=\"{medal['titleCharStyle']} animation-delay: {time}s;\">{letter}</span>" 
                medalRow += "</span></td>"
        elif "design" in medal:
            for design in designs:
                if design['name'] == medal['design']:
                    medalRow += "<td style=\"padding: 10; text-align: center; border: 1px solid gray;\">" + design['name'] + f"<br><img src=\"{imgPath}" + design['img'] + "\" width=\"100\"></img></td>"
        elif "flair" in medal:
            for flair in flairs:
                if flair['name'] == medal['flair']:
                    medalRow += f"<td style=\"padding: 10; text-align: center; border: 1px solid gray;\">{medal['flair']}<br>{flair['preview']}</td>"
        elif "ability" in medal:
            medalRow += f"<td style=\"padding: 10; text-align: center; border: 1px solid gray;\"><img style=\"height: 18; width: 18\" src=\"{imgPath}icons/special/ability.png\">Ability: {medal['ability']['name']}<br>{medal['ability']['desc']}</td>"
        else:
            medalRow += f"<td style=\"padding: 10; text-align: center; border: 1px solid gray;\">None</td>"
    medalRow += "</tr>"
    return medalRow


def generateMedalTableHeader(includeBonus = True):
    medalsHtmlHeader = "<table class=\"sortable\">"
    medalsHtmlHeader += f"<thead><tr><th class=\"sorttable_nosort\" style=\"border: 1px solid gray;width: 150\">Image</th>"
    medalsHtmlHeader += f"<th class=\"sort_a\" style=\"padding: 10; border: 1px solid gray\">Name</th>"
    medalsHtmlHeader += f"<th class=\"sorttable_nosort\" style=\"padding:10; border: 1px solid gray;width: 500\">Description</th>"
    medalsHtmlHeader += f"<th style=\"border: 1px solid gray;padding: 10; width: 100\">Points</th>"
    if includeBonus:
        medalsHtmlHeader += f"<th class=\"sorttable_nosort\" style=\"border: 1px solid gray;width: 300\">Bonus</th></tr></thead>" 
    return medalsHtmlHeader

def icons(name, height=20):
    path = ""
    if name == "Studies":
        path = "icons/studies3.png"
    elif name == "Research":
        path = "icons/research.png"
    elif name == "Influence":
        path = "icons/influence.png"
    elif name == "Red Badges":
        path = "icons/special/badge-r.png"
    elif name == "Blue Badges":
        path = "icons/special/badge-b.png"
    elif name == "Yellow Badges":
        path = "icons/special/badge-y.png"
    elif name == "Green Badges" or name.lower() == "greens":
        path = "icons/special/badge-g.png"
    elif name == "Silver Badges" or name.lower() == "silvers":
        path = "icons/special/badge-s.png"
    elif name == "Relic Badges" or name == "relic":
        path = "icons/special/relicbadge2.png"
    elif name == "Aeon Badges":
        path = "icons/special/badge-a.png"
    elif name.lower() == "ctp":
        path = "icons/special/parts.png"
    elif name == "CR" or name == "cr":
        path = "icons/credits.png"
    elif name == "XP":
        path = "icons/xp.png"
    elif name == "GP":
        path = "icons/galaxypoints.png"
    elif name == "PT":
        path = "icons/special/relic.png"
    elif name == "Uldri Credits":
        path = "icons/special/uldricred.png"
    elif name == "XTS9":
        path = "icons/special/xts9.png"
    elif name == "EM":
        path = "icons/special/exotic.png"
    elif name == "Dark Badges":
        path = "icons/special/badge-l.png"
    elif name == "MP":
        path = "icons/starpoints-button.png"
    elif name == "PF":
        path = "icons/special/political.png"
    elif name == "Genes":
        path = "icons/dna.png"
    elif name == "Energy":
        path = "icons/energy.png"
    else:
        return name
    
    return f"<img height=\"{height}\" src=\"{imgPath + path}\">"

async def writeStructures():
    html = "<head><link rel=\"stylesheet\" href=\"style.css\"><script type=\"text/javascript\" charset=\"utf8\" src=\"../sorttable.js\" defer></script></head><table class=\"sortable\"><thead><tr>"
    html += f"<th class=\"sort_a\" style=\"border: 1px solid gray;width: 100\">Name</th>"
    html += f"<th style=\"border: 1px solid gray;width: 50\">Extract</th>"
    html += f"<th style=\"border: 1px solid gray;width: 50\">Limited</th>"
    html += f"<th style=\"border: 1px solid gray;width: 20\">Limit</th>"
    html += f"<th style=\"border: 1px solid gray;width: 20\">Size</th>"
    html += f"<th style=\"border: 1px solid gray;width: 20\">MP</th>"
    html += f"<th style=\"border: 1px solid gray;width: 20\">BMP</th>"
    html += f"<th style=\"border: 1px solid gray;width: 20\">MPS</th>"
    html += f"<th style=\"border: 1px solid gray;width: 20\">AP</th>"
    html += f"<th style=\"border: 1px solid gray;width: 20\">BAP</th>"
    html += f"<th style=\"border: 1px solid gray;width: 20\">APS</th>"
    html += f"<th style=\"border: 1px solid gray;width: 20\">RP</th>"
    html += f"<th style=\"border: 1px solid gray;width: 20\">BRP</th>"
    html += f"<th style=\"border: 1px solid gray;width: 20\">RPS</th>"
    html += f"<th style=\"border: 1px solid gray;width: 20\">IP</th>"
    html += f"<th style=\"border: 1px solid gray;width: 20\">BIP</th>"
    html += f"<th style=\"border: 1px solid gray;width: 20\">IPS</th>"
    html += f"<th style=\"border: 1px solid gray;width: 20\">AT</th>"
    html += f"<th style=\"border: 1px solid gray;width: 20\">BAT</th>"
    html += f"<th style=\"border: 1px solid gray;width: 20\">D</th>"
    html += f"<th style=\"border: 1px solid gray;width: 20\">BD</th>"
    html += f"<th style=\"border: 1px solid gray;width: 20\">P</th>"
    html += f"<th style=\"border: 1px solid gray;width: 20\">BP</th>"
    html += f"<th style=\"border: 1px solid gray;width: 20\">C</th>"
    html += f"<th style=\"border: 1px solid gray;width: 20\">BC</th>"
    html += f"<th style=\"border: 1px solid gray;width: 20\">IC</th>"
    html += f"<th style=\"border: 1px solid gray;width: 20\">ES</th>"
    html += f"<th style=\"border: 1px solid gray;width: 20\">ID</th>"
    html += "</tr></thead><tbody>"
    for (name, structure) in structures.items():
        source = structureSourceLink(structure)
        html += "<tr>"
        html += f"<td style=\"border: 1px solid gray;width: 300\"><a href=\"{source}\">{structure['name']}</a></td>"
        html += f"<td style=\"border: 1px solid gray;width: 50\">{structure['extract']}</td>"
        html += f"<td style=\"border: 1px solid gray;width: 50\">{structure['limited']}</td>"
        html += f"<td style=\"border: 1px solid gray;width: 20\">{structure['limit']}</td>"
        html += f"<td style=\"border: 1px solid gray;width: 20\">{structure['size']}</td>"
        html += f"<td style=\"border: 1px solid gray;width: 40\">{structureValue(structure, 'mp')}</td>"
        html += f"<td style=\"border: 1px solid gray;width: 40\">{structureValue(structure, 'bmp')}</td>"
        html += f"<td style=\"border: 1px solid gray;width: 40\">{structureValue(structure, 'mps')}</td>"
        html += f"<td style=\"border: 1px solid gray;width: 40\">{structureValue(structure, 'ap')}</td>"
        html += f"<td style=\"border: 1px solid gray;width: 40\">{structureValue(structure, 'bap')}</td>"
        html += f"<td style=\"border: 1px solid gray;width: 40\">{structureValue(structure, 'aps')}</td>"
        html += f"<td style=\"border: 1px solid gray;width: 40\">{structureValue(structure, 'rp')}</td>"
        html += f"<td style=\"border: 1px solid gray;width: 40\">{structureValue(structure, 'brp')}</td>"
        html += f"<td style=\"border: 1px solid gray;width: 40\">{structureValue(structure, 'rps')}</td>"
        html += f"<td style=\"border: 1px solid gray;width: 40\">{structureValue(structure, 'ip')}</td>"
        html += f"<td style=\"border: 1px solid gray;width: 40\">{structureValue(structure, 'bip')}</td>"
        html += f"<td style=\"border: 1px solid gray;width: 40\">{structureValue(structure, 'ips')}</td>"
        html += f"<td style=\"border: 1px solid gray;width: 40\">{structureValue(structure, 'at')}</td>"
        html += f"<td style=\"border: 1px solid gray;width: 40\">{structureValue(structure, 'bat')}</td>"
        html += f"<td style=\"border: 1px solid gray;width: 40\">{structureValue(structure, 'd')}</td>"
        html += f"<td style=\"border: 1px solid gray;width: 40\">{structureValue(structure, 'bd')}</td>"
        html += f"<td style=\"border: 1px solid gray;width: 40\">{structureValue(structure, 'p')}</td>"
        html += f"<td style=\"border: 1px solid gray;width: 40\">{structureValue(structure, 'bp')}</td>"
        html += f"<td style=\"border: 1px solid gray;width: 40\">{structureValue(structure, 'c')}</td>"
        html += f"<td style=\"border: 1px solid gray;width: 40\">{structureValue(structure, 'bc')}</td>"
        html += f"<td style=\"border: 1px solid gray;width: 40\">{structureValue(structure, 'ic')}</td>"
        html += f"<td style=\"border: 1px solid gray;width: 40\">{structureValue(structure, 'es')}</td>"
        html += f"<td style=\"border: 1px solid gray;width: 40\">{structureValue(structure, 'id')}</td>"
        html += "</tr>"
    html += "</tbody></table>"
    async with aiofiles.open(outPath + "structures.html", "w") as file:
        await file.write(html)

    async with aiofiles.open("config/planetbuilderdata.json", "w") as file:
        jsonString = json.dumps(planetBuilderData, separators=(',', ':'))
        await file.write(jsonString)

asyncio.run(writeStructures())

async def writeMedals():
    mp = 0
    gpMp = 0

    medalsHtmlTable = generateMedalTableHeader()

    html = "<head><link rel=\"stylesheet\" href=\"style.css\"><script type=\"text/javascript\" charset=\"utf8\" src=\"../sorttable.js\" defer></script><script type=\"text/javascript\" charset=\"utf8\" src=\"../collapsible.js\" defer></script></head>"
    tablesHtml = ""
    tocHtml = ""

    sortedMedals = []

    medalsHtmlTable = generateMedalTableHeader()
    for line in sortedMedalLines:
        line = line.strip()
        colonSplit = line.split(":")
        if colonSplit[0] == "Domain":
            tablesHtml += f"<br><h2 id=\"{colonSplit[1]}\">{colonSplit[1]}</h2><br>"
            lastDomain = colonSplit[1]
            tocHtml += f"</span> <a href=\"#{colonSplit[1]}\" style=\"padding-right: 10;\">{colonSplit[1]}</a><button type=\"button\" class=\"collapsible\"><svg width=\"10px\" height=\"10px\" viewBox=\"0 0 32 32\" xmlns=\"http://www.w3.org/2000/svg\" fill=\"none\"><path stroke=\"#535358\" stroke-linecap=\"round\" stroke-linejoin=\"round\" stroke-width=\"2\" d=\"M9 20l7 7 7-7M23 12l-7-7-7 7\"/></svg></button><br><span hidden class=\"content\">"
        elif colonSplit[0] == "Section":
            tablesHtml += f"<h3 id=\"{lastDomain}-{colonSplit[1]}\">{colonSplit[1]}</h3><br>"
            tocHtml += f"&emsp;<a href=\"#{lastDomain}-{colonSplit[1]}\">{colonSplit[1]}</a><br>"
            tablesHtml += generateMedalTableHeader()
        elif line != "":
            found = False
            for medal in medals:
                if medal['name'] == line:
                    for sortedMedal in sortedMedals:
                        if sortedMedal['name'] == medal['name']:
                            print(f"Duplicate sorted medal: {medal['name']}")
                    sortedMedals.append(medal)
                    tablesHtml += generateMedalRow(medal)
                    found = True
                    medalsHtmlTable += generateMedalRow(medal)

                    medalMp = int(medal['medalPoints'].replace(",", ""))
                    mp += medalMp
                    if any(key in medal for key in ['requiresGP', 'requiresSupporterBonus']):
                        gpMp += medalMp
                    
                    if 'triggers' in medal:
                        for trigger in medal['triggers']:
                            if trigger['type'] == "Receive Artifact" and 'races' in trigger:
                                for triggerRace in trigger['races']:
                                    races[triggerRace]['legionMedals'].append(medal)
        
                    if 'artifact' in medal:
                        if not medal['artifact'] in artifacts:
                            print(f"Missing artifact: {medal['artifact']}")
                        else:
                            artifacts[medal['artifact']]['sources']['medals'].append(medal)

            if not found:
                print("Not found: " + line)
        else:
            tablesHtml += "</table>"

    if sortedMedals.__len__() != medals.__len__():
        for medal in medals:
            found = False
            for sortedMedal in sortedMedals:
                if sortedMedal['name'] == medal['name']:
                    found = True
            if not found:
                print(f"Medal not in sorted list: {medal['name']}")
        if sortedMedals.__len__() > medals.__len__():
            print("Duplicates in sorted medal list")
        print("Missing medals from sort")

    html += tocHtml + "</span>"
    html += tablesHtml
    async with aiofiles.open(outPath + "medals_sorted.html", "w") as file:
        await file.write(html)

    medalsHtmlTable += "</table>"
    async with aiofiles.open(outPath + "medals.html", "w") as file:
        unsortedHtml = "<head><link rel=\"stylesheet\" href=\"style.css\"><script type=\"text/javascript\" charset=\"utf8\" src=\"../sorttable.js\" defer></script></head><div>"
        
        await file.write(f"{unsortedHtml}{medalsHtmlTable}</div>")

    
    for medal in sortedMedals:

        async with aiofiles.open(outPath + "medals/" + normalizeName(medal['name']) + ".html", "w") as medalFile:
            medalFileHtml = "<head><link rel=\"stylesheet\" href=\"../style.css\"></head>"
            if 'img' in medal:
                medalFileHtml += f"<img src=\"{imgPath}medals/{medal['img']}\"/>"
            medalFileHtml += "<div>"
            medalFileHtml += f"<img src=\"{imgPath}bg/medals-m.png\" width=\"25\">"
            medalFileHtml += medal['name']
            medalFileHtml += "<br>"
            medalFileHtml += f"<img src=\"{imgPath}icons/starpoints-button.png\" width=\"25\">" + str(medal['medalPoints'] + "<br>")
            medalFileHtml += medal['desc'] + "<br>"
            
            if "artifact" in medal:
                artifactPage = configPath + normalizeName(medal['artifact']) + ".html"
                medalFileHtml += f"<img src=\"{imgPath}icons/special/artifact.png\" width=\"20\"><a href=\"" + artifactPage + "\">" + medal['artifact'] + "</a>"
            elif "title" in medal:
                if not 'titleCharStyle' in medal and not 'titleHtml' in medal:
                    medalFileHtml += "<td style=\"padding: 10; text-align: center; border: 1px solid gray;\">Title: <span style=\"" + ((medal['titleStyle']) + "\"" if 'titleStyle' in medal else "font-style:italic; font-weight:bold; color:#999999;\"") + ">" + medal['title'] + "</span></td>"
                elif 'titleHtml' in medal:
                    medalFileHtml += f"<style>{medal['titleCharAnimation']}</style>"
                    medalFileHtml += f"<td style=\"padding: 10; text-align: center; border: 1px solid gray;\">Title: {medal['titleHtml']}</td>"
            elif "design" in medal:
                for design in designs:
                    if design['name'] == medal['design']:
                        medalFileHtml += f"Design: {design['name']}<br>"
                        medalFileHtml += f"<img src=\"{imgPath}{design['img']}\"></img>"

            await medalFile.write(medalFileHtml + "</div>")

asyncio.run(writeMedals())


async def writeAscendancy():
    html = f'''<head><style>a:link {{ color: white; }} body {{ background: url('{imgPath}bg/farbackground.jpg') repeat 20% 20%; color: white; font-family: Arial, Helvetica, sans-serif;}}</style></head>
    <h1>Ascendancy Tree</h1>
    <h3 style="display: block;"><div style="max-width: 460px;"><div style="font-size: 14px; font-weight: bold; color: #6089f9; letter-spacing: 1px; text-transform: uppercase; margin-bottom: 8px; text-shadow: 0 0 8px rgba(96,137,249,0.3);">Legion Ascendancy</div><div style="color: #b0b8c0; line-height: 1.6;">
    <div style="margin-top: 10px; padding: 8px 10px; background: rgba(96,137,249,0.08); border: 1px solid rgba(96,137,249,0.25); border-radius: 4px;">
    The Ascendancy Tree is a shared talent tree for the legion. Members pool resources to unlock permanent bonuses that benefit everyone who is loyal. Each option has a number of 'phases' required to unlock, and members can contribute resources to advance progress by 1 phase (with a per-member cooldown).
    <br><br>Each tier unlocks new talents with increasing costs. Higher tiers require previous options to be fully unlocked before they become available, and many are not visible until their paths are cleared.
    </div></div></div></h3>
    '''

    currentLevel = 0
    for talent in ascendancyTree:
        if talent['level'] > currentLevel:
            if talent['level'] != 1:
                html += "</div>"
            currentLevel = talent['level']
            html += "<div style=\"display: flex; justify-content: center; align-items: center;\">"
        nameStr = "<strong><em>Unknown</em></strong>"
        if talent['name'] != "Unknown":
            nameStr = f"<a href=\"ascendancy/{normalizeName(talent['name'])}.html\">{talent['name']}</a>"
        html += f"<div style=\"padding: 10;justify-content: center; align-items: center; width: 300; height: 250;\">{nameStr}" + (f"<br>{talent['bonusDesc']}" if 'bonusDesc' in talent else "")
        if 'phases' in talent:
            html += f"<br>Phases: {talent['phases']}"
        if 'cost' in talent:
            html += f"<br>Phase Cost:<br>"
            first = True
            for key in talent['cost']:
                if not first:
                    html += "<br>"
                html += f"&nbsp;&nbsp;&nbsp;&nbsp;{talent['cost'][key]}&nbsp;{icons(key)}"
                if first:

                    first = False
        if 'prereqs' in talent:
            if talent['prereqs'].__len__() == 2:
                html += f"<br>Requirements<br>&nbsp;&nbsp;&nbsp;&nbsp;{talent['prereqs'][0]}<br>&nbsp;&nbsp;&nbsp;&nbsp;{talent['prereqs'][1]}"
            elif talent['prereqs'].__len__() == 1:
                html += f"<br>Requirements<br>&nbsp;&nbsp;&nbsp;&nbsp;{talent['prereqs'][0]}"
        html += "</div>"

        if talent['name'] != "Unknown":
            talentPage = f"<head><style>a:link {{ color: white; }} body {{ background: url('{imgPath + 'bg/' + talent['img']}'), url('{imgPath}bg/farbackground.jpg'); background-repeat: no-repeat, repeat; background-position: 0% 0%, 20% 20%; color: white; font-family: Arial, Helvetica, sans-serif;}}</style></head>"
            talentPage += f"<h1>{talent['name']}</h1><br>{talent['bonusDesc']}<br><br>{talent['desc']}"

            async with aiofiles.open(outPath + f"/ascendancy/{normalizeName(talent['name'])}.html", "w") as file:
                await file.write(talentPage)

    html += "</div>"

    async with aiofiles.open(outPath + "ascendancy.html", "w") as file:
        await file.write(html)

asyncio.run(writeAscendancy())
    
async def writeDesignFun():
    html = f"<head><script type=\"text/javascript\" charset=\"utf8\" src=\"../radio_buttons.js\" defer></script><style>@keyframes flair-goldshimmer {{   			0% {{ background-position: -200% 0; }} 20% {{ background-position: 100% 0; }} 100% {{ background-position: 100% 0; }} }} @keyframes title-ripple {{ 0% {{ opacity: 0.5; transform: translateY(-4px); color: #3366aa; }} 8% {{ opacity: 1; transform: translateY(0); color: #66bbff; text-shadow: 0 0 10px rgba(60,140,255,0.8), 0 0 20px rgba(60,140,255,0.3); }} 16% {{ opacity: 1; transform: translateY(0); color: #d8e4f4; text-shadow: none; }} 100% {{ opacity: 0.9; transform: translateY(0); color: #c8d6e8; text-shadow: none; }} }} .title-ripple-char {{display: inline-block; color: #c8d6e8; opacity: 0.9; animation: title-ripple 8s ease-out infinite;}} label {{ color: white; }} body {{ background: url('{imgPath}bg/farbackground.jpg') repeat 20% 20%; color: white; font-family: Arial, Helvetica, sans-serif;}}</style></head><a href=\"gldb.html\">Back to Main</a><div id=\"TB_ajaxContent\" style=\"width:480px;height:280px\"><div id=\"playerinfo\" style=\"width: 480;\"><div id=\"flair-effect-wrapper\" class=\"flair-effect-wrapper\" style=\"position: absolute; left: 48px; top: 50px; width: 250px; height: 133px; pointer-events: none;\"><img id=\"shield\" hidden><img id=\"shipimg\" style=\"position: relative; left: 40px; top: 40px;\" width=\"250\" src=\"{imgPath}ships/abyssiod-right.png\"><img id=\"nightclaw\" style=\"position: absolute; z-index: -1; left: 5px; top: 5px;\" hidden src=\"{imgPath}planets/effects/fighter4.png\"><img id=\"cerulean\" style=\"position: absolute; z-index: 10; left: 250px; top: 140px;\" hidden src=\"{imgPath}planets/effects/fighter3.png\"><div id=\"playerheader\" style=\"width: 176\"><div style=\"width: 176; position: absolute; left: 330; top: 20; text-align: center; padding: 8px 12px; margin-bottom: 8px;\"><div id=\"playername\" style=\"color: white;display: inline-block; font-size: 18px; font-weight: bold; font-family: Arial, Helvetica, sans-serif; position: relative;\"><span id=\"name-effect-element\">Player Name</span></div><div id=\"rank-div\" style=\"margin-top: 6px; padding-top: 6px; border-top: 1px solid rgba(255,255,255,0.2);\"><div style=\"white-space: nowrap; font: 12px Arial, Helvetica, sans-serif;\"><strong id=\"rank\">Rank 1000</strong><span id=\"race\"> Aerlen Biologist</span></div><div id=\"legion-name\" style=\"white-space: nowrap; font: 12px Arial, Helvetica, sans-serif;\">Legion Name (60)</div></div></div></div><br></div></div></div>"

    html += "Player Name: <input type=\"text\" maxlength=\"15\" id=\"player-name-input\" value=\"Player Name\">Legion Name: <input type=\"text\" maxlength=\"15\" id=\"legion-name-input\" value=\"Legion Name\">Legion Member Count: <input type=\"number\" id=\"member-count\" min=\"0\" max=\"99\" value=\"60\"><br>Rank: <input type=\"number\" id=\"rank-input\" min=\"1\" max=\"100000\" value=\"1000\">"
    html += "Race:<select name=\"races\" id=\"race-input\"><option value=\"Aerlen\">Aerlen</option><option value=\"Human\">Human</option><option value=\"Inergon\">Inergon</option><option value=\"Konqul\">Konqul</option><option value=\"Sillixx\">Sillixx</option><option value=\"Vygoid\">Vygoid</option><option value=\"Bahreen\">Bahreen</option><option value=\"Drannik\">Drannik</option><option value=\"Genetarr\">Genetarr</option><option value=\"Kronyn\">Kronyn</option><option value=\"Lazuli\">Lazuli</option><option value=\"Litheor\">Litheor</option><option value=\"Mylarai\">Mylarai</option><option value=\"Taltherian\">Taltherian</option><option value=\"Uldrinan\">Uldrinan</option><option value=\"Xecti\">Xecti</option><option value=\"Zolazin\">Zolazin</option><option value=\"Space Entity\">Space Entity</option><option value=\"Octafari\">Octafari</option><option value=\"Comet\">Comet</option><option value=\"Undulok\">Undulok</option><option value=\"Singularity\">Singularity</option><option value=\"Dark\">Dark</option></select>"
    html += "Profession:<select name=\"professions\" id=\"profession-input\"><option value=\"Biologist\">Biologist</option><option value=\"Builder\">Builder</option><option value=\"Diplomat\">Diplomat</option><option value=\"Excavator\">Excavator</option><option value=\"Explorer\">Explorer</option><option value=\"Fixer\">Fixer</option><option value=\"Governor\">Governor</option><option value=\"Guard\">Guard</option><option value=\"Hacker\">Hacker</option><option value=\"Mentor\">Mentor</option><option value=\"Merchant\">Merchant</option><option value=\"Miner\">Miner</option><option value=\"Physicist\">Physicist</option><option value=\"Raider\">Raider</option><option value=\"Saboteur\">Saboteur</option><option value=\"Spy\">Spy</option><option value=\"Smuggler\">Smuggler</option></select>"

    html += '''<div class="tab">
    <button class="tablinks" onclick="openTab(event, 'designs')">Designs</button>
    <button class="tablinks" onclick="openTab(event, 'titles')">Titles</button>
    <button class="tablinks" onclick="openTab(event, 'shields')">Shields</button>
    <button class="tablinks" onclick="openTab(event, 'name-effects')">Name Effects</button>
    <button class="tablinks" onclick="openTab(event, 'name-frames')">Name Frames</button>
    <button class="tablinks" onclick="openTab(event, 'ship-effects')">Ship Effects</button>
    <button class="tablinks" onclick="openTab(event, 'fighters')">Fighters</button>
    </div>'''

    count = 1
    html += "<div id=\"name-frames-tab\" class=\"tab-page\" hidden data-tab=\"name-frames\"><table data-group=\"name-frame\"><tr>"
    html += "<td width=\"300\"><input type=\"radio\" id=\"name-frame-none\" name=\"name-frame\" checked><label for=\"None\">None<br></label></td>"

    for flair in flairs:
        if count == 8:
            html += "</tr><tr>"
            count = 0
        if flair['type'] == "Name Frame":
            html += f"<td width=\"300\"><input type=\"radio\" id=\"{flair['name']}\" name=\"name-frame\" data-style={flair['style']} data-img=\"{imgPath + flair['img']}\"><label style=\"place-items: center;\" id=\"{flair['name']}-label\" for=\"{flair['name']}\">{flair['name']}<br>{flair['preview']}<br><label style=\"display: none;\" for=\"{flair['name']}-slider\">{flair['name']} Brightness Slider</label><input type=\"range\" id=\"{flair['name']}-slider\" name=\"{flair['name']}-slider\" min=\"0\" max=\"360\" value=\"180\" step=\"1\"></label></td>"

    html += "</table></div>"

    count = 1
    html += "<div id=\"ship-effects-tab\" class=\"tab-page\" hidden data-tab=\"ship-effects\"><table data-group=\"ship-effect\"><tr>"
    html += "<td width=\"300\"><input type=\"radio\" id=\"Ship_Effect_None\" name=\"ship-effect\" checked><label for=\"None\">None<br></label></td>"

    for flair in flairs:
        if count == 8:
            html += "</tr><tr>"
            count = 0
        if flair['type'] == "Ship Effect":
            html += f"<td width=\"300\"><input type=\"radio\" id=\"{flair['name']}\" name=\"ship-effect\"><label style=\"place-items: center;\" id=\"{flair['name']}-label\" for=\"{flair['name']}\">{flair['name']}<br>{flair['preview']}</label></td>"
    html += "</table></div>"
    count = 1

    html += "<div id=\"name-effects-tab\" class=\"tab-page\" hidden data-tab=\"name-effects\"><table data-group=\"name-effect\"><tr>"
    html += "<td width=\"300\"><input type=\"radio\" id=\"Name_Effect_None\" name=\"name-effect\" checked><label for=\"None\">None<br></label></td>"

    for flair in flairs:
        if count == 8:
            html += "</tr><tr>"
            count = 0
        if flair['type'] == "Name Effect":
            html += f"<td width=\"300\"><input type=\"radio\" id=\"{flair['name']}\" name=\"name-effect\"><label id=\"{flair['name']}-label\" for=\"{flair['name']}\">{flair['name']}<br>{flair['preview']}</label></td>"

    html += "</table></div>"
    count = 1
    html += "<div id=\"shields-tab\" class=\"tab-page\" hidden data-tab=\"shields\"><table data-group=\"shield\"><tr>"
    html += f"<td width=\"300\"><input type=\"radio\" id=\"Shield_None\" name=\"shield\" data-img=\"\" checked><label for=\"None\">None<br></label></td>"
    html += f"<td width=\"300\" id=\"default-shield-cell\"><input type=\"radio\" id=\"Shield_default\" name=\"shield\" data-img=\"{imgPath}ships/abyssiod-shield.png\"><label for=\"None\">Default<br><img id=\"default-shield-preview\" width=\"100\" src=\"{imgPath}ships/abyssiod-shield.png\"></label></td>"
    for flair in flairs:
        if count == 8:
            html += "</tr><tr>"
            count = 0
        if flair['type'] == "Shield":
            html += f"<td width=\"300\"><input type=\"radio\" id=\"{flair['name']}\" name=\"shield\" data-img=\"{imgPath + flair['img']}\"><label id=\"{flair['name']}-preview-label\" for=\"{flair['name']}\">{flair['name']}<br><img id=\"{flair['name']}-image\" width=\"100\" src=\"{imgPath + flair['img']}\"><br><label style=\"display: none;\" for=\"{flair['name']}-slider\">{flair['name']} Brightness Slider</label><input type=\"range\" id=\"{flair['name']}-slider\" name=\"{flair['name']}-slider\" min=\"50\" max=\"150\" value=\"100\" step=\"1\"></label></td>"
            count += 1
        
    html += "</table></div>"
    count = 0
    html += "<div id=\"designs-tab\" class=\"tab-page\" data-tab=\"designs\"><table data-group=\"design\"><tr>"
    for design in designs:
        if count == 8:
            html += "</tr><tr>"
            count = 0
        designPath = imgPath + design['img']
        shieldPath = ""
        if 'ship-base' in design['img']:
            shieldPath = imgPath + design['img'].replace('ship-base', 'ship-shield').replace('-right', '')
        elif 'right' in design['img']:
            shieldPath = imgPath + design['img'].replace('right', 'shield')
        html += f"<td width=\"300\"><input type=\"radio\" id=\"{design['name']}\" name=\"design\" data-img=\"{designPath}\"" + (" data-shield=\"" + shieldPath + "\" " if shieldPath != "" else "") + f"><label for=\"{design['name']}\">{design['name']}<br><img width=\"100\" src=\"{designPath}\"></label></td>"
        count += 1

    html += "</table></div>"

    count = 1
    titleWidth = 300
    html += "<div id=\"titles-tab\" class=\"tab-page\" hidden data-tab=\"titles\"><table data-group=\"title\"><tr>"
    html += f"<td width=\"{titleWidth}\"><input type=\"radio\" id=\"title_none\" name=\"title\" data-img=\"\" checked><label for=\"None\">None<br></label></td>"
    sortedTitles = sorted(medals, key=lambda medal: medal['title'] if 'title' in medal else '')
    for medal in sortedTitles:
        if 'title' in medal:
            if count == 8:
                html += "</tr><tr>"
                count = 0
            if not 'titleCharStyle' in medal and not 'titleHtml' in medal:
                style = medal['titleStyle'] if 'titleStyle' in medal else "font-style:italic; font-weight:bold; color:#999999;"
                html += f"<td style=\"padding-top: 10; padding-bottom: 10;\" width=\"{titleWidth}\"><input type=\"radio\" data-style=\"{style}\" data-title=\"{medal['title']}\" name=\"title\"\"><label id=\"label-{medal['title']}\" for=\"{medal['title']}\"><span style=\"{style}\">{medal['title']}</span></label></td>"
            elif 'titleHtml' in medal:
                html += f"<style>{medal['titleCharAnimation']}</style>"
                html += f"<td style=\"padding-top: 10; padding-bottom: 10;\" width=\"{titleWidth}\"><input type=\"radio\" data-title=\"{medal['title']}\" name=\"title\"\"><label id=\"label-{medal['title']}\" for=\"{medal['title']}\"><span>{medal['titleHtml']}</span></label></td>"
            else:
                forward = medal['charOrder'] == "Forward"
                increment = float(medal['charDelayIncrement'])
                start = 0 if forward else (medal['title'].__len__() - 1) * increment
                html += f"<style>{medal['titleCharAnimation']}</style>"
                html += f"<td style=\"padding-top: 10; padding-bottom: 10;\" width=\"{titleWidth}\"><input type=\"radio\" data-style=\"{medal['titleStyle']}\" data-title=\"{medal['title']}\" name=\"title\"\"><label id=\"label-{medal['title']}\" style=\"{medal['titleStyle']}\" for=\"{medal['title']}\">"
                for index, letter in enumerate(medal['title']):
                    if letter == " ":
                        html += " "
                        continue
                    time = start + increment * index if forward else start - increment * index
                    html += f"<span style=\"{medal['titleCharStyle']} animation-delay: {time}s;\">{letter}</span>" 
                html += "</label></td>"
            count += 1
    html += "</table></div>"

    html += "<div id=\"fighters-tab\" class=\"tab-page\" hidden data-tab=\"fighters\"><table><tr>"
    html += f"<td width=\"300\"><input type=\"checkbox\" id=\"nightclaw-checkbox\"><label for=\"nightclaw-checkbox\">Nightclaw<br><img src=\"{imgPath}planets/effects/fighter4.png\"></td>"
    html += f"<td width=\"300\"><input type=\"checkbox\" id=\"cerulean-checkbox\"><label for=\"cerulean-checkbox\">Cerulean<br><img src=\"{imgPath}planets/effects/fighter3.png\"></td>"
    html += "</tr></table>"
    async with aiofiles.open(outPath + "design_fun.html", "w") as file:
        await file.write(html)

asyncio.run(writeDesignFun())

async def writeResources():
    html = "<head><link rel=\"stylesheet\" href=\"style.css\"></head>"
    for resource in resources:
        html += f"<a href=./resources/{normalizeName(resource['name'])}.html>{resource['name']}</a><br>"
        resourceHtml = "<head><link rel=\"stylesheet\" href=\"../style.css\"><script type=\"text/javascript\" charset=\"utf8\" src=\"../../sorttable.js\" defer></script></head>"
        resourceHtml += f"<img height=\"20\" src=\"{imgPath + resource['img']}\">  {resource['name']} <br>"
        resourceHtml += "In-game Description:<br>" + resource['desc'] + "<br><br>" + "Explanation:<br>" + resource['explanation'] + "<br><br>Storage:<br>" + resource['capacity'] + "<br><br>"

        if 'usageTable' in resource and resource['usageTable']:
            costTable = "Uses:<br><table class=\"sortable\"><thead><tr>"
            costTable += f"<th class=\"sort_a\" style=\"border: 1px solid gray;width: 200\">Usage</th>"
            costTable += f"<th style=\"border: 1px solid gray;width: 40\">Cost</th></tr></thead>"
        
            for (name, artifact) in artifacts.items():
                if 'cost' in artifact and resource['name'] in artifact['cost']:
                    costTable += f"<td style=\"border: 1px solid gray;width: 200\">Artifact: {artifact['name']}</td>"
                    costTable += f"<td style=\"border: 1px solid gray;width: 40\">{artifact['cost'][resource['name']]}</td></tr>"

            costTable += "</table>"

        
        structuresHtml = "Related Structures:<br><table class=\"sortable\"><thead><tr>"
        structuresHtml += f"<td class=\"sort_a\" style=\"border: 1px solid gray;width: 200\">Name</td>"
        for stat in resource['relatedStats']:
            structuresHtml += f"<td style=\"border: 1px solid gray;width: 40\">{stat}</td>"
        structuresHtml += "</tr></thead>"
        storageTable = ""
        
        if 'storageStat' in resource:
            storageTable = "Storage Structures:<br><table class=\"sortable\"><thead><tr>"
            storageTable += f"<th class=\"sort_a\" style=\"border: 1px solid gray;width: 200\">Name</th>"
            storageTable += f"<th style=\"border: 1px solid gray;width: 40\">{resource['storageStat']}</th></tr></thead>"

        for (name, structure) in structures.items():
            if any(key in structure for key in resource['relatedStats']):
                structuresHtml += "<tr>"
                structuresHtml += f"<td style=\"border: 1px solid gray;width: 200\">{structure['name']}</td>"

                for stat in resource['relatedStats']:
                    structuresHtml += f"<td style=\"border: 1px solid gray;width: 40\">{structureValue(structure, stat)}</td>"

                resourceHtml += "</tr>"

            if 'storageStat' in resource and resource['storageStat'] in structure:
                storageTable += f"<tr><td style=\"border: 1px solid gray;width: 200\">{structure['name']}</td>"
                storageTable += f"<td style=\"border: 1px solid gray;width: 40\">{structureValue(structure, resource['storageStat'])}</td></tr>"
        
        structuresHtml += "</table><br><br>"    

        storageTable += "</table>"

        if resource['name'] == "Artifacts":
            commonArtiTable = "<h1>Common Artifacts</h1><br>General Pool<br><table class=\"sortable\"><thead><tr>"
            commonArtiTable += f"<th class=\"sorttable_nosort\" style=\"border: 1px solid gray;width: 200\">Image</th>"
            commonArtiTable += f"<th class=\"sort_a\" style=\"border: 1px solid gray;width: 200\">Name</th>"
            commonArtiTable += f"<th class=\"sorttable_nosort\" style=\"border: 1px solid gray\">Description</th>"
            commonArtiTable += f"<th style=\"border: 1px solid gray;width: 40\">Cost</th></tr></thead>"
            for commonArti in commonArtis:
                foundArtifact = {}
                for (name, artifact) in artifacts.items():
                    if name == commonArti['name']:
                        foundArtifact = artifact

                artiImg = imgPath + "artifacts/" + foundArtifact['img'] if 'img' in foundArtifact else artifactIcon    
                commonArtiTable += f"<tr><td style=\"border: 1px solid gray;width: 150\"><img src=\"{artiImg}\" width=\"150\"/></td>"
                commonArtiTable += f"<td style=\"border: 1px solid gray;width: 200\"><a href=\"../artifacts/{normalizeName(commonArti['name'])}.html\">{commonArti['name']}</a></td>"
                commonArtiTable += f"<td style=\"border: 1px solid gray\">{foundArtifact['desc'] if 'desc' in foundArtifact else ''}</td>"
                commonArtiTable += f"<td style=\"border: 1px solid gray;width: 40\">{commonArti['cost']}</td></tr>"

            commonArtiTable += "</table>"
            resourceHtml += commonArtiTable
                
        if 'usageTable' in resource and resource['usageTable']:
            resourceHtml += costTable
        resourceHtml += structuresHtml
        resourceHtml += storageTable

        async with aiofiles.open(outPath + f"resources/{normalizeName(resource['name'])}.html", "w") as file:
            await file.write(resourceHtml)

    async with aiofiles.open(outPath + "resources.html", "w") as file:
        await file.write(html)

asyncio.run(writeResources())

async def writeCouncil():
    html = "<head><link rel=\"stylesheet\" href=\"style.css\"></head><h2>Galactic Council</h2><br>"
    councilorLoreHtml = "<table><thead>"
    councilorLoreHtml += f"<th style=\"border: 1px solid black;width: 200\">Image</th>"
    councilorLoreHtml += f"<th style=\"border: 1px solid black;width: 100\">Name</th>"
    councilorLoreHtml += f"<th style=\"border: 1px solid black;width: 100\">Race</th>"
    councilorLoreHtml += f"<th style=\"border: 1px solid black;width: 200\">Description</th>"
    councilorLoreHtml += f"<th style=\"border: 1px solid black;width: 500\">Reward</th></thead>"
    for level in galacticCouncil:
        html += "Cost: " + level['influence'] + "<br>"
        toolLevel = { "influence": level['influence']}
        toolCouncilors = []
        if 'councilors' in level:
            for councilor in level['councilors']:
                reward = f"<a href=\"./artifacts/{normalizeName(councilor['reward'])}.html\">{councilor['reward']}</a>"
                if 'min' in councilor and 'max' in councilor:
                    reward += f" ({councilor['min']} - {councilor['max']})"
                if 'seasonal' in councilor:
                    reward += f" ({councilor['seasonal']} Seasonal Only)"
                html += councilor['shortName'] + " - " + councilor['rarity'] + ": " + reward
                html += "<br>"

                for (name, artifact) in artifacts.items():
                    if name == councilor['reward'] and 'desc' in artifact:
                        reward += f"<br>{artifact['desc']}"
                        break

                councilorLoreHtml += "<tr>"
                councilorLoreHtml += f"<td style=\"border: 1px solid gray;width: 200\"><img height=\"200\" src=\"{imgPath + councilor['img']}\"></td>"
                councilorLoreHtml += f"<td style=\"border: 1px solid gray;width: 200\">{councilor['name']}</td>"
                councilorLoreHtml += f"<td style=\"border: 1px solid gray;width: 200\">{councilor['race']}</td>"
                councilorLoreHtml += f"<td style=\"border: 1px solid gray\">{councilor['desc']}</td>"
                councilorLoreHtml += f"<td style=\"border: 1px solid gray;width: 200\">{reward}</td>"
                councilorLoreHtml += "</tr>"
                toolData = {"name":councilor['shortName'],"reward":reward, "rarity":councilor['rarity']}
                if 'seasonal' in councilor:
                    toolData['seasonal'] = councilor['seasonal']
                toolCouncilors.append(toolData)

            toolLevel["councilors"] = toolCouncilors
        if 'remove' in level:
            toolRemovals = []
            for councilor in level['remove']:
                found = False
                reward = ""
                for level in galacticCouncil:
                    if 'councilors' in level:
                        for rewardCouncilor in level['councilors']:
                            if rewardCouncilor['name'] == councilor:
                                html += "<b>Councilor Removed</b>: " + rewardCouncilor['shortName'] + " - " + rewardCouncilor['rarity'] + ": " + f"<a href=\"./artifacts/{normalizeName(rewardCouncilor['reward'])}.html\">{rewardCouncilor['reward']}</a><br>"
                                found = True
                                if 'min' in rewardCouncilor and 'max' in rewardCouncilor:
                                    html += f" ({rewardCouncilor['min']} - {rewardCouncilor['max']})"
                                toolRemovals.append(rewardCouncilor['shortName'])
                if not found:
                    print(f"Could not find removed councilor {councilor}")
            toolLevel['removals'] = toolRemovals

        councilToolData['levels'].append(toolLevel)

        html += "<br>"

    councilorLoreHtml += "</table>"

    async with aiofiles.open("config/counciltooldata.json", "w") as file:
        jsonString = json.dumps(councilToolData)
        await file.write(jsonString)

    async with aiofiles.open(outPath + "council.html", "w") as file:
        await file.write(html + councilorLoreHtml)

asyncio.run(writeCouncil())

async def writeBuildOrder():
    html = "<head><link rel=\"stylesheet\" href=\"style.css\"><style>body { background: none; background-color: black; }</style></head><h2>Build Order Cheat Sheet</h2><h3>Artifacts / abilities with a limit based on placed structure count</h3>"
    artifactsByCount = []
    for (name, artifact) in artifacts.items():
        if 'restrictions' in artifact:
            for restriction in artifact['restrictions']:
                if restriction['type'] == "Structure Count" and 'max' in restriction:
                    index = 0
                    for structure in artifactsByCount:
                        if structure[1] > restriction['max']:
                            break
                        index += 1
                    artifactsByCount.insert(index, (artifact, restriction['max']))
                            
    for artifact in artifactsByCount:
        html += f"<p><a href=\"./artifacts/{normalizeName(artifact[0]['name'])}.html\">{artifact[0]['name']}</a>: {artifact[0]['desc'].replace('<br>', ' ') if 'desc' in artifact else '(Missing Description)' }<br></p>"

    html += "<h3>Artifacts / abilities that require or are improved on a New Colony</h3>"

    needInvasion = []
    attackedNewColony = []
    for (name, artifact) in artifacts.items():
        if 'restrictions' in artifact:
            newColony = False
            invaded = False
            attacked = False
            for restriction in artifact['restrictions']:
                if restriction['type'] == "Development Status" and restriction['status'] == "New Colony":
                    newColony = True
                elif restriction['type'] == "Attacked Status" and restriction['status'] == "Recently Invaded":
                    invaded = True
                    needInvasion.append(artifact)
                elif restriction['type'] == "Attacked Status" and restriction['status'] == "Recently Attacked":
                    attacked = True
                    attackedNewColony.append(artifact)
        
            if newColony and not invaded and not attacked:
                html += f"<p><a href=\"./artifacts/{normalizeName(artifact['name'])}.html\">{artifact['name']}</a>: {artifact['desc'].replace('<br>', ' ') if 'desc' in artifact else '(Missing Description)' }<br></p>"
        elif 'planetEffectsConditional' in artifact:
            newColony = False
            invaded = False
            attacked = False
            for effect in artifact['planetEffectsConditional']:
                if 'conditions' in effect:
                    for condition in effect['conditions']:
                        if condition['type'] == "Development Status" and condition['status'] == "New Colony":
                            newColony = True
                        elif condition['type'] == "Attacked Status" and condition['status'] == "Recently Invaded":
                            invaded = True
                            needInvasion.append(artifact)
                        elif condition['type'] == "Attacked Status" and condition['status'] == "Recently Attacked":
                            attacked = True
                            attackedNewColony.append(artifact)
        
            if newColony and not invaded and not attacked:
                html += f"<p><a href=\"./artifacts/{normalizeName(artifact['name'])}.html\">{artifact['name']}</a>: {artifact['desc'].replace('<br>', ' ') if 'desc' in artifact else '(Missing Description)' }<br></p>"

    html += "<br><h3>Artifacts / abilities that require or are improved on a Recently Attacked New Colony</h3>"

    for artifact in attackedNewColony:
        html += f"<p><a href=\"./artifacts/{normalizeName(artifact['name'])}.html\">{artifact['name']}</a>: {artifact['desc'].replace('<br>', ' ') if 'desc' in artifact else '(Missing Description)' }<br></p>"

    html += "<br><h3>Artifacts / abilities that require or are improved on a planet with that has been invaded</h3>"
    for (name, artifact) in artifacts.items():
        if name == "Luring Cynosure":
            needInvasion.append(artifact)
    for artifact in needInvasion:
        html += f"<p><a href=\"./artifacts/{normalizeName(artifact['name'])}.html\">{artifact['name']}</a>: {artifact['desc'].replace('<br>', ' ') if 'desc' in artifact else '(Missing Description)' }<br></p>"

    html += "<br><h3>Artifacts / abilities that require or are improved on a planet with a Recently Attacked status</h3>"

    for (name, artifact) in artifacts.items():
        if 'restrictions' in artifact:
            for restriction in artifact['restrictions']:
                if restriction['type'] == "Calm" and 'max' in restriction:
                    html += f"<p><a href=\"./artifacts/{normalizeName(artifact['name'])}.html\">{artifact['name']}</a>: {artifact['desc'].replace('<br>', ' ') if 'desc' in artifact else '(Missing Description)' }<br></p>"

    html += "<br><h3>Artifacts / abilities that require or are improved on a planet with a other scanners</h3>"

    for (name, artifact) in artifacts.items():
        if 'restrictions' in artifact:
            for restriction in artifact['restrictions']:
                if restriction['type'] == "Other Scanners" and 'min' in restriction:
                    html += f"<p><a href=\"./artifacts/{normalizeName(artifact['name'])}.html\">{artifact['name']}</a> ({restriction['min']}): {artifact['desc'].replace('<br>', ' ') if 'desc' in artifact else '(Missing Description)' }<br></p>"
        if 'planetEffectsConditional' in artifact:
                for effect in artifact['planetEffectsConditional']:
                    if 'conditions' in effect:
                        match = False
                        for condition in effect['conditions']:
                            if condition['type'] == "Other Scanners" and 'min' in condition:
                                html += f"<p><a href=\"./artifacts/{normalizeName(artifact['name'])}.html\">{artifact['name']}</a> ({condition['min']}): {artifact['desc'].replace('<br>', ' ') if 'desc' in artifact else '(Missing Description)' }<br></p>"
                                
    html += "<br><h3>Starter Charters (these may have other restrictions):</h3>"

    for charter in startCharters:
        html += f"<p><a href=\"/artifacts/{normalizeName(charter['name'])}.html\">{charter['name']}</a>: {charter['desc'].replace('<br>', ' ') if 'desc' in charter else '(Missing Description)'}<br></p>"

    html += "<br><h3>Artifacts / abilities that require or are improved on a planet with a max resource availability of Extremely Abundant or less:</h3>"
    for (name, artifact) in artifacts.items():
        if 'restrictions' in artifact:
            for restriction in artifact['restrictions']:
                if restriction['type'] == "Resource Availability" and 'max' in restriction and restriction['max'] == "EA":
                    html += f"<p><a href=\"./artifacts/{normalizeName(artifact['name'])}.html\">{artifact['name']}</a>: {artifact['desc'].replace('<br>', ' ') if 'desc' in artifact else '(Missing Description)' }<br></p>"

    html += "<br><h3>Artifacts / abilities that require or are improved on a planet with a max resource availability of Rich or less:</h3>"
    for (name, artifact) in artifacts.items():
        if 'restrictions' in artifact:
            for restriction in artifact['restrictions']:
                if restriction['type'] == "Resource Availability" and 'max' in restriction and restriction['max'] == "R":
                    html += f"<p><a href=\"./artifacts/{normalizeName(artifact['name'])}.html\">{artifact['name']}</a>: {artifact['desc'].replace('<br>', ' ') if 'desc' in artifact else '(Missing Description)' }<br></p>"

    html += "<br><h3>Artifacts / abilities that are improved by having an existing structure:</h3>"
    for (name, artifact) in artifacts.items():
        if 'planetEffectsConditional' in artifact:
            for effect in artifact['planetEffectsConditional']:
                if 'conditions' in effect:
                    for condition in effect['conditions']:
                        if condition['type'] == 'Existing Structures':
                            html += f"<p><a href=\"./artifacts/{normalizeName(artifact['name'])}.html\">{artifact['name']}</a>: {artifact['desc'].replace('<br>', ' ')}<br></p>"

    html += "<br><h3>Artifacts / abilities that require or are improved on a planet of a max size</h3>"
    for (name, size) in planetSizes.items():
        
        html += f"<h3>Max size: {size['name']}</h3>"
        for (name, artifact) in artifacts.items():
            if 'planetEffectsConditional' in artifact:
                for effect in artifact['planetEffectsConditional']:
                    if 'conditions' in effect:
                        match = False
                        for condition in effect['conditions']:
                            if condition['type'] == "Size" and ('max' in condition and condition['max'] == size['name']) or ('size' in condition and condition['size'] == size['name']):
                                html += f"<p><a href=\"./artifacts/{normalizeName(artifact['name'])}.html\">{artifact['name']}</a>: {artifact['desc'].replace('<br>', ' ') if 'desc' in artifact else '(Missing Description)' }<br></p>"
                                match = True
                                break
                        if match:
                            break
            if 'restrictions' in artifact:
                for restriction in artifact['restrictions']:
                    if restriction['type'] == "Size" and ('max' in restriction and restriction['max'] == size['name']) or ('size' in restriction and restriction['size'] == size['name']):
                        html += f"<p><a href=\"./artifacts/{normalizeName(artifact['name'])}.html\">{artifact['name']}</a>: {artifact['desc'].replace('<br>', ' ') if 'desc' in artifact else '(Missing Description)' }<br></p>"
                        break

        for (name, structure) in structures.items():
            if 'ability' in structure and 'restrictions' in structure['ability']:
                for restriction in structure['ability']['restrictions']:
                    if restriction['type'] == "Size" and ('max' in restriction and restriction['max'] == size['name']):
                        html += "<p>Structure ability: " + structure['name'] + "<br></p>"
                        break

        html += "<br>"

    async with aiofiles.open(outPath + "build_order.html", "w") as file:
        await file.write(html)

asyncio.run(writeBuildOrder())

async def writeGiveaways():      
    html = "<head><link rel=\"stylesheet\" href=\"style.css\"><script type=\"text/javascript\" charset=\"utf8\" src=\"../sorttable.js\" defer></script></head><table class=\"sortable\"><thead><tr>"
    html += f"<th class=\"sorttable_nosort\" style=\"border: 1px solid gray;width: 200\">Date</th>"
    html += f"<th class=\"sort_a\" style=\"border: 1px solid gray;width: 200\">Name</th>"
    html += f"<th class=\"sorttable_nosort\" style=\"border: 1px solid gray\">Description</th>"
    html += f"<th class=\"sort_a\" style=\"border: 1px solid gray;width: 200\">Reward</th></thead>"
    for giveaway in giveaways:
        html += "<tr>"
        html += f"<td style=\"border: 1px solid gray;width: 200\">{giveaway['date']}</td>"
        html += f"<td style=\"border: 1px solid gray;width: 200\">{giveaway['name']}</td>"
        html += f"<td style=\"border: 1px solid gray\">{giveaway['desc']}</td>"
        html += f"<td style=\"border: 1px solid gray;width: 200\"><a href=\"./artifacts/{normalizeName(giveaway['reward'])}.html\">{giveaway['reward']}</a></td>"
        html += "</tr>"
    html += "</table>"

    async with aiofiles.open(outPath + "giveaways.html", "w") as file:
        await file.write(html)

asyncio.run(writeGiveaways())

raceTable = "<head><link rel=\"stylesheet\" href=\"style.css\"></head>"

for (name, race) in races.items():
    raceTable += f"<tr><td style=\"border: 1px solid gray;\"><a href=\"./races/{race['name']}.html\">{race['name']}</td><td style=\"border: 1px solid gray;\"><img src=\"{imgPath}aliens/{race['images'][0]}\" width=\"200\"></td><td style=\"border: 1px solid gray;\">{race['bonus']}</td></tr>"
    with open(outPath + "races/" + race['name'] + ".html", "w") as outFile:
        outFile.write(f"<head><link rel=\"stylesheet\" href=\"../style.css\"></head><b>{race['name']}</b><br>{race['lore']}<br>{race['bonus']}<br><table><tr>")

        imageCount = 0
        for image in race['images']:
            
            if imageCount > 0 and imageCount % 5 == 0:
                outFile.write("</tr><tr>")
            imageCount += 1
            outFile.write(f"<td style=\"border: 1px solid gray;\"><img src=\"{imgPath}aliens/{image}\" width=\"200\"></img></td>")

        outFile.write("</tr></table>")

        for design in designs:
            if design['name'] == race['name']:
                outFile.write(f"<img src=\"{imgPath}{design['img']}\" width=\"400\"/>")
        
        if 'legionMedals' in race:
            legionMedalsHtml = "<br>Help Legion Members and Friends:<br>" + generateMedalTableHeader()
            for medal in race['legionMedals']:
                legionMedalsHtml += generateMedalRow(medal)

            outFile.write(f"{legionMedalsHtml}</table>")

        outFile.write(f"<br><td style=\"border: 1px solid gray;\"><img src=\"{imgPath}aliens/{race['oldImg']}\" width=\"200\"></img></td>")


with open(outPath + "races.html", "w") as file:
    file.write(f"<table>{raceTable}</table>")


medalDesignsTable = ""
artifactDesignsTable = ""
moduleDesignsTable = ""
raceDesignsTable = ""

def addRowHtml(table, design):
        table += "<tr>"
        table += "<td style=\"border: 1px solid gray;\">" + design['name'] + "</td>"
        table += f"<td style=\"border: 1px solid gray;\"><img src=\"{imgPath}" + design['img'] + "\" width=\"200\"></img></td>"
        return table
    
for design in designs:

    if 'raceDefault' in design and design['raceDefault'] == "Yes":
        raceDesignsTable = addRowHtml(raceDesignsTable, design)
        raceDesignsTable += f"<td style=\"border: 1px solid gray;\"><a href=\"./races/{design['name']}.html\">{design['name']}</href></td>"
    else:
        found = False
        for medal in medals:
            if 'design' in medal:
                if medal['design'] == design['name']:
                    medalDesignsTable = addRowHtml(medalDesignsTable, design)
                    medalPage = normalizeName(medal['name'])
                    medalDesignsTable += f"<td style=\"border: 1px solid gray;\"><a href=\"./medals/{medalPage}.html\">{medal['name']}</href></td>"
                    found = True
                    break

        if not found:
            for (name, artifact) in artifacts.items():
                if 'playerEffectsRandom' in artifact:
                    effects = artifact['playerEffectsRandom']
                    for effect in effects:
                        if 'type' in effect and effect['type'] == "Apply Design" and effect['design'] == design['name']:
                            artifactDesignsTable = addRowHtml(artifactDesignsTable, design)
                            artifactPage = normalizeName(artifact['name'])
                            artifactDesignsTable += f"<td style=\"border: 1px solid gray;\"><a href=\"./artifacts/{artifactPage}.html\">{artifact['name']}</href></td>"
                            found = True
                            break

        if not found:
            for (name, artifact) in artifacts.items():
                if 'playerEffects' in artifact:
                    effects = artifact['playerEffects']
                    for effect in effects:
                        if 'type' in effect and effect['type'] == "Apply Design" and effect['design'] == design['name']:
                            artifactDesignsTable = addRowHtml(artifactDesignsTable, design)
                            artifactPage = normalizeName(artifact['name'])
                            artifactDesignsTable += f"<td style=\"border: 1px solid gray;\"><a href=\"./artifacts/{artifactPage}.html\">{artifact['name']}</href></td>"
                            found = True
                            break


        if not found:
            for (name, module) in modules.items():
                if 'playerEffects' in module:
                    effects = module['playerEffects']
                    for effect in effects:
                        if effect['type'] == "Apply Design" and effect['design'] == design['name']:
                            moduleDesignsTable = addRowHtml(moduleDesignsTable, design)
                            modulePage = normalizeName(module['name'])
                            moduleDesignsTable += f"<td style=\"border: 1px solid gray;\"><a href=\"./artifacts/{modulePage}.html\">{module['name']}</href></td>"
                            found = True
                            break

        if not found:
            print(f"Missing Design Source: {design['name']}")
    
with open(outPath + "designs.html", "w") as output:
    output.write(f"<head><link rel=\"stylesheet\" href=\"style.css\"></head><h3>Race designs</h3>\n<table>{raceDesignsTable}</table><br><br><h3>Medal designs<h3><br><table>{medalDesignsTable}</table><br><br><h3>Artifact-induced designs</h3><br><table>{artifactDesignsTable}</table><br><br><h3>Module designs</h3><br><table>{moduleDesignsTable}</table")
    
""" with open("./othermedals.txt", "r") as file:
    otherMedals = file.read()
    lines = otherMedals.splitlines()
    names = []
    prevEmpty = False
    for line in lines:
        if line == "":
            prevEmpty = True
            continue
        if prevEmpty:
             names.append(line)
             prevEmpty = False

    for name in names:
        found = False
        for medal in medals:
            if medal['name'] == name:
                found = True
                break
        if not found:
            print(name) """


updates = {}
with open(configPath + "updates.json", "r") as file:
    updates = json.load(file)

html = "<head><link rel=\"stylesheet\" href=\"style.css\"></head><table>"
for update in updates:
    html += "<tr>"
    typeCell = update['type']
    if update['type'] == "Forum" or update['type'] == "Forum (Krytan)" or update['type'] == "Forum (MrSpock)":
        typeCell = f"<img src=\"{imgPath}icons/galaxypoints.png\" width=\"30\"/>"
    elif update['type'] == "Discord":
        typeCell = "<img src=\"https://cdn.prod.website-files.com/6257adef93867e50d84d30e2/66e3d80db9971f10a9757c99_Symbol.svg\" width=\"30\"/>"
    elif update['type'] == "Event":
        typeCell = "<svg xmlns=\"http://www.w3.org/2000/svg\" width=\"14\" height=\"14\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"#38bdf8\" stroke-width=\"2\" stroke-linecap=\"round\" stroke-linejoin=\"round\"><circle cx=\"12\" cy=\"12\" r=\"5\"></circle><line x1=\"12\" y1=\"1\" x2=\"12\" y2=\"3\"></line><line x1=\"12\" y1=\"21\" x2=\"12\" y2=\"23\"></line><line x1=\"4.22\" y1=\"4.22\" x2=\"5.64\" y2=\"5.64\"></line><line x1=\"18.36\" y1=\"18.36\" x2=\"19.78\" y2=\"19.78\"></line><line x1=\"1\" y1=\"12\" x2=\"3\" y2=\"12\"></line><line x1=\"21\" y1=\"12\" x2=\"23\" y2=\"12\"></line><line x1=\"4.22\" y1=\"19.78\" x2=\"5.64\" y2=\"18.36\"></line><line x1=\"18.36\" y1=\"5.64\" x2=\"19.78\" y2=\"4.22\"></line></svg>"
    elif update['type'] == "Cosmetic":
        typeCell = "<svg xmlns=\"http://www.w3.org/2000/svg\" width=\"14\" height=\"14\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"#a78bfa\" stroke-width=\"2\" stroke-linecap=\"round\" stroke-linejoin=\"round\"><rect x=\"3\" y=\"3\" width=\"18\" height=\"18\" rx=\"2\" ry=\"2\"></rect><circle cx=\"8.5\" cy=\"8.5\" r=\"1.5\"></circle><polyline points=\"21 15 16 10 5 21\"></polyline></svg>"
    elif update['type'] == "Tweak":
        typeCell = "<svg xmlns=\"http://www.w3.org/2000/svg\" width=\"14\" height=\"14\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"#94a3b8\" stroke-width=\"2\" stroke-linecap=\"round\" stroke-linejoin=\"round\"><circle cx=\"12\" cy=\"12\" r=\"3\"></circle><path d=\"M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1 0 2.83 2 2 0 0 1-2.83 0l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-2 2 2 2 0 0 1-2-2v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83 0 2 2 0 0 1 0-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1-2-2 2 2 0 0 1 2-2h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 0-2.83 2 2 0 0 1 2.83 0l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 2-2 2 2 0 0 1 2 2v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 0 2 2 0 0 1 0 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 2 2 2 2 0 0 1-2 2h-.09a1.65 1.65 0 0 0-1.51 1z\"></path></svg>"
    elif update['type'] == "Feature":
        typeCell = "<svg xmlns=\"http://www.w3.org/2000/svg\" width=\"14\" height=\"14\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"#4ade80\" stroke-width=\"2\" stroke-linecap=\"round\" stroke-linejoin=\"round\"><polygon points=\"12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2\"></polygon></svg>"
    elif update['type'] == "Maintenance":
        typeCell = "<svg xmlns=\"http://www.w3.org/2000/svg\" width=\"14\" height=\"14\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"#f97316\" stroke-width=\"2\" stroke-linecap=\"round\" stroke-linejoin=\"round\"><path d=\"M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z\"></path></svg>"
    elif update['type'] == "Initiative":
        typeCell = "<svg xmlns=\"http://www.w3.org/2000/svg\" width=\"14\" height=\"14\" viewBox=\"-2 -2 28 28\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"1.8\" stroke-linecap=\"round\" stroke-linejoin=\"round\"><g transform=\"rotate(30 12 9)\"><rect x=\"7\" y=\"2\" width=\"10\" height=\"12\" rx=\"1.5\"></rect><polyline points=\"9.5 8 11 10 14.5 5.5\"></polyline></g><path d=\"M3 17h18v3c0 1.1-.9 2-2 2H5c-1.1 0-2-.9-2-2v-3z\"></path></svg>"
    elif update['type'] == "Gift":
        typeCell = "<svg xmlns=\"http://www.w3.org/2000/svg\" width=\"14\" height=\"14\" viewBox=\"0 0 24 24\" fill=\"currentColor\"><path d=\"M20 6h-2.18c.11-.31.18-.65.18-1 0-1.66-1.34-3-3-3-1.05 0-1.96.54-2.5 1.35l-.5.67-.5-.68C10.96 2.54 10.05 2 9 2 7.34 2 6 3.34 6 5c0 .35.07.69.18 1H4c-1.11 0-1.99.89-1.99 2L2 19c0 1.11.89 2 2 2h16c1.11 0 2-.89 2-2V8c0-1.11-.89-2-2-2zm-5-2c.55 0 1 .45 1 1s-.45 1-1 1-1-.45-1-1 .45-1 1-1zM9 4c.55 0 1 .45 1 1s-.45 1-1 1-1-.45-1-1 .45-1 1-1zm11 15H4v-2h16v2zm0-5H4V8h5.08L7 10.83 8.62 12 11 8.76l1-1.36 1 1.36L15.38 12 17 10.83 14.92 8H20v6z\"></path></svg>"
    
    html += f"<td style=\"border: 1px solid gray;width: 30;padding: 10;\">{typeCell}</td>"
    html += f"<td style=\"border: 1px solid gray;width: 100;padding: 10;\">{update['date']}</td>"
    html +=  f"<td style=\"border: 1px solid gray;width: 200;padding: 10;\">{update['desc']}</td>"
    html +=  "</tr>"
html +=  "</table>"

with open(outPath + "updates.html", "w") as file:
    file.write(html)

validTargets = [
    "Base",
    "Enemy Base",
    "Enemy Planet",
    "Enemy Ship",
    "Friend",
    "Mission",
    "Planet",
    "Player",
    "Your Planet",
    "None"
]
artifactTable = {}

for target in validTargets:
    artifactTable[target] = []


html = "<head><link rel=\"stylesheet\" href=\"style.css\"><script type=\"text/javascript\" charset=\"utf8\" src=\"../sorttable.js\" defer></script></head><table class=\"sortable\"><thead><tr>"
html += f"<th class=\"sorttable_nosort\" style=\"border: 1px solid gray;width: 150\">Image</th>"
html += f"<th class=\"sort_a\" style=\"border: 1px solid gray;width: 200\">Name</th>"
html += f"<th class=\"sorttable_nosort\" style=\"border: 1px solid gray\">Description</th></tr></thead>"
for (name, artifact) in artifacts.items():
    img = imgPath + "/artifacts/" + artifact['img'] if 'img' in artifact else artifactIcon
    if 'target' not in artifact or artifact['target'] not in validTargets:
        raise Exception(f"Artifact: \"{artifact['name']}\" has invalid target")
    artiHtml = "<head><link rel=\"stylesheet\" href=\"../style.css\"></head>" + artifact['name'] + "<br>"
    
    artiHtml += f"<img src=\"{img}\"/><br><br>"
    artiHtml += f"Target: {artifact['target']}<br><br>"
    artiHtml += artifact['desc'] + "<br>" if 'desc' in artifact else "<br><br>"
    if 'cost' in artifact:
        artiHtml += "Cost:<br>"
        for key in artifact['cost']:
            artiHtml += str(key) + ": " + artifact['cost'][key] + "<br>"
        artiHtml += "<br>"

    if 'scrap' in artifact:
        typeStr = "CTP" if artifact['scrap']['type'] == "ctp" else "Credits" if artifact['scrap']['type'] == "cr" else "Relic Badges" if artifact['scrap']['type'] == "relic" else "EM"
        artiHtml += f"Scrap: {artifact['scrap']['min']} - {artifact['scrap']['max']} {icons(artifact['scrap']['type'])}<br><br>"

    artiHtml += "<h2>How to Obtain:</h2>"
    
    if artifact['sources']['medals'].__len__() > 0:
        artiHtml += generateMedalTableHeader(False)
        for sourceMedal in artifact['sources']['medals']:
            artiHtml += generateMedalRow(sourceMedal, "../medals", False)
        artiHtml += "</table><br>"

    if artifact['sources']['legionMissions'].__len__() > 0:
        artiHtml += "<h3>Legion Mission Tasks</h3>"
        for task in artifact['sources']['legionMissions']:
            artiHtml += f"{task[0]['name']}: {task[1]['name']}<br>"

    if 'restrictions' in artifact:
        eligibleArtifacts = []
        for restriction in artifact['restrictions']:
            if restriction['type'] == "Existing Structures" and 'tags' in restriction:
                for tag in restriction['tags']:
                    for potentialArtifact in artifacts:
                        if 'planetEffects' in potentialArtifact:
                            eligible = False
                            for effect in potentialArtifact['planetEffects']:
                                if effect['type'] == "Construct Structure" and 'tags' in potentialArtifact and tag in potentialArtifact['tags']:
                                    eligibleArtifacts.append(potentialArtifact)
                                    eligible = True
                                    break
                artiHtml += "Eligible Artifacts:<br>"
                for eligibleArtifact in eligibleArtifacts:
                    artiHtml += eligibleArtifact['name'] + "<br>"
                artiHtml += "<br>"

    with open(outPath + f"artifacts/{normalizeName(artifact['name'])}.html", "w") as file:
        file.write(artiHtml)     
    
    html += "<tr>"
    html += f"<td style=\"border: 1px solid gray;width: 150\"><img src=\"{img}\" width=\"200\"/></td>"
    html += f"<td style=\"border: 1px solid gray;width: 200\"><a href=\"./artifacts/{normalizeName(artifact['name'])}.html\">{artifact['name']}</a></td>"
    descString = artifact['desc'] if 'desc' in artifact else ""
    html += f"<td style=\"border: 1px solid gray\">{descString}</td>"
    html += "</tr>"

print(f"{artifacts.__len__()}")
html += "</table>"
with open(outPath + "artifacts.html", "w") as file:
    file.write(html)

async def writeHeaderPage():
    headerHtml = '''<head><link rel=\"stylesheet\" href=\"../style.css\"></head>
                        <h2>Header</h2>
                        <img src="../assets/header.png"><br>
                        
                        This header displays at the top of the page regardless of your current tab. It displays the following information:<br><br>
                        Your player name, which links to your ship stats<br>
                        Your player ID<br>
                        The game version<br>
                        The Galactic Server Time, which matches the UTC time zone<br>
                        Your current <a href="../designs.html">Ship Design</a>, which links to the <a href="shiptab.html">Ship</a> tab<br>
                        Your current and maximum <a href="../stats/energy.html">Energy</a> and a filling circle depicting your <a href="../stats/energyrecharge.html">Energy Recharge</a><br>
                        Your current and maximum <a href="../stats/hull.html">Hull</a><br>
                        Your current and maximum <a href="../stats/shield.html">Shield</a> and a filling circle depicting your <a href="../stats/shieldrecharge.html">Shield Recharge</a><br>
                        Your current <a href="../races.html">Race</a> image, which links to the <a href="evolutiontab.html">Evolution Tree</a> tab. If this is flashing green, then Genes are available to collect<br>
                        Your <a href="../stats/ranks.html>Rank</a> insignia and number<br>
                        Your current <a href="materials/gp.html>Galaxy Point</a> balance<br>
                        The <a href="music.html">Music</a> menu<br>
                        The <a href="account.html">Account</a> menu<br>
                        Your current <a href="../materials/genes.html">Genes</a> amount, which links to the <a href="evolutiontab.html">Evolution Tree</a> tab<br>
                        Your current <a href="../resources/research.html">Research</a> amount, which links to the <a href="researchtab.html">Research</a> tab<br>
                        Your current <a href="../resources/influence.html">Influence</a> amount, which links to the <a href="influencetab.html">Influence</a> tab<br>
                        The Redeem button, which accesses the <a href="../markets/artifactmarket.html">Artifact</a> Market<br>
                        Your current <a href="../materials/credits.html">Credits</a> value<br>
                        
                        <h3>Energy Bar</h3>
                        Hovering over the Energy bar displays current vs max Energy, Energy Charge Rate, and time until you receive another point of Energy<br>
                        Clicking on the Energy bar displays a pop-up with your max and current energy, your current charge rate, and the sources of you max energy.<br>
                        <img src="../assets/energypopup.png">

                        <h3>Hull Bar</h3>
                        Hovering over the Hull bar displays current vs max Hull.<br>
                        Clicking on the Hull bar displays a pop-up with max and current energy, along with your base hull and various bonuses.<br>
                        <img src="../assets/hullpopup.png">

                        <h3>Shield Pop-Up</h3>
                        Hovering over the Shield bar displays current vs max Shield and Shield Charge Rate.<br>
                        Clicking on the Shield bar displays a pop-up with max and current shield level, your current shield charge rate, and your base shield and various bonuses.<br>
                        <img src="../assets/shieldpopup.png">

                        <h3>Rank Area</h3>
                        Hovering over the XP bar displays experience needed to reach the next rank.<br>
                        Clicking on your rank, rank insignia, or experience bar displays a pop-up with your rank insignia, rank, experience progress, experience needed to reach the next rank, and total experience earned.<br>
                        <img src="../assets/rankpopup.png">

                        <h3>Galaxy Points Pop-Up</h3>
                        Clicking on the Galaxy Points displays a pop-up with various GP purchase options.<br>
                        <img src="../assets/gppopup.png">

                        <h3>Genes</h3>
                        Hovering over the Genes displays your current Genes amount and the time until you can Grow Genes.

                        <h3>Research</h3>
                        Hovering over Research will display your current Research amount and the time until you receive more Research.

                        <h3>Influence</h3>
                        Hovering over Influence will display your current Influence amount and the time until you receive more Influence.

                        <h3>Credits</h3>
                        Hovering over Credits will display your current Credits.

                    '''
    async with aiofiles.open(outPath + "interface/header.html", "w") as file:
        await file.write(headerHtml)

asyncio.run(writeHeaderPage())

async def writeNewsTab():

    newsTabHtml =   '''<head><link rel=\"stylesheet\" href=\"../style.css\"></head>
                        <h2>News Tab</h2>
                        Access this tab by clicking the button the image below<br>
                        <img src="../assets/newstabbutton.png"><br>
                        
                        This tab displays general game information<br>
                        <img src="../assets/newstab.png"><br><br>

                        The <a href="../actions/dailyreward.html">Daily Reward</a> button<br>
                        The <a href="../actions/supporterbonus.html">Supporter Bonus</a> button<br>
                        The <a href="../materials/gp.html">Galaxy Points</a> purchase button<br>
                        The <a href="../markets/artifactmarket.html">Artifact</a> Market button<br>
                        The Seasonal Events Schedule button<br>
                        The active Seasonal Event banners (if any Seasonal Events are active)<br>
                        A link to Galaxy Legion: Apotheosis, the sequel game<br>
                        A button to view all game updates<br>
                        A section to view the most recent updates<br>
                        The Galactic Voting button, which accesses Initiatives<br>
                        The current Legion Announcement, where Legion leaders can post important updates<br>
                        The Ship's Log, which includes many types of messages about your game<br>

                        <h3>Galaxy Points Pop-Up</h3>
                        Clicking on the Galaxy Points displays a pop-up with various GP purchase options.<br>
                        <img src="../assets/gppopup.png">

                        <h3>Seasonal Events Schedule Pop-Up</h3>
                        Clicking on the Schedule button displays a pop-up with the Seasonal Events schedule. This schedule lists the various Seasonal Events in the game, along with their timeframes. In addition, hovering over the icons can give more information about the features available during that Seasonal Event.<br>
                        <img src="../assets/seasonaleventsschedulepopup.png">

                        <h3>Seasonal Banners</h3>
                        You can expand these banners by clicking on them, which reveals more information about the Event.

                        <h3>Updates</h3>
                        This button displays the full list of game updates. Some updates have more lengthy information associated, which you can see by clicking on the updates. Further, you can click on any updates indicating a passing Initiative to see more information about the effect.<br>
                        <img src="../assets/gameupdatespopup.png">

                        <h3>Ship's Log</h3>
                        This log contains various filter buttons. Click these buttons at the top to filter the type of messages seen.
                    '''

    async with aiofiles.open(outPath + "interface/news.html", "w") as file:
        await file.write(newsTabHtml)

asyncio.run(writeNewsTab())

async def writeShipTab():

    shipHtml =  '''
                <head><link rel=\"stylesheet\" href=\"../style.css\"></head>
                <h2>Ship Tab</h2>
                Access this tab either by clicking the Ship tab button or by clicking on your ship design in the header<br>
                <img src="../assets/shiptabbutton.png"><img src="../assets/shiptabbutton2.png"><br><br>

                This tab shows information about your ship<br>
                <img src="../assets/shiptab.png"><br><br>

                This tab displays the following information:<br>
                Your <a href="../shipstats/size.html">Ship Size (Space)</a> stat<br>
                Your <a href="../shipstats/attack.html">Attack</a> stat<br>
                Your <a href="../shipstats/defense.html">Defense</a> stat<br>
                Your <a href="../shipstats/scan.html">Scan</a> stat<br>
                Your <a href="../shipstats/cloak.html">Cloak</a> stat<br>
                Your <a href="../shipstats/cargo.html">Cargo</a> stat<br>
                Your <a href="../shipstats/upkeep.html">Upkeep</a><br>
                Your <a href="../races.html">Race</a><br>
                Your <a href="../professions.html">Profession</a><br>
                The <a href="shipstats.html">Ship Stats</a> button<br>
                The <a href="../medals_sorted.html">Medals</a> button<br>
                The <a href="../actions/repairship.html">Repair Ship</a> button<br>
                The <a href="../artifacts.html">Artifacts</a> button<br>
                The <a href="../abilities.html">Abilities</a> button<br>
                The <a href="settingswindow.html">Settings</a> button<br>
                The ship display

                <h3>Space Pop-Up</h3>
                Clicking your Space stat will show your space used vs your ship size, your size class, and any modifiers to your ship size.<br>
                <img src="../assets/shipspacepopup.png">

                <h3>Attack Pop-Up</h3>
                Clicking your Attack stat will show your total attack, attack from crew, attack from modules, and any modifiers to your attack.<br>
                <img src="../assets/shipattackpopup.png">

                <h3>Defense Pop-Up</h3>
                Clicking your Defense stat will show your total defense, defense from crew, defense from modules, and any modifiers to your defense.<br>
                <img src="../assets/shipdefensepopup.png">

                <h3>Scan Pop-Up</h3>
                Clicking your Scan stat will show your total scan, scan from modules, and any modifiers to your scan.<br>
                <img src="../assets/shipscanpopup.png">

                <h3>Cloak Pop-Up</h3>
                Clicking your Cloak stat will show your total cloak, cloak from modules, and any modifiers to your cloak.<br>
                <img src="../assets/shipcloakpopup.png">

                <h3>Cargo Pop-Up</h3>
                Clicking your Cargo stat will show your used cargo space vs max cargo space, cargo space installed on your ship, and any modifiers to your cargo space.<br>
                <img src="../assets/shipcargopopup.png">

                <h3>Upkeep Pop-Up</h3>
                Clicking your Upkeep stat will your total upkeep, time until your upkeep is due, and any modifiers to your upkeep.<br>
                <img src="../assets/shipupkeepopup.png">

                <h3>Race Pop-Up</h3>
                Clicking your Race image will show your current race, its bonus, and its description.<br>
                <img src="../assets/racepopup.png">

                <h3>Profession Pop-Up</h3>
                Clicking your Profession will show your current profession, its bonus, and its description.<br>
                <img src="../assets/professionpopup.png">

                <h3>Ship Stats Window</h3>
                <a href="shipstats.html">More Information</a><br>
                <img src="../assets/shipstatswindow.png">

                <h3>Medals Window</h3>
                This window displays your medals and accumulated medal points.
                <img src="../assets/medalswindow.png">

                <h3>Abilities Window</h3>
                This window displays your abilities. Here, you can only use abilities that don't require a specific target, like a specific planet or NPC.<br>
                <img src="../assets/abilitieswindow.png">

                <h3>Settings Window</h3>
                This window displays your <a href="../actions/settings.html">Player Settings</a>.<br>
                <img src="../assets/settingswindow.png">

                <h3>Ship Display</h3>
                You can expand the various sections to see ship crew and size, modules, and allies. In the Ship Crew & Size, you can spend Rank points. In the modules sections, you can install various standard modules, sell modules, use modules abilities, or uninstall / reinstall modules.<br>
                <img src="../assets/shipdisplay.png">

                '''

    async with aiofiles.open(outPath + "interface/ship.html", "w") as file:
        await file.write(shipHtml)
        
asyncio.run(writeShipTab())

async def writeShipStatsWindow():
    html =  '''
            <head><link rel=\"stylesheet\" href=\"../style.css\"></head>
            <h2>Ship Stats Window</h2>
            You can access this window from the <a href="ship.html">Ship</a> tab<br>
            <img src="../assets/shipstatswindow.png"><br><br>

            This window displays:<br>
            A player display area<br>
            A <a href="../playerstats.html">Player Stats</a> tab<br>
            A Ship tab<br>
            An Actions tab<br>
            Your player comm<br>
            Your Effects tab<br>

            <h3>Player Display</h3>
            The area at the top of this window shows your ship, fighters, name, title, rank, race, profession, and Legion<br>
            <img src="../assets/playerdisplay.png">

            <h3>Actions Tab</h3>
            Here you can access the Abilities and Medals windows.<br>
            <img src="../assets/abilitieswindow.png"><br>
            <img src="../assets/medalswindow.png">

            <h3>Comm Tab</h3>
            On this tab, you can see messages sent to you by other players. You can then delete each message, block the sender, or reply to the sender.<br>
            <img src="../assets/playercomm.png">

            '''
    
    async with aiofiles.open(outPath + "interface/shipstats.html", "w") as file:
        await file.write(html)

asyncio.run(writeShipStatsWindow())

async def writeSettingsWindow():
    html =  '''
            <head><link rel=\"stylesheet\" href=\"../style.css\"></head>
            <h2>Settings Window</h2>
            You can access this window from the <a href="ship.html">Ship</a> tab<br>
            <img src="../assets/settingswindow.png"><br><br>

            This window displays:<br>
            A Miscellaneous Settings Tab<br>
            A Titles and Ships Tab<br>
            A Flairs Tab<br>
            Remember to click Save Settings at the bottom when you are done!

            <h3>Misc Tab</h3>
            This tab contains a variety of settings, including: background animation, alerts, and button styles. In addition, this tab contains the Tutorial.<br>

            <h3>Titles and Ships Tab</h3>
            This tab allows you to select from the Titles and <a href="../designs.html">Designs</a> that you've unlocked.

            <h3>Flairs Tab</h3>
            This tab allows you to select from <a href="../flairs.html">Flairs</a> that you've unlocked.<br><br>

            You can unlock more Designs, Titles, and Flairs by earning <a href="../medals_sorted.html">Medals</a><br>
            You can test out different Designs, Titles, and Flairs with the <a href="../design_fun.html">Fun with Designs!</a> page.
            '''
    
    async with aiofiles.open(outPath + "interface/settingswindow.html", "w") as file:
        await file.write(html)

asyncio.run(writeSettingsWindow())

async def writePlanetsTab():
    html =  '''
            <head><link rel=\"stylesheet\" href=\"../style.css\"></head>
            <h2>Planets Tab</h2>
            You can access this tab with the button below.<br>
            <ing src="../assets/planetstabbutton.png"><br><br>

            This tab displays the following:<br>
            The <a href="../actions/scan.html">Scan Planets</a> button<br>
            The planet that you are currently <a href="../actions/guard.html">Guarding</a>, if you are doing so<br>
            The various filters for planets, such as your planets or enemy planets<br>
            The planet text filter<br>
            The list of planets that currently match this filter<br>
            Icons on planets indicating the owner: you, a player in your Legion, or a player in another Legion<br>
            The planet quick action button, which allows you to quickly use probes or purgers on planets<br>

            <h3>Scan Planets Pop-Up</h3>
            Clicking the "Scan New Planets" pop-up provides the scan button, and displays your scan stat, the number of planets you have on scan, the number of planets in the galaxy, your chance for a successful scan, and an image of the planet that you just scanned, or a blank planet image if you have not scanned<br>
            <img src="../assets/scanpopup.png">

            <h3>Planet Window</h3>
            Clicking a planet displays the <a href="planetwindow.html">Planet</a> window<br>
            <img src="../assets/planetwindow.png">

            <h3>Planet Quick Action</h3>
            The quick action button displays a few artifacts that you can use without actually opening the planet<br>
            <img src="../assets/planetquickaction.png">
            '''
    
    async with aiofiles.open(outPath + "interface/planetstab.html", "w") as file:
        await file.write(html)

asyncio.run(writePlanetsTab())

async def writePlanetWindow():
    html =  ''' 
            <head><link rel=\"stylesheet\" href=\"../style.css\"></head>
            <h2>Planet Window</h2>
            This window displays information about a particular planet. The window changes depending on the owner<br>
            <img src="../assets/planetwindow.png"><br><br>

            <img src="../assets/planetwindowheader.png"><br>
            This section displays any icons representing planet events and effects, the planet image, the name of the planet, the <a href="../planetstats/size.html">Size</a> and <a href="../planettypes.html">Type</a> of the planet, the rarity of the type (if applicable), the controller, and an action button<br>
            You can click the icons in the upper-left of the window for details on the effects<br>
            The action button depends on the owner:<br>
            If you or a Legion member own the planet, then this button lets you <a href="../actions/guard.html">Guard</a> the planet<br>
            If a player in another Legion owns the planet, then this button lets you <a href="../actions/attackplanet.html">Attack</a> the planet<br>
            If no one owns the planet, then this button lets you <a href="./actions/colonize.html">Colonize</a> the planet<br><br>

            <img src="../assets/planetresourcestab.png"><br>
            This tab displays the resources of the planet. You can click each production value to see the base values of the resource and any modifiers<br>
            At the bottom of the tab you can see the passive stats for the planet. They can be Attack, Defense, or Cloak<br><br>

            <img src="../assets/planetcolonytab.png"><br>
            This tab, which does not appear on unoccupied planets, displays the following:<br>
            The <a href="../planetstats/population.html">Population</a> of the planet, which you can click for a detailed pop-up of the base value and modifiers<br>
            The age and <a href="../planetstats/developmentstatus.html">Development Status</a> of the planet, which you can click for a detailed pop-up<br>
            The <a href="../planetstats/threatstatus.html">Threat Status</a> of the planet, which you can click for a detailed pop-up<br>
            The <a href="../planetstats/defense.html">Defense</a>, <a href="../planetstats/attack.html">Attack</a>, and <a href="../planetstats/cloak.html">Cloak</a> of the planet, each of which you can click for a detailed pop-up<br><br>

            <img src="../assets/planetstructurestab.png"><br>
            This tab, which does not appear on unoccupied planets, displays the following:<br>
            The space on the planet, which you can click for a detailed pop-up<br>
            The <a href="../action/buildstructure.html">Build New Structure</a> button, which you can click to see the structure menu (only on planets that you or a Legion member own)<br>
            The list of structures on the planet. If you own the planet, then each structure will have a "Demolish" button. This button removes the structure without returning anything required for building the structure<br>
            Note: If you have used a <a href="../artifacts/MylaraiBuildExtractor.html">Mylarai Build Extractor</a>, then structures that you can extract will return the original artifact to you. Also note that this button sometimes appears on structures that you can't extract; clicking the button in such cases will cause an error message<br><br>

            <img src="../assets/planetactionstab.png"><br>
            This tab displays the following:<br>
            The <a href="../actions/planetplayeralert.png">Alert</a> button, which makes the planet visible to your Legion<br>
            Buttons to use either artifacts that target the planet or artifacts that target yourself<br>
            The <a href="../actions/abandon.html">Abandon</a> button, if you own the planet<br>
            The <a href="../actions/flagplanet.html">Flag</a> button, which allows you to mark a planet with a flag. Note: due to the <a href="../artifacts/VethinBomb.html">Vethin Bomb</a>, it is not recommended to use the black flag, except for the use of the bomb<br>
            An abilities button, to access abilities that you can use on the planet
            The <a href="../actions/analyzeplanet.html">Analyze</a> button, if Analysis is available on the planet<br>
            Any planet-based abilities, which come from structures or effects<br><br>

            <img src="../assets/planeteffectstab.png"><br>
            This tab displays the various effects on the planet. This does not appear on unoccupied planets
            '''
    
    async with aiofiles.open(outPath + "interface/planetwindow.html", "w") as file:
        await file.write(html)

asyncio.run(writePlanetWindow())

evolutionTabHtml = "<head><link rel=\"stylesheet\" href=\"../style.css\"></head>"
evolutionTabHtml += '''<h2>Evolution Tab</h2>
                        Access this tab either by clicking on the Genes value in the header or by clicking on your race image in the header.<br><br>
                        <img style="border: 1px solid gray;" src="../assets/genestab1.png"><img style="border: 1px solid gray;" src="../assets/genestab2.png"><br><br>
                        This tab includes actions related to Evolution Genes.<br><br>
                        <img style="border: 1px solid gray;" src="../assets/evolutiontab.png"><br>
                        <h3>Grow Genes</h3>
                        <img src="../assets/growgenes.png"><br>
                        This button grants Genes, which you can use for Evolutions, artifacts, and abilities.<br>
                        <a href="../actions/growgenes.html">More Information</a><br>
                        <h3>Complete Evolution</h3><br>
                        <img src="../assets/completedevolution.png"><br>
                        Evolutions are upgrades to your current race. They only apply while you are that race, but they persist if you switch to another race and then switch back.<br>
                        <a href="../actions/completeevolutions.html">More Information</a>
                        '''

with open(outPath + "interface/evolutiontab.html", "w") as file:
    file.write(evolutionTabHtml)

html = "<head><script type=\"text/javascript\" charset=\"utf8\" src=\"../../sorttable.js\" defer></script><script type=\"text/javascript\" charset=\"utf8\" src=\"growgenes.js\" defer></script><link rel=\"stylesheet\" href=\"../style.css\"></head>"
html += '''<h2>Grow Genes</h2>
            <img src="../assets/growgenes.png"><br><br>
            This button grants Genes, which you can use for Evolutions, artifacts, and abilities. By default, it grants 8 - 16 Genes with a 20 hour cooldown.<br>Click various bonuses below to see final timer and values: <span id=\"final-value\">8 - 16</span> <span id=\"final-cooldown\">20</span> hours<br>'''

cooldownTable = "<table class=\"sortable\"><thead><tr><th class=\"sort_a\" style=\"border: 1px solid gray;width: 300;padding: 5;\">Source</th><th class=\"sort_a\" style=\"border: 1px solid gray;width: 200;padding: 5;\">Type</th><th class=\"sort_a\" style=\"border: 1px solid gray;width: 30;padding: 5;\">Value</th><th class=\"sort_a\" style=\"border: 1px solid gray;width: 100;padding: 5;\">Duration</th><th style=\"border: 1px solid gray;width: 30;padding: 5;\">Active?</th></tr></thead>"
boostTable = "<table class=\"sortable\"><thead><tr><th class=\"sort_a\" style=\"border: 1px solid gray;width: 300\">Source</th><th class=\"sort_a\" style=\"border: 1px solid gray;width: 200;padding: 5;\">Type</th><th class=\"sort_a\" style=\"border: 1px solid gray;width: 30\">Value</th><th class=\"sort_a\" style=\"border: 1px solid gray;width: 100\">Duration</th><th style=\"border: 1px solid gray;width: 30;padding: 5;\">Active?</th></tr></thead>"
amountTable = "<table class=\"sortable\"><thead><tr><th class=\"sort_a\" style=\"border: 1px solid gray;width: 300\">Source</th><th class=\"sort_a\" style=\"border: 1px solid gray;width: 200;padding: 5;\">Type</th><th class=\"sort_a\" style=\"border: 1px solid gray;width: 30\">Value</th><th class=\"sort_a\" style=\"border: 1px solid gray;width: 100\">Duration</th><th style=\"border: 1px solid gray;width: 30;padding: 5;\">Active?</th></tr></thead>"
resetTable = "<table class=\"sortable\"><thead><tr><th class=\"sort_a\" style=\"border: 1px solid gray;width: 300\">Source</th><th class=\"sort_a\" style=\"border: 1px solid gray;width: 200;padding: 5;\">Type</th></tr></thead>"
for effect in genesEffects:
    if effect[0] == "Cooldown":
        source = ""
        if effect[1] == "Artifact":
            source = f"<a href=\"../artifacts/{normalizeName(effect[2])}.html\">{effect[2]}</a>"
        elif "Evolution" in effect[1]:
            source = f"<a href=\"../evolutions/{normalizeName(effect[2])}.html\">{effect[2]}</a>"
        elif effect[1] == "Structure Ability":
            source = f"<a href=\"{structureSourceLink(effect[5])}\">{effect[2]}</a>"
        elif effect[1] == "Petitioners Suite":
            source = f"<a href=\"../petitionerssuite/{normalizeName(effect[2])}.html\">{effect[2]}</a>"
        elif effect[1] == "Ally":
            source = f"<a href=\"../allies/{normalizeName(effect[2])}.html\">{effect[2]}</a>"
        elif effect[1] == "Planet-Based Ability":
            source = f"<a href=\"../allies/{normalizeName(effect[2])}.html\">{effect[2]}</a>"
        elif effect[1] == "Talent":
            source = f"<a href=\"../allies/{normalizeName(effect[2])}.html\">{effect[2]}</a>"
        cooldownTable += f"<tr><td style=\"border: 1px solid gray;\">{source}</td>"
        cooldownTable += f"<td style=\"border: 1px solid gray;\">{effect[1]}</td>"
        cooldownTable += f"<td style=\"border: 1px solid gray;\">{effect[3]}</td>"
        cooldownTable += f"<td style=\"border: 1px solid gray;\">{effect[4]}</td>"
        cooldownTable += f"<td style=\"border: 1px solid gray;\"><input type=\"checkbox\" class=\"cooldown\" data-value=\"{effect[3].replace('%', '')}\"></td>"
        cooldownTable += "</tr>"
    elif effect[0] == "Boost":
        source = ""
        if effect[1] == "Artifact":
            source = f"<a href=\"../artifacts/{normalizeName(effect[2])}.html\">{effect[2]}</a>"
        elif effect[1] == "Profession":
            source = f"<a href=\"../professions/{normalizeName(effect[2])}.html\">{effect[2]}</a>"
        elif effect[1] == "Petitioners Suite":
            source = f"<a href=\"../petitionerssuite/{normalizeName(effect[2])}.html\">{effect[2]}</a>"
        elif "Evolution -" in effect[1]:
            source = f"<a href=\"../evolutions/{normalizeName(effect[2])}.html\">{effect[2]}</a>"
        elif effect[1] == "Seasonal":
            source = f"<a href=\"../seasonals/{normalizeName(effect[2])}.html\">{effect[2]}</a>"
        elif effect[1] == "Talent":
            source = f"<a href=\"../ascendancy/{normalizeName(effect[2])}.html\">{effect[2]}</a>"
        elif effect[1] == "Planet-Based Ability":
            source = f"<a href=\"../planetbasedabilities/{normalizeName(effect[2])}.html\">{effect[2]}</a>"
        elif effect[1] == "Ally":
            source = f"<a href=\"../allies/{normalizeName(effect[2])}.html\">{effect[2]}</a>"
        elif effect[1] == "Structure Ability":
            source = f"<a href=\"{structureSourceLink(effect[5])}\">{effect[2]}</a>"
        boostTable += f"<tr><td style=\"border: 1px solid gray;\">{source}</td>"
        boostTable += f"<td style=\"border: 1px solid gray;\">{effect[1]}</td>"
        boostTable += f"<td style=\"border: 1px solid gray;\">{effect[3]}</td>"
        boostTable += f"<td style=\"border: 1px solid gray;\">{effect[4]}</td>"
        boostTable += f"<td style=\"border: 1px solid gray;\"><input type=\"checkbox\" class=\"boost\" data-value=\"{effect[3].replace('%', '')}\"></td>"
        boostTable += "</tr>"
    elif effect[0] == "Amount":
        source = ""
        checkColumn = ""
        if effect[1] == "Artifact":
            source = f"<a href=\"../artifacts/{normalizeName(effect[2])}.html\">{effect[2]}</a>"
            checkColumn = f"<td style=\"border: 1px solid gray;\"><input type=\"checkbox\" class=\"amount-checkbox\" data-value=\"{effect[3].replace('%', '')}\"></td>"
        elif "Evolution -" in effect[1]:
            source = f"<a href=\"../evolutions/{normalizeName(effect[2])}.html\">{effect[2]}</a>"
            checkColumn = f"<td style=\"border: 1px solid gray;\"><input type=\"checkbox\" class=\"amount-checkbox\" data-value=\"{effect[3].replace('%', '')}\"></td>"
        elif effect[1] == "Module":
            source = f"<a href=\"../modules/{normalizeName(effect[2])}.html\">{effect[2]}</a>"
            if effect[5] == 1:
                checkColumn += f"<td style=\"border: 1px solid gray;\"><input type=\"checkbox\" class=\"amount-checkbox\" data-value=\"{effect[3]}\"></td>"
            else:
                checkColumn += f"<td style=\"border: 1px solid gray;\"><select data-value=\"{effect[3]}\" class=\"amount-count\">"
                for i in range(effect[5] + 1):
                    checkColumn += f"<option value=\"{i}\">{i}</option>"
                checkColumn += "</td>"
        amountTable += f"<tr><td style=\"border: 1px solid gray;\">{source}</td>"
        amountTable += f"<td style=\"border: 1px solid gray;\">{effect[1]}</td>"
        amountTable += f"<td style=\"border: 1px solid gray;\">{effect[3]}</td>"
        amountTable += f"<td style=\"border: 1px solid gray;\">{effect[4]}</td>"
        amountTable += checkColumn
        amountTable += "</tr>"
    elif effect[0] == "Reset":
        source = ""
        if effect[1] == "Artifact":
            source = f"<a href=\"../artifacts/{normalizeName(effect[2])}.html\">{effect[2]}</a>"
        elif effect[1] == "Petitioners Suite":
            source = f"<a href=\"../petitionerssuite/{normalizeName(effect[2])}.html\">{effect[2]}</a>"
        elif "Evolution -" in effect[1]:
            source = f"<a href=\"../evolutions/{normalizeName(effect[2])}.html\">{effect[2]}</a>"
        elif effect[1] == "Planet-Based Ability":
            source = f"<a href=\"../planetbasedabilities/{normalizeName(effect[2])}.html\">{effect[2]}</a>"
        resetTable += f"<tr><td style=\"border: 1px solid gray\">{source}</td><td style=\"border: 1px solid gray\">{effect[1]}</td>"
        resetTable += "</tr>"
        
    else:
        print(f"Malformed Genes Effect: {effect}")
cooldownTable += "</table>"
boostTable += "</table>"
amountTable += "</table>"
resetTable += "</table>"

def generateInitiativeEffectiveDateCell(initiative, optionName):
    if 'winner' in initiative and initiative['winner'] == optionName:
        return f"<td style=\"border: 1px solid gray;\">Start: {initiative['end']}<br>Duration: {initiative['effectDuration']}</td>"
    elif 'winner' in initiative:
        return "<td style=\"border: 1px solid gray;\">Did not pass</td>"
    else:
        return "<td style=\"border: 1px solid gray;\">TBD</td>"


initiativesTable = "<table class=\"sortable\"><thead><tr><th class=\"sort_a\" style=\"border: 1px solid gray;width: 300\">Source</th><th class=\"sort_a\" style=\"border: 1px solid gray;width: 200;padding: 5;\">Type</th><th class=\"sort_a\" style=\"border: 1px solid gray;width: 200;padding: 5;\">In Effect</th><th class=\"sort_a\" style=\"border: 1px solid gray;width: 30\">Value</th><th style=\"border: 1px solid gray;width: 30;padding: 5;\">Active?</th></tr></thead>"
for (name, initiative) in initiatives.items():
    for option in initiative['options']:
        if 'playerEffects' in option:
            for effect in option['playerEffects']:
                if effect['type'] == "Increase Genes Production":
                    initiativesTable += "<tr>"
                    initiativesTable += f"<td style=\"border: 1px solid gray;\">{option['name']}</td>"
                    initiativesTable += "<td style=\"border: 1px solid gray;\">Modify Yield</td>"
                    initiativesTable += generateInitiativeEffectiveDateCell(initiative, option['name'])
                    initiativesTable += f"<td style=\"border: 1px solid gray;\">{effect['value']}</td>"
                    initiativesTable += f"<td style=\"border: 1px solid gray;\"><input type=\"checkbox\" class=\"boost\" data-value=\"{effect['value'].replace('%', '')}\"></td>"
                elif effect['type'] == "Decrease Grow Genes Cooldown":
                    initiativesTable += "<tr>"
                    initiativesTable += f"<td style=\"border: 1px solid gray;\">{option['name']}</td>"
                    initiativesTable += "<td style=\"border: 1px solid gray;\">Modify Cooldown</td>"
                    initiativesTable += generateInitiativeEffectiveDateCell(initiative, option['name'])
                    initiativesTable += f"<td style=\"border: 1px solid gray;\">{effect['value']}</td>"
                    initiativesTable += f"<td style=\"border: 1px solid gray;\"><input type=\"checkbox\" class=\"cooldown\" data-value=\"{effect['value'].replace('%', '')}\"></td>"
    if 'failurePlayerEffects' in initiative:
        for effect in initiative['failurePlayerEffects']:
            if effect['type'] == "Increase Genes Production":
                initiativesTable += "<tr>"
                initiativesTable += f"<td style=\"border: 1px solid gray;\">{name}: Failure</td>"
                initiativesTable += "<td style=\"border: 1px solid gray;\">Modify Yield</td>"
                initiativesTable += generateInitiativeEffectiveDateCell(initiative, "Failure")
                initiativesTable += f"<td style=\"border: 1px solid gray;\">{effect['value']}</td>"
                initiativesTable += f"<td style=\"border: 1px solid gray;\"><input type=\"checkbox\" class=\"boost\" data-value=\"{effect['value'].replace('%', '')}\"></td>"
            elif effect['type'] == "Decrease Grow Genes Cooldown":
                initiativesTable += "<tr>"
                initiativesTable += f"<td style=\"border: 1px solid gray;\">{name}: Failure</td>"
                initiativesTable += "<td style=\"border: 1px solid gray;\">Modify Cooldown</td>"
                initiativesTable += generateInitiativeEffectiveDateCell(initiative, "Failure")
                initiativesTable += f"<td style=\"border: 1px solid gray;\">{effect['value']}</td>"
                initiativesTable += f"<td style=\"border: 1px solid gray;\"><input type=\"checkbox\" class=\"cooldown\" data-value=\"{effect['value'].replace('%', '')}\"></td>"



html += f"<h3>Decrease Cooldown</h3>{cooldownTable}<br><h3>Boost Production</h3>{boostTable}<br><h3>Increase Amount</h3>{amountTable}<br><h3>Reset Cooldown</h3>{resetTable}<br><h3>Initiatives</h3>{initiativesTable}"

with open(outPath + "actions/growgenes.html", "w") as file:
    file.write(html)


html = "<head><link rel=\"stylesheet\" href=\"style.css\"><script type=\"text/javascript\" charset=\"utf8\" src=\"../sorttable.js\" defer></script></head><table class=\"sortable\"><thead><tr>"
html += f"<th class=\"sort_a\" style=\"padding: 2;border: 1px solid gray;width: 250\">Name</th>"

for (name, planetType) in planetTypes.items():
    html += f"<th style=\"border: 1px solid gray;width: 50\">{name}</th>"

html += "</tr></thead>"

for (name, artifact) in artifacts.items():
    if 'restrictions' in artifact:
        for restriction in artifact['restrictions']:
            if restriction['type'] == "Type":
                html += f"<tr><td style=\"border: 1px solid gray\"><a href=\"artifacts/{normalizeName(name)}.html\">{name}</a></td>"
                for (planetTypeName, planetType) in planetTypes.items():
                    if planetTypeName in restriction['types']:
                        html += "<td style=\"border: 1px solid gray\">X</td>"
                    else:
                        html += "<td style=\"border: 1px solid gray\"></td>"
                html += "</tr>"
        

html += "</table>"

with open(outPath + "types_table.html", "w") as file:
    file.write(html)

async def writeRank():
    html = "<head><link rel=\"stylesheet\" href=\"../style.css\"><script type=\"text/javascript\" charset=\"utf8\" src=\"../sorttable.js\" defer></script></head>"

    html += "<h1>Rank</h1>Your player rank, which unlocks access to various features<br>"
    insigniaTableColCount = 6
    html += "<h2>Rank Insignia Gallery</h2><table><tr>"

    files = [f for f in Path(outPath + "assets/ranks").iterdir() if f.is_file()]

    files.sort(key=lambda x: int(x.stem))
    count = 0
    for file in files:
        
        if count == insigniaTableColCount:
            html += "</tr><tr>"
            count = 0
        count += 1
        html += f"<td><img width=\"200\" src=\"../assets/ranks/{file.name}\"></td>"

    html += "</table>"

    async with aiofiles.open(outPath + "stats/ranks.html", "w") as file:
        await file.write(html)

asyncio.run(writeRank())


