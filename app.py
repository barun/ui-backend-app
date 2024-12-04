from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/process", methods=["POST"])
def process():
    data = request.json
    name = data.get("name")
    if name:
        return jsonify({"message": f":) Hello, {name}!"})
    return jsonify({"error": "No name provided"}), 400

if __name__ == "__main__":
    app.run(debug=True)
