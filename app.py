from flask import Flask
from flask import jsonify
from flask import request

import medical_expert_system as expert_system

app = Flask(__name__)
app.debug = True

@app.route('/')
def hello():
    return 'Hello World'


@app.route('/mayusculas/<string:cadena>', methods=['GET'])
def mayusculas(cadena): 
    print (cadena)
    cadena = cadena.upper()
    print (cadena)
    return jsonify({"resultado": cadena})



@app.route('/sumar/<int:numero1>/<int:numero2>', methods=['GET'])
def sumar(numero1, numero2):
    suma = numero1 + numero2
    print (suma)
    return jsonify({"resultado": suma})


@app.route('/json', methods=['POST'])
def json():
    """
    Maneja una solicitud POST en la ruta '/json' para procesar datos JSON.

    Se espera que la solicitud contenga datos JSON con la clave 'numero1'.
    El valor asociado con 'numero1' se utiliza para calcular el resultado.

    Returns:
        flask.Response: La respuesta JSON que contiene el resultado calculado.

    Example:
        >>> # Enviar una solicitud POST con datos JSON: {"numero1": 10}
        >>> # La respuesta esperada sería: {"resultado": 10}
        >>> response = client.post('/json', json={"numero1": 10})
        >>> print(response.json)
        {"resultado": 10}
        >>>
        >>> # Ejemplo de solicitud cURL equivalente
        >>> # Enviar una solicitud POST con datos JSON: {"numero1": 20}
        >>> # La respuesta esperada sería: {"resultado": 20}
        >>> curl_command = 'curl -X POST -H "Content-Type: application/json" -d \'{"numero1": 20}\' http://localhost:5000/json'
        >>> response = subprocess.check_output(curl_command, shell=True, text=True)
        >>> print(response)
        {"resultado": 20}
    """
    data = request.get_json()
    resultado = data["numero1"]
    return jsonify({"resultado": resultado})

if __name__ == '__main__':
    # app.run()


    
    expert_system.main()



    

