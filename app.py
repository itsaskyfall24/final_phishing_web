from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

# Inisialisasi Flask
app = Flask(__name__)
CORS(app)  # Mengizinkan akses dari frontend

# Muat model dan TF-IDF Vectorizer
model = joblib.load("random_forest_model.pkl")  # Simpan model ini dari scikit-learn
vectorizer = joblib.load("tfidf_vectorizer.pkl")  # Simpan TF-IDF vectorizer

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    url = data.get('url')  # Mendapatkan URL dari frontend

    if not url:
        return jsonify({'error': 'URL is required!'}), 400

    # Preprocessing URL
    features = vectorizer.transform([url]).toarray()

    # Prediksi dengan model
    prediction = model.predict(features)
    label_map = {0: "benign", 1: "defacement", 2: "malware", 3: "phishing"}  # Sesuaikan dengan label
    result = label_map[prediction[0]]

    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
