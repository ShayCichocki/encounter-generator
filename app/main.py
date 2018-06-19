from flask import Flask
from flask import jsonify, render_template
from flask import request
import json
from generator.encountergen import EncounterGen
from generator.monster import Monster

multipliers =  [0,1,1.5,2,2,2,2,2.5,2.5,2.5,2.5,3,3,3,3,4]

simple_monsters_file = "data/simplified-monsters.json"
keyed_monsters_file = "data/monsters-keyed.json"

app = Flask(__name__, template_folder="../encountergenux")
app.keyed_monsters = {}
app.simplified_monsters = {}

app.encounter_generator = None

@app.route("/")
def home():
    return render_template('www/index.html')

@app.route("/monsters")
def get_monster_list():
    return jsonify(app.simplified_monsters)

@app.route("/monsters/<id>")
def get_monster_by_id(id):
    if(str(id) in app.keyed_monsters):
        return jsonify(app.keyed_monsters[str(id)])
    else:
        return jsonify({})

@app.route("/generate-encounter", methods=['POST'])
def generate_encounter():
    encounter_data = json.loads(request.data)
    encounter = app.encounter_generator.generate_encounter(encounter_data)
    return jsonify(encounter)

@app.before_first_request
def setup_data():
    app.keyed_monsters = json.load(open(keyed_monsters_file, "r"))
    app.simplified_monsters = json.load(open(simple_monsters_file, "r"))
    encounter_difficulty = json.load(open("data/encounter-difficulty.json", "r"))
    monster_dict = {}
    for monster in app.simplified_monsters:
        print(monster)
        monster_dict[monster['id']] = Monster(monster['id'], monster['name'], monster['cr'], monster['xp'], monster['environment'])
    app.encounter_generator = EncounterGen(monster_dict, encounter_difficulty)
