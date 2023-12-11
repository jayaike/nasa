from flask import Flask, json
from sklearn.preprocessing import MinMaxScaler
import pickle


app = Flask(__name__)

@app.route('/')
def home():
    loaded_model = pickle.load(open('model.sav', 'rb'))

    X = [[0.255009, 0.570217, 42737.733765, 4.627557e+07, 20.09]]
    scaler = MinMaxScaler()
    X_scaled = scaler.fit_transform(X)    
    prediction = loaded_model.predict(X_scaled)[0]
   
    response = app.response_class(
        response=json.dumps({'isHazardous': bool(prediction)}),
        status=200,
        mimetype='application/json'
    )
    return response