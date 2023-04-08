import sys
import json
import re
from datetime import datetime
import redis
from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

rTimestamps = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)
rUsername = redis.Redis(host='localhost', port=6379, db=1,decode_responses=True)


@app.route('/flip/<author>/<flip>', methods=['POST'])
def flip_by_time(author,flip):
    """enregiste les flips par auteurs et timestamp"""
    if request.method == 'POST':
        timestamp = str(datetime.now())
        content = {
            "flip" : flip,
            "author" : author,
        }
        rUsername.set(timestamp, json.dumps(content))
        rTimestamps.lpush( "u-"+author, timestamp)
        patternhashtag = r"(?<!\w)#[A-Za-z0-9]+(?![A-Za-z0-9]*#)" #regex du sujet
        sujets = re.findall(patternhashtag, flip) #application regex 2
        if sujets:
            for sujet in sujets:
                rTimestamps.lpush("h-"+ sujet, timestamp)
    response = jsonify({"message": "Flip ajouté avec succès"})
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

@app.route('/getAllFlip', methods=['GET'])
def get_flip():
    """récupère l'ensemble des flips"""
    if request.method == 'GET':
        flips = []
        for key in rUsername.scan_iter("*"):
            flip = json.loads(rUsername.get(key))
            flips.append(flip)
            response = jsonyfy(flips).headers.add('Access-Control-Allow-Origin', '*')
    return flips #ca marche

@app.route('/getFlipByUser/<author>', methods=['GET'])
def get_flip_by_user(author):
    """récupère l'ensemble des flips provennant d'un utilisateur"""
    if request.method == 'GET':
        timestamps = rTimestamps.lrange("u-" + author,0,-1) #récupère l'ensemle des timestamps des flips d'une personne
        flip_by_user = []
        for timestamp in timestamps:
            flip = json.loads(rUsername.get(timestamp))
            flip_by_user.append(flip)
    return json.dumps(flip_by_user) #renvoie le tableau avec les flip d'un user

@app.route('/getAllSubject', methods=['GET'])
def get_subject():
    """récupère l'ensemble des sujets"""
    if request.method == 'GET':
        keys = rTimestamps.keys('h-*')
        sujets = []
        for key in keys:
            sujets.append(key[2:])
    return json.dumps(sujets)

@app.route('/getFlipByHashtag/<sujet>', methods=['GET'])
def get_flip_by_subject(sujet):
    """récupère tous les flips qui correspondent à un sujet"""
    if request.method == 'GET':
        timestamps = rTimestamps.lrange("h-" + sujet,0,-1) #récupère l'ensemle des timestamps des flips d'une personne
        flip_by_hashtag = []
        for timestamp in timestamps:
            flip = json.loads(rUsername.get(timestamp))
            flip_by_hashtag.append(flip)
    return json.dumps(flip_by_hashtag) #renvoie le tableau avec les flip d'un sujet

@app.route('/Reflip/<flipper>/<reflipper>/<reflipped>', methods=['POST'])
def reflip(flipper,reflipper,reflipped):
    """une route qui permet de préciser un reflip et qui à reflip"""
    if request.method == 'POST':
        content = {
            "flip" : reflipped,
            "author" : flipper,
            "refliper": reflipper
        }
        timestamp = str(datetime.now())
        rUsername.set(timestamp, json.dumps(content))
        rTimestamps.lpush( "u-"+ reflipper, timestamp)
        patternhashtag = r"(?<!\w)#[A-Za-z0-9]+(?![A-Za-z0-9]*#)" #regex du sujet
        sujets = re.findall(patternhashtag, reflipped) #application regex 2
        if sujets:
            for sujet in sujets:
                rTimestamps.lpush("h-"+ sujet, timestamp)
    return 'hello \n'


if __name__ == '__main__':
    if len(sys.argv) > 1:
        if sys.argv[1] == "check_syntax":
            print("Build [ OK ]")
            exit(0)
        else:
            print("Passed argument not supported ! Supported argument : check_syntax")
            exit(1)
    app.run(debug=True)
