from flask import Flask, request, jsonify
from flask_cors import CORS
import numpy as np
import sqlite
import pickle

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})  # Allow all origins (for development)

# Load trained model and scaler
model_path = "model/house_price_model.pkl"
scaler_path = "model/scaler.pkl"

try:
    with open(model_path, 'rb') as model_file:
        model = pickle.load(model_file)
    with open(scaler_path, 'rb') as scaler_file:
        scaler = pickle.load(scaler_file)
    print("✅ Model and Scaler Loaded Successfully")
except Exception as e:
    print(f"❌ Error loading model or scaler: {e}")

# Initialize SQLite database
DB_PATH = "house_predictions.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS predictions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            GrLivArea REAL,
            LotArea REAL,
            OverallQual INTEGER,
            OverallCond INTEGER,
            YearBuilt INTEGER,
            TotalBsmtSF REAL,
            predicted_price REAL
        )
    ''')
    conn.commit()
    conn.close()

init_db()

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        features = np.array([[data["GrLivArea"], data["LotArea"], data["OverallQual"],
                              data["OverallCond"], data["YearBuilt"], data["TotalBsmtSF"]]])
        
        # Scale the features
        scaled_features = scaler.transform(features)
        
        # Predict house price
        prediction = model.predict(scaled_features)[0]
        
        # Store the input and prediction in SQLite
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO predictions (GrLivArea, LotArea, OverallQual, OverallCond, YearBuilt, TotalBsmtSF, predicted_price)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (data["GrLivArea"], data["LotArea"], data["OverallQual"],
              data["OverallCond"], data["YearBuilt"], data["TotalBsmtSF"], float(prediction)))
        conn.commit()
        conn.close()

        return jsonify({"predicted_price": float(prediction)})

    except Exception as e:
        print(f"❌ Prediction error: {e}")
        return jsonify({"error": "Prediction failed"}), 500

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5020)  # Make Flask accessible from network

