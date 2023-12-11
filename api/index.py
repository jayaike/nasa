from flask import Flask, json, request
import pickle
import joblib
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

scaler = joblib.load('scaler.pkl')
loaded_model = pickle.load(open('model.sav', 'rb'))

@app.route('/')
def home():
    min_diameter = float(request.args.get('min_diameter'))
    max_diameter = float(request.args.get('max_diameter'))
    relative_velocity = float(request.args.get('relative_velocity'))
    miss_distance = float(request.args.get('miss_distance'))
    magnitude = float(request.args.get('magnitude'))

    X = [[min_diameter, max_diameter, relative_velocity, miss_distance, magnitude]]

    X_scaled = scaler.transform(X)   
    prediction = loaded_model.predict(X_scaled)[0]
    prediction_proba = loaded_model.predict_proba(X_scaled)[0]
   
    response = app.response_class(
        response=json.dumps({
            'isHazardous': bool(prediction), 
            'probability': str(prediction_proba[prediction]),
            'x': str(X),
            'xScaled': str(X_scaled),
            'prediction': str(prediction)
          }),
        status=200,
        mimetype='application/json'
    )
    return response