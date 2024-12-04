from flask import Flask, render_template, request, jsonify
from database import init_db, insert_name, get_all_names
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/process", methods=["POST"])
def process():
    data = request.json
    name = data.get("name")
    if name: 
        insert_name(name)
        return jsonify({"message": f":) Hello, {name}!"})
    return jsonify({"error": "No name provided"}), 400

@app.route("/names", methods=["GET"])
def get_names():
    # Retrieve all names from the database
    names = get_all_names()
    return jsonify({"names": names})

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
