from flask import Flask, render_template, request
import pickle
import pandas as pd
import json

app = Flask(__name__)

# Load once at startup (important for speed)
with open("RidgeModel.pkl", "rb") as f:
    model = pickle.load(f)

with open("locations.json", "r") as f:
    locations = json.load(f)

@app.route("/")
def home():
    return render_template("index.html", locations=locations)

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Faster input capture
        location = request.form.get("location")
        sqft = float(request.form.get("total_sqft"))
        bath = float(request.form.get("bath"))
        bhk = int(request.form.get("bhk"))

        # Fast dataframe
        input_data = pd.DataFrame(
            [[location, sqft, bath, bhk]],
            columns=["location", "total_sqft", "bath", "bhk"]
        )

        prediction = round(model.predict(input_data)[0], 2)

        return render_template(
            "index.html",
            locations=locations,
            prediction_text=f"Estimated Price: ₹ {prediction} Lakhs"
        )

    except Exception as e:
        return render_template(
            "index.html",
            locations=locations,
            prediction_text=f"Error: {str(e)}"
        )

if __name__ == "__main__":
    app.run(debug=False)
