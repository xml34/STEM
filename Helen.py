#! /usr/bin/env python
import numpy
from sklearn import tree  #esta libreria nos afrece el arbol 

from sklearn.tree import export_graphviz #esta libreria nos ofrece la opcion de graficar el arbol
import graphviz
import interpretar as inter  
import matplotlib.pyplot as plt 
import numpy as np  #nos ofrece la opcion de crear vectores y matrices

atributos=[]#tendra los datos del desempeno del estudiante
entidad=[]#tendra los datos personales del estu.

with open('dataSet.csv') as f:  #abre el archivo donde estan los 60 datos por estudiante
	for line in f:  # por cada iteracion carga en f linea a linea el archivo
		cont = 0
		temp = line.strip()  #quita especios adelante y atras de cada linea
		array = temp.split(',')  # separa la lina por ',' y cada uno de estas particiones las guarda como elementos en un arreglo
		entidad.append(array[0:11]) # toma los primeros datos los cuales corresponden a datos personales
		atributos.append(array[11:len(array)]) #toma los datos resptantes correspondientes al desempeno

clasif = tree.DecisionTreeClassifier() 
clasif = clasif.fit(entidad,atributos) #entrena al modelo con los datos
probar()
#este metodo a traves de 11 datos predice el desempeno del estudiante
class probar:
	flag=True
	while flag: 
		print('>')
		inp=input() #recibe los 11 datos separados por ','
		if inp == "exit":
			flag = False
		else:
			x=clasif.predict([inp]) #separa los 11 datos 
			#inter.interpretar(x) # predice el desempeno	
			print(x)


