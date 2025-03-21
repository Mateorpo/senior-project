from flask import Flask, request, jsonify
from flask_cors import CORS
import numpy as np
import pickle

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})  # Allow all origins (for development)

# Load your trained model and scaler
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

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        features = np.array([[data["GrLivArea"], data["LotArea"], data["OverallQual"],
                              data["OverallCond"], data["YearBuilt"], data["TotalBsmtSF"]]])
        scaled_features = scaler.transform(features)
        prediction = model.predict(scaled_features)[0]
        return jsonify({"predicted_price": float(prediction)})
    except Exception as e:
        print(f"❌ Prediction error: {e}")
        return jsonify({"error": "Prediction failed"}), 500

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5020)  # Make Flask accessible from network
