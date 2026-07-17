import json

eventsStats = {
    "Q-Pedd":{"days":0},
    "Lepus":{"days":0},
    "Genoform":{"days":0},
    "Civicordium":{"days":0},
    "Bane":{"days":0},
    "Harvest":{"days":0},
    "Scruuge":{"days":0},
    "Chuhn":{"days":0},
}

itemTypes = [
    "challenges",
    "suite",
    "market",
    "npcs",
    "missions",
    "supporter",
    "planetEvents",
    "terminal",
    "dailyReward",
    "scan",
    "commonArtis",
    "council",
    "zone"
]

for itemType in itemTypes:
    for (event, stats) in eventsStats.items():
        stats[itemType] = 0

with open("config/seasonal_events.json", "r") as file:
    events = json.load(file)

for event in events:
    if event['name'] == "Spectral Convergence (2026)":
        for day in event['randomSeasonals']:
            dayList = []
            for (item, seasonal) in day.items():
                if item == "date":
                    continue

                if not seasonal in dayList and not item == "zone":
                    dayList.append(seasonal)
                
                
                eventsStats[seasonal][item] += 1
                

            for seasonal in dayList:
                eventsStats[seasonal]['days'] += 1

with open("convergencestats.json", "w") as file:
    json.dump(eventsStats, file, indent=4)