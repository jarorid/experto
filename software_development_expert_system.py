from experta import *

error_list = []
error_inference = []
inference_map = {}
d_desc_map = {}
d_solution_map = {}

def preprocess():
	global error_list,error_inference,inference_map,d_desc_map,d_solution_map
	errors = open("errors.txt")
	errors_t = errors.read()
	error_list = errors_t.split("\n")
	errors.close()
	for error in error_list:
		error_s_file = open("Inference/" + error + ".txt")
		error_s_data = error_s_file.read()
		s_list = error_s_data.split("\n")
		error_inference.append(s_list)
		inference_map[str(s_list)] = error
		error_s_file.close()
		error_s_file = open("Descriptions/" + error + ".txt")
		error_s_data = error_s_file.read()
		d_desc_map[error] = error_s_data
		error_s_file.close()
		error_s_file = open("Solution/" + error + ".txt")
		error_s_data = error_s_file.read()
		d_solution_map[error] = error_s_data
		error_s_file.close()
	

def identify_error(*arguments):
	inference_list = []
	for caso in arguments:
		inference_list.append(caso)
	# Handle key error
	return inference_map[str(inference_list)]

def get_details(error):
	return d_desc_map[error]

def get_solution(error):
	return d_solution_map[error]

def if_not_matched(error):
		print("")
		id_error = error
		error_details = get_details(id_error)
		solution = get_solution(id_error)
		response = ""
		response += "El error más probable que tiene en el código es %s\n\n" %(id_error)
		response += "\nA continuación se ofrece una breve descripción del concepto por el que se está generando el error:\n"
		response += error_details+"\n"
		response += "Los procedimientos comunes sugeridos para corregir el error: \n"
		solution += solution+"\n"
		return response

class Greetings(KnowledgeEngine):
	def __init__(self, dict_sintomas):
		super().__init__()
		self.dic_inference = dict_sintomas
		self.response_1 = ""
	
	@DefFacts()
	def _initial_action(self):
		yield Fact(action="find_error")

	@Rule(Fact(action='find_error'), NOT(Fact(objeto=W())),salience = 1)
	def inference_0(self):
		self.declare(Fact(objeto=self.dic_inference['objeto']))
	
	@Rule(Fact(action='find_error'), NOT(Fact(constructor=W())),salience = 1)
	def inference_1(self):
		self.declare(Fact(constructor=self.dic_inference['constructor']))
	
	@Rule(Fact(action='find_error'), NOT(Fact(atributoYmetodos=W())),salience = 1)
	def inference_2(self):
		self.declare(Fact(atributoYmetodos=self.dic_inference['atributoYmetodos']))
	
	@Rule(Fact(action='find_error'), NOT(Fact(instanciado=W())),salience = 1)
	def inference_3(self):
		self.declare(Fact(instanciado=self.dic_inference['instanciado']))

	@Rule(Fact(action='find_error'), Fact(objeto="yes"), Fact(constructor="no"), Fact(atributoYmetodos="no"), Fact(instanciado="no"))
	def case_0(self):
		self.declare(Fact(error="Objeto"))

	# Falla la prueba
	@Rule(Fact(action='find_error'), Fact(objeto="no"), Fact(constructor="yes"), Fact(atributoYmetodos="no"), Fact(instanciado="no"))
	def case_1(self):
		self.declare(Fact(error="Constructor"))

	# Falla la prueba
	@Rule(Fact(action='find_error'), Fact(objeto="no"), Fact(constructor="no"), Fact(atributoYmetodos="yes"), Fact(instanciado="no"))
	def case_1(self):
		self.declare(Fact(error="AtributoYmetodos"))

	@Rule(Fact(action='find_error'), Fact(objeto="no"), Fact(constructor="no"), Fact(atributoYmetodos="no"), Fact(instanciado="yes"))
	def case_1(self):
		self.declare(Fact(error="Instanciado"))


	@Rule(Fact(action='find_error'),Fact(error=MATCH.error),salience = -998)
	def problema(self, error):
		id_error = error
		error_details = get_details(id_error)
		solution = get_solution(id_error)
		self.response_1 = ""
		self.response_1 += "El error más probable que tiene en el código es %s\n" % id_error
		self.response_1 += "A continuación se ofrece una breve descripción del problema:\n\n"
		self.response_1 += error_details + "\n"
		self.response_1 += "Los procedimientos sugeridos para corregir el error son:\n"
		self.response_1 += solution + "\n"
		
	@Rule(Fact(action='find_error'),
		  Fact(objeto=MATCH.objeto),
		  Fact(constructor=MATCH.constructor),
		  Fact(atributoYmetodos=MATCH.atributoYmetodos),
		  Fact(instanciado=MATCH.instanciado),
		  NOT(Fact(error=MATCH.error)),salience = -999)

	
	def not_matched(self, objeto, constructor, atributoYmetodos, instanciado):
		self.response_1 = ""
		self.response_1 += "\n!!!!No se ha encontrado un error que tenga una coincidencia exacta.\n\nIntente descartar el siguiente caso.\n\n"
		lis = [objeto, constructor, atributoYmetodos, instanciado]
		max_count = 0
		max_inference = ""
		for key,val in inference_map.items():
			count = 0
			temp_list = eval(key)
			for j in range(0,len(lis)):
				if(temp_list[j] == lis[j] and lis[j] == "yes"):
					count = count + 1
			if count > max_count:
				max_count = count
				max_inference = val
		self.response_1 += if_not_matched(max_inference)
	

def experto(dic_inference):
	preprocess()
	engine = Greetings(dict_sintomas=dic_inference)
	engine.reset()  # Prepare the engine for the execution.
	engine.run()  # Run it!
	response = engine.response_1
	print(response)
	return response

if __name__ == "__main__":
	
	# error = "Objeto"
	dic_inference = {
		"objeto": "yes",
		"constructor": "no",
		"atributoYmetodos": "no",
		"instanciado": "no"
		}
	
	# error = "No objeto"
	dic_inference = {
		"objeto": "no",
		"constructor": "yes",
		"atributoYmetodos": "no",
		"instanciado": "no"
		}

	experto(dic_inference)
