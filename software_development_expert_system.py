from experta import *

diseases_list = []
diseases_symptoms = []
symptom_map = {}
d_desc_map = {}
d_treatment_map = {}

def preprocess():
	global diseases_list,diseases_symptoms,symptom_map,d_desc_map,d_treatment_map
	diseases = open("errors.txt")
	diseases_t = diseases.read()
	diseases_list = diseases_t.split("\n")
	diseases.close()
	for disease in diseases_list:
		disease_s_file = open("Inference/" + disease + ".txt")
		disease_s_data = disease_s_file.read()
		s_list = disease_s_data.split("\n")
		diseases_symptoms.append(s_list)
		symptom_map[str(s_list)] = disease
		disease_s_file.close()
		disease_s_file = open("Descriptions/" + disease + ".txt")
		disease_s_data = disease_s_file.read()
		d_desc_map[disease] = disease_s_data
		disease_s_file.close()
		disease_s_file = open("Solution/" + disease + ".txt")
		disease_s_data = disease_s_file.read()
		d_treatment_map[disease] = disease_s_data
		disease_s_file.close()
	

def identify_disease(*arguments):
	symptom_list = []
	for symptom in arguments:
		symptom_list.append(symptom)
	# Handle key error
	return symptom_map[str(symptom_list)]

def get_details(disease):
	return d_desc_map[disease]

def get_treatments(disease):
	return d_treatment_map[disease]

def if_not_matched(disease):
		print("")
		id_disease = disease
		disease_details = get_details(id_disease)
		treatments = get_treatments(id_disease)
		# print("")
		# print("La enfermedad más probable que padeces es %s\n" %(id_disease))
		# print("A continuación se ofrece una breve descripción de la enfermedad :\n")
		# print(disease_details+"\n")
		# print("Los medicamentos y procedimientos comunes sugeridos por otros médicos reales son: \n")
		# print(treatments+"\n")
		response = ""
		response = "El error más probable que tiene en el código es %s\n" %(id_disease)
		response = "A continuación se ofrece una breve descripción del concepto por el que se está generando el error:\n"
		response = disease_details+"\n"
		response = "Los procedimientos comunes sugeridos para corregir el error: \n"
		response = treatments+"\n"
		return response

