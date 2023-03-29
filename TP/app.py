import sys
import json
import re
from datetime import datetime
import redis
from flask import Flask, request

app = Flask(__name__)

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
            "Reflip" : False
        }
        rUsername.set( timestamp, json.dumps(content))
        rTimestamps.lpush(author, timestamp)
    return 'hello \n'

@app.route('/getAllFlip', methods=['GET','POST'])
def get_flip():
    """récupère l'ensemble des flips"""
    if request.method == 'POST' or request.method == 'GET':
        flips = []
        for key in rUsername.scan_iter("*"):
            flip = json.loads(rUsername.get(key))
            flips.append(flip["flip"])
    return flips

@app.route('/getFlipByUser/<author>', methods=['GET','POST'])
def get_flip_by_user(author):
    """récupère l'ensemble des flips provennant d'un utilisateur"""
    if request.method == 'POST' or request.method == 'GET':
        timestamps = rTimestamps.lrange(author,0,-1) #récupère l'ensemle des timestamps des flips d'une personne
        flip_by_user = []
        pattern = r"author:.*?flip:\s*(.*)$" #regex pour extraire les flips
        for timestamp in timestamps: 
            flip = rUsername.lrange(timestamp,0,-1) #récupération du flip
            flip = [x.decode() for x in flip]
            match = re.search(pattern, str(flip))# application regex
            flip = match.group(1) #récupère la partie recherché
            flip_by_user.append(flip)
    return json.dumps(flip_by_user) #renvoie le tableau avec les users

@app.route('/getAllSubject', methods=['GET','POST'])
def get_subject():
    """récupère l'ensemble des sujets"""
    if request.method == 'POST' or request.method == 'GET':
        pattern = r"author:.*?flip:\s*(.*)$" #regex du flip
        pattern2 = r"(?<!\w)#[A-Za-z0-9]+(?![A-Za-z0-9]*#)" #regex du sujet
        sujets = []
        for key in rUsername.scan_iter("*"):
            flip = rUsername.lrange(key,0,-1) #tout les flips
            flip = [x.decode() for x in flip] #décode 
            match = re.search(pattern, str(flip))# application regex 1
            flip = match.group(1) #récupère le flip
            match2 = re.findall(pattern2, flip) #application regex 2
            if match2:
                sujets.extend(match2)
    return json.dumps(sujets)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        if sys.argv[1] == "check_syntax":
            print("Build [ OK ]")
            exit(0)
        else:
            print("Passed argument not supported ! Supported argument : check_syntax")
            exit(1)
    app.run(debug=True)


