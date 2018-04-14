import numpy  #permite usar arrays
from sklearn import tree  #permite usar arboles de desicion

clasif = tree.DecisionTreeClassifier() #crea un variable con todos los atributos y metodos del arbol clasificador
z=['U1C','U2C','U3C','U4C','U1T','U2T','U3T','U4T','U1I','U2I','U3I','U4I','U1M','U2M','U3M','U4M']

def entrenar(entrada,salida):
	global clasif
	clasif= clasif.fit(entrada,salida) # entrena el modelos con 2 matrices dadas (de 11 y 49 datos)

def predecir(datoPredecir):
	global clasif
	return clasif.predict([datoPredecir]) #predice desempeno en base a un dato entrada

def interpretar(x):	#interpreta la prediccion obtenida, la resive como parametro
	i=2
	y=[]
	while i < len(x[0]):
		if x[0][i]> 0.0:
			y.append('-')
		else:
			y.append('Reforzar')
		i=i+3
	i=0
	while i < len(z): 
		print (y[i],z[i])
		i=i+1

def probar(entrada,salida): #dadas 2 matrices (20% de los datos) prueba que tan preciso es el modelo
	i=0
	cantDatosIguales=0
	for dato in entrada:
		array=predecir(dato)
		if probarIgualdad(array[0],salida[i]):	
			cantDatosIguales=cantDatosIguales+1
		i=i+1
	presicion=(cantDatosIguales+0.0)/(i+0.0)
	return presicion		

def probarIgualdad(array1,array2): #este metodo sirve como apoyo al metodo probar compara 2 arrays
	flag=True
	i=0
	for dato in array1:
		if array1[i]!=array2[i]:
			flag=False
		else:
			print(array1[i],array2[i])
		i=i+1	
	return flag