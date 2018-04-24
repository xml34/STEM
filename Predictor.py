import numpy  #permite usar arrays
from sklearn import tree  #permite usar arboles de desicion

from sklearn.tree import export_graphviz #esta libreria nos ofrece la opcion de graficar el arbol
import graphviz
import interpretar as inter
import matplotlib.pyplot as plt
import numpy as np  #nos ofrece la opcion de crear vectores y matrices
import sys


# red=MLPClassifier(max_iter=(10000), hidden_layer_sizes=(1000,1000))
clasif = tree.DecisionTreeClassifier() #crea un variable con todos los atributos y metodos del arbol clasificador
z=['U1C','U2C','U3C','U4C','U1T','U2T','U3T','U4T','U1I','U2I','U3I','U4I','U1M','U2M','U3M','U4M']

def cargarArchivos():
	entidad=[]
	atributos=[]
	with open(sys.argv[1]) as f:  #abre el archivo donde estan los 60 datos por estudiante
		for line in f:  # por cada iteracion carga en f linea a linea el archivo
			cont = 0
			temp = line.strip()  #quita especios adelante y atras de cada linea
			array = temp.split(',')  # separa la lina por ',' y cada uno de estas particiones las guarda como elementos en un arreglo
			entidad.append(array[0:11]) # toma los primeros datos los cuales corresponden a datos personales
			atributos.append(array[11:len(array)]) #toma los datos resptantes correspondientes al desempeno
	global clasif
	clasif= clasif.fit(entidad,atributos) # entrena el modelos con 2 matrices dadas (de 11 y 49 datos)
	imprimir()

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
		cantDatosIguales=cantDatosIguales + probarIgualdad(array[0],salida[i])
		i=i+1
	size=len(salida)*48
	presicion=(cantDatosIguales+0.0)/(size+0.0)
	return presicion

def probarIgualdad(array1,array2): #este metodo sirve como apoyo al metodo probar compara 2 arrays
	cantDatosIgu=0
	i=0
	while i < len(array1):
		a=int(array1[i])
		b=int(array2[i])
		if a == b:
			cantDatosIgu=cantDatosIgu+1
		#else:
			#print(array1[i],array2[i])
		i=i+1
	return cantDatosIgu

def imprimir():
	global clasif
	names=['genero','edad','grado','ciencia','tecnologia',
		'ingenieria','metematica','estrato','madre','padre','hermanos']

	export_graphviz(clasif,out_file='arbol.dot',feature_names=names,
		class_names=['l','m','n','o','p','q','r','s','t','u','v'],impurity=False,filled=True)
	with open('arbol.dot') as f:
		dot_graph=f.read()
	graphviz.Source(dot_graph)
	print("termino")

	plt.barh(range(11),clasif.feature_importances_)
	plt.yticks(np.arange(11),names)
	plt.xlabel('Importacia de la variables')
	plt.ylabel('Variable')
	plt.show()
