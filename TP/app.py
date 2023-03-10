import sys
from datetime import datetime
import redis
from flask import Flask, request

app = Flask(__name__)
rTimeStamps = redis.Redis(host='localhost', port=6379, db=0)
rUsername = redis.Redis(host='localhost', port=6379, db=1)

@app.route('/flip/<author>/<flip>', methods=['GET','POST'])
def flip_by_time(flip,author):
    """enregiste les flips par auteurs et timestamp"""
    if request.method == 'POST' or request.method == 'GET':
        key = str(datetime.now())
        rUsername.lpush( key, "author: " +  author + " flip: " + flip)
        timestamp = rUsername.lrange(key,0,-1)
        timestamp +=  key
        rTimeStamps.lpush(author, str(timestamp))
    return 'hello \n'

@app.route('/getAllFlip', methods=['GET','POST'])
def get_flip():
    """récupère l'ensemble des flips"""
    flips = []
    for key in rUsername.scan_iter("*"):
        flip = rUsername.lrange(key,0,-1)
        flips.append(str(flip))
    return flips


if __name__ == '__main__':
    if len(sys.argv) > 1:
        if sys.argv[1] == "check_syntax":
            print("Build [ OK ]")
            exit(0)
        else:
            print("Passed argument not supported ! Supported argument : check_syntax")
            exit(1)
    app.run(debug=True)
