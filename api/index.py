from flask import Flask, json
from sklearn.preprocessing import MinMaxScaler
import pickle
import numpy as np

app = Flask(__name__)

@app.route('/')
def home():
    loaded_model = pickle.load(open('model.sav', 'rb'))

    X = np.array([[0.265800, 0.594347, 73588.726663, 6.143813e+07, 20.00]])
    scaler = MinMaxScaler()
    X_scaled = scaler.fit_transform(X)   
    prediction = loaded_model.predict(X_scaled)[0]
   
    response = app.response_class(
        response=json.dumps({
            'isHazardous': bool(prediction), 
            'xScaled': str(X_scaled),
            'prediction': str(prediction)
          }),
        status=200,
        mimetype='application/json'
    )
    return response