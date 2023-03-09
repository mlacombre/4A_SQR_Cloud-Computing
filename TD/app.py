import sys
import redis
from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
r = redis.Redis(host='localhost', port=6379, db=0)

CORS(app)

@app.route('/add/<int:value1>/<int:value2>', methods=['POST'])
def add(value1, value2):  
    result_add = int(value1) + int(value2)
    if request.method == 'POST':
        key = r.dbsize()
        r.set(key,result_add)
        ret = { "text": "The result of the addition is " + str(result_add) + " ; id resultat = " + str(key) + "\n" }
    return ret


@app.route('/get_my_calcul/<int:id>', methods=['GET'])
def get_add(id):
    if request.method == 'GET':
        val = r.get(id)
        ret = "The result of the addition with id " + str(id) + " is : " + str(val) + "\n" 
    return ret


@app.route('/sub/<int:value1>/<int:value2>', methods=['POST'])
def sub(value1, value2):   
    result_sub = int(value1) - int(value2)
    if request.method == 'POST':
        key = r.dbsize()
        r.set(key,result_sub)
        ret = "The result of the addition is " +str(result_sub)+" ; id resultat = " + str(key) + "\n" 
    return ret


@app.route('/mul/<int:value1>/<int:value2>', methods=['POST'])
def mul(value1, value2):   
    result_mul = int(value1) * int(value2)
    if request.method == 'POST':
        key = r.dbsize()
        r.set(key,result_mul)
        ret = "The result of the addition is " + str(result_mul) + " ; id resultat = " + str(key) + "\n" 
    return ret

@app.route('/div/<int:value1>/<int:value2>', methods=['POST'])
def div(value1, value2):
    result_div = int(value1) / int(value2)
    if request.method == 'POST':
        key = r.dbsize()
        r.set(key,result_div)
        ret = "The result of the addition is " + str(result_div) + " ; id resultat = " + str(key) + "\n" 
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

