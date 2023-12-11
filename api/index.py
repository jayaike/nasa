from flask import Flask, json
from sklearn.preprocessing import MinMaxScaler
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__)

df = pd.read_csv('neo.csv')
df['hazardous'] = df['hazardous'].replace({False: 0, True: 1})

X = df.drop("hazardous", axis=1)
y = df["hazardous"]

scaler = MinMaxScaler()
scaler.fit(X)

@app.route('/')
def home():
    loaded_model = pickle.load(open('model.sav', 'rb'))

    X = np.array([[0.265800, 0.594347, 73588.726663, 6.143813e+07, 20.00]])
    scaler = MinMaxScaler(feature_range=())
    X_scaled = scaler.transform(X)   
    prediction = loaded_model.predict(X_scaled)[0]
   
    response = app.response_class(
        response=json.dumps({
            'isHazardous': bool(prediction), 
            'x': str(X),
            'xScaled': str(X_scaled),
            'prediction': str(prediction)
          }),
        status=200,
        mimetype='application/json'
    )
    return response