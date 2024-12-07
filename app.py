from flask import Flask, render_template, request, jsonify
from database import init_db, insert_name, get_all_names
import logging
import base64
import os
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

app = Flask(__name__)

init_db()

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

@app.route("/upload-photo", methods=["POST"])
def upload_photo():
    try:
        data = request.json
        image_data = data.get("image")
        
        # Decode the base64 image
        header, encoded = image_data.split(",", 1)
        binary_image = base64.b64decode(encoded)
        
        # Save the image to a file (or database)
        file_path = os.path.join("uploads", "captured_photo.png")
        os.makedirs("uploads", exist_ok=True)
        with open(file_path, "wb") as f:
            f.write(binary_image)
        
        return jsonify({"message": "Photo uploaded successfully!"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400@app.route("/upload-photo", methods=["POST"])
if __name__ == "__main__":

    app.run(debug=True)
