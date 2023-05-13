from flask import Flask, request
import pandas as pd

df = pd.read_csv('./homework-mn-medications/data/rxdetail2018.csv')

app = Flask(__name__)

@app.route('/', methods=["GET"])
def home():
    return 'this is an api service for MN Medication details'

@app.route('/preview', methods=['GET'])
def preview():
    top10rows = df.head(1)
    result = top10rows.to_json(orient="records")
    return result

@app.route('/medications/<value>', methods=["GET"])
def medication(value):
    print('value', value)
    filtered = df[df['LABELERNAME'] == value]
    return filtered.to_json(orient="records")


if __name__ == '__main__':
    app.run (debug=True)