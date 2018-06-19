import json
from fractions import Fraction
difficultyFile = open("../app/data/monsters.json", "r")

data = json.load(difficultyFile)

simplifiedData = []
keyedMonsters = {}
j=1
for i in data:
    simplifiedData.append({
        "id": j,
        "name": i['Name'],
        "cr": float(Fraction(i['CR'])),
        "xp": float(i['XP']),
        "environment": i['Environment']
    })
    keyedMonsters[j] = i
    j=j+1

simplifiedMonsters = open("../app/data/simplified-monsters.json", "w")
simplifiedMonsters.write(json.dumps(simplifiedData))
difficultyFile = open("../app/data/monsters-keyed.json", "w")
difficultyFile.write(json.dumps(keyedMonsters))