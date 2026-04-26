# Bengaluru House Price Prediction

A Flask-based machine learning web application that predicts house prices in Bengaluru based on user inputs such as location, total square feet, number of bathrooms, and BHK.

## Live Demo

[Click here to use the deployed app](https://bengaluru-house-price-predictor-ztph.onrender.com)

## Features

- Predicts Bengaluru house prices using a trained machine learning model.
- User-friendly web interface built with Flask.
- Takes inputs like location, square feet, bath, and BHK.
- Deployed on Render.

## Project Structure

```bash
house-price-app/
│── app.py
│── model.pkl
│── locations.json
│── requirements.txt
│── README.md
│── templates/
│   └── index.html
│── static/
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/mlmohan002/bengaluru-house-price-predictor.git
cd bengaluru-house-price-predictor
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

**Windows PowerShell**

```bash
.venv\Scripts\Activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

## Run Locally

Start the Flask application:

```bash
python app.py
```

Then open your browser and visit:

```bash
http://127.0.0.1:5000
```

## Deployment on Render

### Build Command

```bash
pip install -r requirements.txt
```

### Start Command

```bash
gunicorn app:app
```

## Example Inputs

- **Location:** Indira Nagar
- **Total Sqft:** 1200
- **Bath:** 2
- **BHK:** 2

## Tech Stack

- Python
- Flask
- Pandas
- NumPy
- Scikit-learn
- Gunicorn
- HTML/CSS

## Future Improvements

- Add better UI styling.
- Add input validation.
- Show price range instead of only one value.
- Add model performance metrics on the page.

## Author

** Mohan**

GitHub: [mlmohan002](https://github.com/mlmohan002)
