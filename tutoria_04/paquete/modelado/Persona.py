class Persona:#Clase persona
	def __init__(self): # se define el __init__  con las variables a utilizar
		self.nombres = ""
		self.edad = 0
	def agregar_nombres(self, n):  # agregamos la variable nombre
		self. nombres = n
	
	def obtener_nombres(self): #obtener nombre (retorna el valor) STRING
		return self.nombres
	
	def agregar_edad(self, d): # agregamos la variable edad
		self. edad = d
	
	def obtener_edad(self): #obtener edad (retorna el valor) INT
		return self.edad
	
	def presentar (self): #en esta funcion presentamos los datos obtenidos 
		c = ("%d - %s" %(self.obtener_edad(),self.nombres)) # cadena donde  se le agrega los valores
		return c #retornamos la cadena


class estudiante(Persona):# Clase estudiante que utiliza elementos de la clase Persona
	def __init__(self):# se define el __init__  con las variables a utilizar
		super(estudiante,self).__init__() #utilizamos el super para ocupar las funciones de la clase Persona
		self.nota = 0
	def agregar_nota(self, a):# agregamos la variable nota
		self. nota = a
	
	def obtener_nota(self):#obtener nota (retorna el valor) INT
		return nota
	
	def presentar_d(self): #Presentamo los valores
		#c = "%s - %s - %s" %(self.nombres,self.edad,self.nota):
		c = "%s - %s" %(super(estudiante,self).presentar(),self.nota)  # cadena donde  se le agrega los valores
		return c #retornamos la cadena

		