from flask import Flask, json
import pickle

app = Flask(__name__)

@app.route('/')
def home():
    loaded_model = pickle.load(open('model.sav', 'rb'))
    response = app.response_class(
        response=json.dumps({'isHazardous': True, 'm': str(loaded_model)}),
        status=200,
        mimetype='application/json'
    )
    return response