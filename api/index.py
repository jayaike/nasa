from flask import Flask, json
import pickle

app = Flask(__name__)

@app.route('/')
def home():
    loaded_model = pickle.load(open('model.sav', 'rb'))
    prediction = loaded_model.predict([[1.198271, 2.679415, 13569.249224, 54839740,	16.73]])[0]
   
    response = app.response_class(
        response=json.dumps({'isHazardous': bool(prediction)}),
        status=200,
        mimetype='application/json'
    )
    return response