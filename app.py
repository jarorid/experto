from flask import Flask
from flask import jsonify

app = Flask(__name__)
app.debug = True

@app.route('/')
def hello():
    return 'Hello World'

#crea un endpoint que una cadena de texto y la devuelva en mayusculas
@app.route('/mayusculas/<string:cadena>', methods=['GET'])
def mayusculas(cadena): 
    print (cadena)
    cadena = cadena.upper()
    print (cadena)
    return jsonify({"resultado": cadena})


#crea un endpoint que reciba dos numeros y los sume
@app.route('/sumar/<int:numero1>/<int:numero2>', methods=['GET'])
def sumar(numero1, numero2):
    suma = numero1 + numero2
    print (suma)
    return jsonify({"resultado": suma})

if __name__ == '__main__':
    app.run()

