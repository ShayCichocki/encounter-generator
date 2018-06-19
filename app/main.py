from flask import Flask
from flask import jsonify, render_template
from flask import request
import json


multipliers =  [0,1,1.5,2,2,2,2,2.5,2.5,2.5,2.5,3,3,3,3,4]

encounter_difficulty_file = "data/encounter-difficulty.json"
simple_monsters_file = "data/simplified-monsters.json"
keyed_monsters_file = "data/monsters-keyed.json"

app = Flask(__name__, template_folder="../encountergenux")

simplified_monsters = {}
encounter_difficulty = {}
keyed_monsters = {}

@app.route("/")
def home():
    return render_template('www/index.html')

@app.route("/monsters")
def get_monster_list():
    simplified_monsters = json.load(open(simple_monsters_file, "r"))
    return jsonify(simplified_monsters)

@app.route("/monsters/<id>")
def get_monster_by_id(id):
    keyed_monsters = json.load(open(keyed_monsters_file, "r"))
    return jsonify(keyed_monsters[str(id)])

@app.route("/generate-encounter", methods=['POST'])
def generate_encounter():
    encounter_data = json.loads(request.data)
    total_xp = gen_encounter(encounter_data)

    returnable = {
        'total_xp': total_xp
    }
    return jsonify(returnable)


def gen_encounter(encounter_data):
    difficulty = encounter_data['difficulty']
    total_xp = 0
    for i in encounter_data['characters']:
        total_xp = total_xp + encounter_difficulty[difficulty][i-1]
    return total_xp


if __name__ == "__main__":
    encounter_difficulty = json.load(open(encounter_difficulty_file, "r"))
    app.run(host="0.0.0.0", debug=True, port=5000)