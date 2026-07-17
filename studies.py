from math import log

sortedMedalLines = []
with open("studies.txt", "r") as file:
    sortedMedalLines = file.readlines()

studiesTotal = 0
for line in sortedMedalLines:
    if line == "\n":
        continue

    research = float(line) + 1.0
    if research == 0.0:
        continue

    studies = log(research * 2.8 / 1200.0, 2.8) / 10.0
    if studies > 0:
        studiesTotal += studies

print(studiesTotal)