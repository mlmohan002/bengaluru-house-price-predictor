from flask import Flask, render_template, request
import pickle
import pandas as pd
import json

app = Flask(__name__)

# Load once during startup
with open("RidgeModel.pkl", "rb") as model_file:
    model = pickle.load(model_file)

with open("locations.json", "r") as f:
    locations = json.load(f)

@app.route("/")
def home():
    return render_template("index.html", locations=locations)

@app.route("/health")
def health():
    return "OK", 200

@app.route("/predict", methods=["POST"])
def predict():
    try:
        location = request.form["location"]
        sqft = float(request.form["sqft"])
        bath = float(request.form["bath"])
        bhk = int(request.form["bhk"])

        input_data = {
            "location": [location],
            "total_sqft": [sqft],
            "bath": [bath],
            "bhk": [bhk]
        }

        input_df = pd.DataFrame(input_data)

        prediction = round(model.predict(input_df)[0], 2)

        return render_template(
            "index.html",
            locations=locations,
            prediction=prediction
        )

    except Exception as e:
        return render_template(
            "index.html",
            locations=locations,
            prediction=f"Error: {str(e)}"
        )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
