import sys
import redis
from flask import Flask, request

app = Flask(__name__)
r = redis.Redis(host='localhost', port=6379, db=0) #save flip

@app.route('/flip/<flip>', methods=['POST','GET']) #vérifier quel méthode utiliser
def flipper(flip):  
    if request.method == 'POST':
        key = r.dbsize()
        r.set(key,flip)
        ret = {"flip" :"your new flip is " + flip}
    return ret








if __name__ == '__main__':
    if len(sys.argv) > 1:
        if sys.argv[1] == "check_syntax":
            print("Build [ OK ]")
            exit(0)
        else:
            print("Passed argument not supported ! Supported argument : check_syntax")
            exit(1)
    app.run(debug=True)
