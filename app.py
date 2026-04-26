from flask import Flask
from flask import render_template
from flask import request
import pickle
import pandas as pd
import json


app = Flask(__name__)


model = pickle.load(open("RidgeModel.pkl", "rb"))

with open("locations.json", "r") as f:
    locations = json.load(f)

@app.route("/")
def home():
    return render_template("index.html", locations=locations)

@app.route("/predict", methods=["POST"])
def predict():
    location = request.form["location"]
    sqft = float(request.form["sqft"])
    bath = float(request.form["bath"])
    bhk = int(request.form["bhk"])

    input_df = pd.DataFrame([{
        "location": location,
        "total_sqft": sqft,
        "bath": bath,
        "bhk": bhk
    }])

    prediction = model.predict(input_df)[0]
    return render_template(
        "index.html",
        locations=locations,
        prediction=round(prediction, 2)
    )

if __name__ == "__main__":
    app.run(debug=True)