# @my_decorator is just a way of saying just_some_function = my_decorator(just_some_function)
#def identify_disease(headache, back_pain, chest_pain, cough, fainting, sore_throat, fatigue, restlessness,low_body_temp ,fever,sunken_eyes):
class Greetings(KnowledgeEngine):
	def __init__(self, dict_sintomas):
		super().__init__()
		self.dic_inference = dict_sintomas
		self.response_1 = ""
	
	@DefFacts()
	def _initial_action(self):
		# print("")
		# print("Hola! Soy la Ing. Martha, estoy aquí para ayudarte a resolver tus problemas de programación de sistemas")
		# print("Para ello tendrás que responder a algunas preguntas sobre tu desarrollo")
		# input("¿estás listo para empezar? Presiona cualquier tecla para continuar")
		# print("")
		
		yield Fact(action="find_disease")


	@Rule(Fact(action='find_disease'), NOT(Fact(headache=W())),salience = 1)
	def symptom_0(self):
		self.declare(Fact(headache=self.dic_inference['object']))

	@Rule(Fact(action='find_disease'), NOT(Fact(back_pain=W())),salience = 1)
	def symptom_1(self):
		self.declare(Fact(back_pain=self.dic_inference['back_pain']))

	@Rule(Fact(action='find_disease'), NOT(Fact(chest_pain=W())),salience = 1)
	def symptom_2(self):
		self.declare(Fact(chest_pain=self.dic_inference['chest_pain']))

	@Rule(Fact(action='find_disease'), NOT(Fact(cough=W())),salience = 1)
	def symptom_3(self):
		self.declare(Fact(cough=self.dic_inference['cough']))

	@Rule(Fact(action='find_disease'), NOT(Fact(fainting=W())),salience = 1)
	def symptom_4(self):
		self.declare(Fact(fainting=self.dic_inference['fainting']))

	@Rule(Fact(action='find_disease'), NOT(Fact(fatigue=W())),salience = 1)
	def symptom_5(self):
		self.declare(Fact(fatigue=self.dic_inference['fatigue']))
	 
	@Rule(Fact(action='find_disease'), NOT(Fact(sunken_eyes=W())),salience = 1)
	def symptom_6(self):
		self.declare(Fact(sunken_eyes=self.dic_inference['sunken_eyes']))
	
	@Rule(Fact(action='find_disease'), NOT(Fact(low_body_temp=W())),salience = 1)
	def symptom_7(self):
		self.declare(Fact(low_body_temp=self.dic_inference['low_body_temp']))
	
	@Rule(Fact(action='find_disease'), NOT(Fact(restlessness=W())),salience = 1)
	def symptom_8(self):
		self.declare(Fact(restlessness=self.dic_inference['restlessness']))
	
	@Rule(Fact(action='find_disease'), NOT(Fact(sore_throat=W())),salience = 1)
	def symptom_9(self):
		self.declare(Fact(sore_throat=self.dic_inference['sore_throat']))
	
	@Rule(Fact(action='find_disease'), NOT(Fact(fever=W())),salience = 1)
	def symptom_10(self):
		self.declare(Fact(fever=self.dic_inference['fever']))

	@Rule(Fact(action='find_disease'), NOT(Fact(nausea=W())),salience = 1)
	def symptom_11(self):
		self.declare(Fact(nausea=self.dic_inference['nausea']))

	@Rule(Fact(action='find_disease'), NOT(Fact(blurred_vision=W())),salience = 1)
	def symptom_12(self):
		self.declare(Fact(blurred_vision=self.dic_inference['blurred_vision']))

	# @Rule(Fact(action='find_disease'),Fact(headache="no"),Fact(back_pain="no"),Fact(chest_pain="no"),Fact(cough="no"))
	@Rule(Fact(action='find_disease'),Fact(headache="no"),Fact(back_pain="no"),Fact(chest_pain="no"),Fact(cough="no"),Fact(fainting="no"),Fact(sore_throat="no"),Fact(fatigue="yes"),Fact(restlessness="no"),Fact(low_body_temp="no"),Fact(fever="yes"),Fact(sunken_eyes="no"),Fact(nausea="yes"),Fact(blurred_vision="no"))
	def disease_0(self):
		print("Ingresa a Objeto")
		self.declare(Fact(disease="Objeto"))

	# @Rule(Fact(action='find_disease'),Fact(headache="no"),Fact(back_pain="no"),Fact(chest_pain="no"),Fact(cough="no"),Fact(fainting="no"),Fact(sore_throat="no"),Fact(fatigue="no"),Fact(restlessness="yes"),Fact(low_body_temp="no"),Fact(fever="no"),Fact(sunken_eyes="no"),Fact(nausea="no"),Fact(blurred_vision="no"))
	# def disease_1(self):
	# 	self.declare(Fact(disease="Alzheimers"))

	# @Rule(Fact(action='find_disease'),Fact(headache="no"),Fact(back_pain="yes"),Fact(chest_pain="no"),Fact(cough="no"),Fact(fainting="no"),Fact(sore_throat="no"),Fact(fatigue="yes"),Fact(restlessness="no"),Fact(low_body_temp="no"),Fact(fever="no"),Fact(sunken_eyes="no"),Fact(nausea="no"),Fact(blurred_vision="no"))
	# def disease_2(self):
	# 	self.declare(Fact(disease="Arthritis"))

	# @Rule(Fact(action='find_disease'),Fact(headache="no"),Fact(back_pain="no"),Fact(chest_pain="yes"),Fact(cough="yes"),Fact(fainting="no"),Fact(sore_throat="no"),Fact(fatigue="no"),Fact(restlessness="no"),Fact(low_body_temp="no"),Fact(fever="yes"),Fact(sunken_eyes="no"),Fact(nausea="no"),Fact(blurred_vision="no"))
	# def disease_3(self):
	# 	self.declare(Fact(disease="Tuberculosis"))


	@Rule(Fact(action='find_disease'),Fact(disease=MATCH.disease),salience = -998)
	def disease(self, disease):
		# print("")
		id_disease = disease
		disease_details = get_details(id_disease)
		treatments = get_treatments(id_disease)
		self.response_1 = ""
		self.response_1 += "El error más probable que tiene en el código es %s\n" % id_disease
		self.response_1 += "A continuación se ofrece una breve descripción del problema:\n"
		self.response_1 += disease_details + "\n"
		self.response_1 += "Los procedimientos sugeridos para corregir el error son:\n"
		self.response_1 += treatments + "\n"
		

	@Rule(Fact(action='find_disease'),
		  Fact(headache=MATCH.headache),
		  Fact(back_pain=MATCH.back_pain),
		  Fact(chest_pain=MATCH.chest_pain),
		  Fact(cough=MATCH.cough),
		  Fact(fainting=MATCH.fainting),
		  Fact(sore_throat=MATCH.sore_throat),
		  Fact(fatigue=MATCH.fatigue),
		  Fact(low_body_temp=MATCH.low_body_temp),
		  Fact(restlessness=MATCH.restlessness),
		  Fact(fever=MATCH.fever),
		  Fact(sunken_eyes=MATCH.sunken_eyes),
		  Fact(nausea=MATCH.nausea),
		  Fact(blurred_vision=MATCH.blurred_vision),NOT(Fact(disease=MATCH.disease)),salience = -999)

	# def not_matched(self,headache, back_pain, chest_pain, cough):
	def not_matched(self, headache, back_pain, chest_pain, cough, fainting, sore_throat, fatigue, restlessness,low_body_temp ,fever ,sunken_eyes ,nausea ,blurred_vision):
		self.response_1 = ""
		self.response_1 += "\nNo se ha encontrado un error que tenga una coincidencia exacta.\n\nIntente descartar el siguiente caso.\n\n"
		#print("\nNo se ha encontrado un error que tenga una coincidencia exacta.\n Intente descartar el siguiente caso.\n")
		lis = [headache, back_pain, chest_pain, cough, fainting, sore_throat, fatigue, restlessness,low_body_temp ,fever ,sunken_eyes ,nausea ,blurred_vision]
		# lis = [headache, back_pain, chest_pain, cough]
		max_count = 0
		max_disease = ""
		for key,val in symptom_map.items():
			count = 0
			temp_list = eval(key)
			for j in range(0,len(lis)):
				if(temp_list[j] == lis[j] and lis[j] == "yes"):
					count = count + 1
			if count > max_count:
				max_count = count
				max_disease = val
		self.response_1 += if_not_matched(max_disease)

