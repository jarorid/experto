from flask import Flask
import subprocess
from flask import jsonify
from flask import request
import asyncio

import medical_expert_system as expert_system

app = Flask(__name__)

@app.route('/')
def hello():
    preguntas = {
        'headache': 'dolor de cabeza',
        'back_pain': 'dolor de espalda',
        'chest_pain': 'dolor en el pecho',
        'cough': 'tos',
        'fainting': 'desmayo',
        'fatigue': 'fatiga',
        'sunken_eyes': 'los ojos hundidos',
        'low_body_temp': 'temperatura corporal baja',
        'restlessness': 'intranquilidad',
        'sore_throat': 'dolor de garganta',
        'fever': 'fiebre',
        'nausea': 'náuseas',
        'blurred_vision': 'visión borrosa'
    }
    return jsonify(preguntas)

@app.route('/endpoint', methods=['POST'])
def recibir_json():
    data = request.get_json()
    if not data:
        return jsonify({'error': 'JSON no encontrado'}), 400
    
    required_keys = [
        'headache', 'back_pain', 'chest_pain', 'cough', 'fainting',
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
   "headache": "no",
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