import sys
import redis
from flask import Flask, request
from datetime import datetime

app = Flask(__name__)
rTimeStamps = redis.Redis(host='localhost', port=6379, db=0)
rUsername = redis.Redis(host='localhost', port=6379, db=1)

@app.route('/flipByTime/<author>/<flip>', methods=['POST']) #vérifier quel méthode utiliser
def flipByTime(flip,author):  
    if request.method == 'POST':
        key = datetime.now()
        rTimeStamps.lpush( key, "author: " +  author + "flip: " + flip)
    return 0

@app.route('/flipByName/<author>/<flip>', methods=['POST']) #vérifier quel méthode utiliser
def flipByName(author):  
    if request.method == 'POST':
        key = author
        timeStamp = rUsername.lrange(key,0,-1)
        timeStamp += datetime.now()
        rTimeStamps.lpush(key, timeStamp)
    return 0
    








if __name__ == '__main__':
    if len(sys.argv) > 1:
        if sys.argv[1] == "check_syntax":
            print("Build [ OK ]")
            exit(0)
        else:
            print("Passed argument not supported ! Supported argument : check_syntax")
            exit(1)
    app.run(debug=True)
