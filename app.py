import sys
from flask import Flask, request

app = Flask(__name__)

dictionary_add = dict()
dictionary_sub = dict()
dictionary_mul = dict()
dictionary_div = dict()

@app.route('/add/<int:value1>/<int:value2>', methods=['POST'])
def add(value1, value2):
    
    result_add = int(value1) + int(value2)
    if request.method == 'POST':
        dictionary_add[len(dictionary_add)] = result_add
        id_add = len(dictionary_add)
        ret = "The result of the addition is " + str(result_add) + " ; id resultat = " + str(id_add) + "\n" 
    return ret

@app.route('/sub/<int:value1>/<int:value2>', methods=['POST'])
def sub(value1, value2):
    
    result_sub = int(value1) - int(value2)
    if request.method == 'POST':
        dictionary_sub[len(dictionary_sub)] = result_sub
        id_sub = len(dictionary_sub)
        ret = "The result of the addition is " + str(result_sub) + " ; id resultat = " + str(id_sub) + "\n" 
    return ret

@app.route('/mul/<int:value1>/<int:value2>', methods=['POST'])
def mul(value1, value2):
    
    result_mul = int(value1) * int(value2)
    if request.method == 'POST':
        dictionary_mul[len(dictionary_mul)] = result_mul
        id_mul = len(dictionary_mul)
        ret = "The result of the addition is " + str(result_mul) + " ; id resultat = " + str(id_mul) + "\n" 
    return ret

@app.route('/div/<int:value1>/<int:value2>', methods=['POST'])
def div(value1, value2):
    
    result_div = int(value1) / int(value2)
    if request.method == 'POST':
        dictionary_div[len(dictionary_div)] = result_div
        id_div = len(dictionary_div)
        ret = "The result of the addition is " + str(result_div) + " ; id resultat = " + str(id_div) + "\n" 
    return ret



"""
@app.route("/sub", methods=['POST'])
def sub():
    if request.method == 'POST':
		# values is a combinaison of form and args data
        value1 = int(request.values.get('value1'))
        value2 = int(request.values.get('value2'))
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