def main():
	# Obtener la ruta del directorio actual
	import os
	current_dir = os.getcwd()
	# print(current_dir)

	preprocess()
	engine = Greetings()
	# while(1):
	# 	engine.reset()  # Prepare the engine for the execution.
	# 	engine.run()  # Run it!
	# 	print("¿Le gustaría diagnosticar otros síntomas?")
	# 	if input() == "no":
	# 		exit()
		#print(engine.facts)
	

def experto(dic_inference):
	print('Inicia el programa')

	preprocess()
	engine = Greetings(dict_sintomas=dic_inference)
	engine.reset()  # Prepare the engine for the execution.
	engine.run()  # Run it!
	# print(engine.response_1)
	response = engine.response_1
	print(response)
	return response

if __name__ == "__main__":
	
	# disease = "Objeto"
	dic_inference = {
		"object": "no",
		"back_pain": "no",
		"chest_pain": "no",
		"cough": "no",
		"fainting": "no",
		"fatigue": "yes",
		"sunken_eyes": "no",
		"low_body_temp": "no",
		"restlessness": "no",
		"sore_throat": "no",
		"fever": "yes",
		"nausea": "yes",
		"blurred_vision": "no"
		}
	
	# disease = "No objeto"
	# dic_inference = {
	dic_inference = {
		"object": "no",
		"back_pain": "no",
		"chest_pain": "no",
		"cough": "no",
		"fainting": "no",
		"fatigue": "yes",
		"sunken_eyes": "no",
		"low_body_temp": "no",
		"restlessness": "no",
		"sore_throat": "no",
		"fever": "no",
		"nausea": "no",
		"blurred_vision": "no"
		}



	experto(dic_inference)
	
	# main()
