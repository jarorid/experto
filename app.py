from flask import Flask
import subprocess
from flask import jsonify
from flask import request
import asyncio

import software_development_expert_system as expert_system

app = Flask(__name__)

@app.route('/')
def hello():
    '''curl http://localhost:5000/'''
    preguntas = {
        'object': '¿tiene declarado el objeto?',
        'constructor': '¿tiene la función denominada constructor?',
        'declaration': '¿Declaró los atributos y metodos del objeto?',
        'instance': '¿Ya se encuentra instanciado el objeto?'
    }
    return jsonify(preguntas)

@app.route('/endpoint', methods=['POST'])
def recibir_json():
    data = request.get_json()
    if not data:
        return jsonify({'error': 'JSON no encontrado'}), 400
    
    required_keys = [
        'object', 'back_pain', 'chest_pain', 'cough', 'fainting',
        'fatigue', 'sunken_eyes', 'low_body_temp', 'restlessness',
        'sore_throat', 'fever', 'sunken_eyes', 'nausea', 'blurred_vision'
    ]
    
    if not all(key in data for key in required_keys):
        return jsonify({'error': 'Estructura JSON no valida'}), 400
    
    valid_values = ['yes', 'no']
    if any(data[key] not in valid_values for key in required_keys):
        return jsonify({'error': 'Valores no validos en el JSON'}), 400
    
    response = expert_system.experto(data)
    # print (response)
    
    return response, 400


if __name__ == '__main__':
    app.run(port=5000)

'''Caso de prueba Hypotermia

curl -X POST -H "Content-Type: application/json" -d '{
   "object": "no",
   "back_pain": "no",
   "chest_pain": "no",
   "cough": "no", 
   "fainting": "yes",
   "fatigue": "no", 
   "sunken_eyes": "no",
   "low_body_temp": "yes",
   "restlessness": "no",
   "sore_throat": "no",
   "fever": "no", 
   "sunken_eyes":"no",
   "nausea": "no",
   "blurred_vision": "no"
}' http://localhost:5000/endpoint

Caso de prueba sin match

curl -X POST -H "Content-Type: application/json" -d '{
   "headache": "no",
   "back_pain": "no",
   "chest_pain": "no",
   "cough": "no", 
   "fainting": "yes",
   "fatigue": "no", 
   "sunken_eyes": "no",
   "low_body_temp": "no",
   "restlessness": "no",
   "sore_throat": "no",
   "fever": "no", 
   "sunken_eyes":"no",
   "nausea": "no",
   "blurred_vision": "no"
}' http://localhost:5000/endpoint

Caso de prueba sin alguna llave

curl -X POST -H "Content-Type: application/json" -d '{
   "headache": "no",
   "back_pain": "no",
   "chest_pain": "no",
   "cough": "no", 
   "fatigue": "no", 
   "sunken_eyes": "no",
   "low_body_temp": "no",
   "restlessness": "no",
   "sore_throat": "no",
   "fever": "no", 
   "sunken_eyes":"no",
   "nausea": "no",
   "blurred_vision": "no"
}' http://localhost:5000/endpoint

Caso de prueba sin datos validos 

curl -X POST -H "Content-Type: application/json" -d '{
   "headache": "manzana",
   "back_pain": "no",
   "chest_pain": "no",
   "cough": "no", 
   "fainting": "yes",
   "fatigue": "no", 
   "sunken_eyes": "Hola Jahir",
   "low_body_temp": "no",
   "restlessness": "no",
   "sore_throat": "no",
   "fever": "no", 
   "sunken_eyes":"no",
   "nausea": "no",
   "blurred_vision": "no"
}' http://localhost:5000/endpoint

'''