# STEM

# This project is still under development


Science, Technology, Engineering, Maths.

VR+Artificial Intelligence application developed for the subject integrative project 2.

This repository only contains the Artificial Intelligence module made with python.

THe project uses its main class Predictor, please ignore the others and you must run it with the probar class


Caren:
	takes a file with 60 characters, example:
	12,34,223,212,1,0,34,131,123, ... ,3

	then it divides the collected data in two groups, 
	the first contains 11 characters and the other 49.
	it generates 2 files
	(trainingData=49 characters y LearnData=11 characters)
	in those files it writes the data like this
	[[12,34,223,212],[1,0,34,131]]

Helen: 
	
	this class get both files generated with Caren.
	with those characters it train the model
	then in an infinite cycle it receives 11 data and predicts the performance
	based on this data.

Predictor:
	This class has the following methods: 
	train: train the model with 2 given arrays of 11 and 49 characters
	predict: predicts the performance of a student based on 11 personal characters.
	interpret: interprets the predicted obtained.
	try: receive 20% of the data and calculate how accurate the model is

	to see the generated tree this command must be executed:
	$ python Probar.py
	$ dot -Tpng tree.dot -o tree.png
	$ dot -Tps tree.dot -o tree.ps
