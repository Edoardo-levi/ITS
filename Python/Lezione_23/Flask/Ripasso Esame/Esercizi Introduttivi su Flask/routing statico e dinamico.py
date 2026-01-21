from flask import *

app = Flask (__name__)

@app.route('/users/<string:nome>')
def benvenuto (nome:str) -> str:
    return f"Benvenuto, {nome}"

@app.route('/square/<int:num>')
def numero(num:int) -> int:
   return f"n= {num}, n al quadrato = {num**num}"

@app.route('/sum/<int:a>/<int:b>')
def sum(a:int,b:int) -> int:
    return f"a={a} <br>\
        b={b}<br>\
        La somma tra {a} e {b} e'= {a+b}"



if __name__ =='__main__':
 app.run (debug=True)