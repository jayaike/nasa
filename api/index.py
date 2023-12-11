from flask import Flask, json

app = Flask(__name__)

@app.route('/')
def home():
    response = app.response_class(
        response=json.dumps({'isHazardous': True}),
        status=200,
        mimetype='application/json'
    )
    return response