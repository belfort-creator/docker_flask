from flask import Flask, jsonify, request
from sklearn.externals import joblib
from data_prep import data_prep
import pandas as pd
import requests
import sys
import os
import shutil
import time
import traceback

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        if model:

            json_=request.json
            query_df=pd.DataFrame(json_)
            df_ml=data_prep(query_df)
            preds=list(model.predict(df_ml))

            return jsonify({"prediction": list(map(int, preds))})

    except Exception as e:

        return jsonify({'error': str(e), 'trace': traceback.format_exc()})

if __name__=='__main__':

    model_path='example_model'

    try:
        port=int(sys.argv[1])
        print('[*] Seting port as', port, '...')

    except Exception as e:
        port=80
        print('[*] Seting port as', port, '...')

    try:
        model=joblib.load(model_path)
        print('[*] Model loaded ...')

    except Exception as e:
        print('[*] ---ERROR---', e)

    app.run(host='0.0.0.0', debug=False)