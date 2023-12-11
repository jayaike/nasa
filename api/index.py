from flask import Flask, json
import pickle

app = Flask(__name__)

@app.route('/')
def home():
    loaded_model = pickle.load(open('model.sav', 'rb'))
    prediction = loaded_model.predict([[0.255009, 0.570217, 42737.733765, 4.627557e+07, 20.09]])[0]
   
    response = app.response_class(
        response=json.dumps({'isHazardous': bool(prediction)}),
        status=200,
        mimetype='application/json'
    )
    return response