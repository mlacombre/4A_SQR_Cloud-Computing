import sys
import redis
from flask import Flask, request
from flask_cors import CORS
id_cpt = 0
app = Flask(__name__)
r = redis.Redis(host='localhost', port=6379, db=0)


CORS(app)

@app.route('/add/<int:value1>/<int:value2>', methods=['POST'])
def add(value1, value2):  
    result_add = int(value1) + int(value2)
    if request.method == 'POST':  
        if r.get(id_cpt):
            id_cpt = r.get(id_cpt)
        r.set(id_cpt,result_add)
        ret = { "text": "The result of the addition is " + str(result_add) + " ; id resultat = " + str(id_cpt) + "\n" }
        id_cpt +=1
        r.set(id_cpt, id_cpt)
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
        if r.get(id_cpt):
            id_cpt = r.get(id_cpt)
        r.set(id_cpt,result_sub)
        id_cpt += 1
        r.set(id_cpt,id_cpt)
        ret = "The result of the addition is " +str(result_sub)+" ; id resultat = " + str(id_cpt) + "\n" 
    return ret


@app.route('/mul/<int:value1>/<int:value2>', methods=['POST'])
def mul(value1, value2):   
    result_mul = int(value1) * int(value2)
    if request.method == 'POST':
        if r.get(id_cpt):
            id_cpt = r.get(id_cpt)
        r.set(id_cpt,result_mul)
        id_cpt +=1
        r.set(id_cpt,id_cpt)
        ret = "The result of the addition is " + str(result_mul) + " ; id resultat = " + str(id_cpt) + "\n" 
    return ret

@app.route('/div/<int:value1>/<int:value2>', methods=['POST'])
def div(value1, value2):
    result_div = int(value1) / int(value2)
    if request.method == 'POST':
        if r.get(id_cpt):
            id_cpt = r.get(id_cpt)
        key = r.dbsize()
        r.set(key,result_div)
        r.set(id_cpt,id_cpt)
        ret = "The result of the addition is " + str(result_div) + " ; id resultat = " + str(key) + "\n" 
    return ret


"""
@app.route("/sub", methods=['POST'])
def sub():
    if request.method == 'POST':
		# values is a combinaison of form and args data
        value1 = int(request.form.get('value1'))
        value2 = int(request.form.get('value2'))
        result_sub = value1 - value2
        dictionary_sub[len(dictionary_sub)] = result_sub
        id_sub = len(dictionary_sub)
        ret =  "The result of the substraction is " + str(result_sub) + " ; id resultat = " + str(id_sub) + "\n" 
    return ret
"""

if __name__ == '__main__':
    if len(sys.argv) > 1:
        if sys.argv[1] == "check_syntax":
            print("Build [ OK ]")
            exit(0)
        else:
            print("Passed argument not supported ! Supported argument : check_syntax")
            exit(1)
    app.run(debug=True)

