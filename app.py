import sys
from flask import Flask, request

app = Flask(__name__)

dictionary_add = dict()
@app.route('/add/<int:value1>/<int:value2>', methods=['POST'])
def add(value1, value2):
    
    result_add = int(value1) + int(value2)
    if request.method == 'POST':
        dictionary_add[len(dictionary_add)] = result_add
        id_add = len(dictionary_add)
        ret = "The result of the addition is " + str(result_add) + " ; id resultat = " + str(id_add) + "\n" 
    return ret


@app.route("/", methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
		# values is a combinaison of form and args data
        value1 = int(request.form.get("key"))
        ret = ret + " \n You send " + value1 + " under 'key' key :)" 
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