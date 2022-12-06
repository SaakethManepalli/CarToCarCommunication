from flask import Flask, jsonify, request,send_file

app = Flask()

@app.route('/lol', method = ['GET'])

def hello():

    return "Hello world!"