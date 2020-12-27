from scrape import new_banks 
from flask import Flask,send_file, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return send_file("index.html")

@app.route("/data")
def post():
    return jsonify(new_banks)



# print(new_banks)