import sys
import redis
from flask import Flask, request

app = Flask(__name__)
r = redis.Redis(host='localhost', port=6379, db=0)

@app.route('/flip/<string:flip>', methods=['POST','GET']) #vérifier quel méthode utiliser
def flip(flip):  
    if request.method == 'POST' or request.method == 'GET':
        key = r.dbsize()
        r.set(key,flip)
        ret = "your new flip is " + flip + "\n"
    return ret