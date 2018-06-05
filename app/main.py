from flask import Flask
from flask import jsonify, render_template
from flask import request
import json

encounter_difficulty = "data/encounter-difficulty.json"
app = Flask(__name__, template_folder="../encountergenux")

@app.route("/")
def home():
    return render_template('www/index.html')

@app.route("/monsters")
def get_monster_list():
    return jsonify([])

@app.route("/monsters/<id>")
def get_monster_by_id(id):
    return jsonify({'ids':id})

@app.route("/generate-encounter", methods=['POST'])
def generate_encounter():
    encounter_data = json.loads(request.data)
    total_xp = gen_encounter(encounter_data)

    encounter_data['total_xp'] = total_xp
    return jsonify(encounter_data)


def gen_encounter(encounter_data):
    encounter_file = open(encounter_difficulty, "r")
    data = json.load(encounter_file)
    difficulty = encounter_data['difficulty']
    total_xp = 0
    for i in encounter_data['characters']:
        total_xp = total_xp + data['levelDifficulty'][str(i)][difficulty]
    return total_xp


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5000)