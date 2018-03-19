import numpy
from sklearn import tree 

atributos=[]
entidad=[]

with open('dataSet.csv') as f:
	for line in f:
		cont = 0
		temp = line.strip()
		array = temp.split(',')
		entidad.append(array[0:11])
		atributos.append(array[11:len(array)])

clasif = tree.DecisionTreeClassifier()
clasif= clasif.fit(entidad,atributos)

flag=True
while flag:
	print('>')
	inp=input()
	if inp == "exit":
		flag = False
	else:
		print(clasif.predict([inp.split(',')]))


