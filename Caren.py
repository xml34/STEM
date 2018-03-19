import numpy
from sklearn import tree 

archTrai = open("trainingData.txt","w")
archLearn = open("learnData.txt","w")

learString= "["
trainingString="["

with open('dataSet.csv') as f:
	for line in f:
		coma1=","
		coma2=","
		learString= learString + "["
		trainingString= trainingString + "["
		cont = 0
		array = line.split(',')
		for dato in array:
			cont = cont +1	
			if cont < 12:
				if cont == 11:
					coma1 = ""
				learString = learString + dato.strip() + coma1
			else:
				if len(array) == cont:
					coma2=""	
				trainingString = trainingString + dato.strip() + coma2
		learString=learString+ "],"
		trainingString=trainingString+"],"
	size =len(learString)
	temp=learString[:size-2]
	learString=temp+"]]"

	size =len(trainingString)
	temp=trainingString[:size-2]
	trainingString=temp+"]]"

archLearn.write(learString)		
archTrai.write(trainingString)		
