from flask import Flask, json
import pickle

app = Flask(__name__)

@app.route('/')
def home():
    loaded_model = pickle.load(open('model.sav', 'rb'))
    prediction = loaded_model.predict([[0.265800, 0.594347, 73588.726663, 6.1438130, 20.00]])[0]
   
    response = app.response_class(
        response=json.dumps({'isHazardous': bool(prediction)}),
        status=200,
        mimetype='application/json'
    )
    return response