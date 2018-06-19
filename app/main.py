from flask import Flask
from flask import jsonify, render_template
from flask import request
import json

from app.monster import Monster

multipliers =  [0,1,1.5,2,2,2,2,2.5,2.5,2.5,2.5,3,3,3,3,4]

simple_monsters_file = "data/simplified-monsters.json"
keyed_monsters_file = "data/monsters-keyed.json"

app = Flask(__name__, template_folder="../encountergenux")

simplified_monsters = {}
encounter_difficulty = {}
keyed_monsters = {}
monsters_dict = {}

@app.route("/")
def home():
    return render_template('www/index.html')

@app.route("/monsters")
def get_monster_list():

    return jsonify(simplified_monsters)

@app.route("/monsters/<id>")
def get_monster_by_id(id):
    keyed_monsters = json.load(open(keyed_monsters_file, "r"))
    if(str(id) in keyed_monsters):
        return jsonify(keyed_monsters[str(id)])
    else:
        return jsonify({})

@app.route("/generate-encounter", methods=['POST'])
def generate_encounter():
    encounter_data = json.loads(request.data)
    total_xp_possible = get_xp_budget(encounter_data)

    returnable = {
        'totalXpPossible': total_xp_possible
    }
    return jsonify(returnable)

if __name__ == "__main__":
    simplified_monsters = json.load(open(simple_monsters_file, "r"))

    j=1
    for monster in simplified_monsters:
        monsters_dict[j] = Monster(j, *simplified_monsters[j])
        j=j+1

    app.run(host="0.0.0.0", debug=True, port=5000)