from flask import Flask
from flask import jsonify, render_template

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
def generate_encounter(id):
    return jsonify({'id':id})

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5000)