from flask import Flask, request, jsonify
import util
from util import load_saved_artifacts
import warnings

warnings.filterwarnings("ignore")

app = Flask(__name__)

load_saved_artifacts()


# @app.get("/ping")
# def ping():
#     return "pong"


@app.route('/get_state_names', methods=['GET'])
def get_state_names():
    response = jsonify({
        'state': util.get_state_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


@app.route('/predict_suicide_rate', methods=['POST'])
def predict_suicide_rate():
    Year = int(request.form['Year'])
    State = request.form['State']
    Type = int(request.form['Type'])
    Gender = int(request.form['Gender'])
    Age_group = int(request.form['Age_group'])

    value = util.get_estimated_suicide(State, Year, Type, Gender, Age_group)
    response = jsonify({
        'estimated_suicide': value
    })

    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == "__main__":
    print("Starting Python Flask Server For Suicide Rate Prediction")
    app.run(debug=True)
