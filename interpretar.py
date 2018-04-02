
#1,2,<0>,3,0,<1>,1,2,<0>,3,0,<1>,3,0,<1>,3,0,<1>,3,0,<1>,3,0,<1>,3,0,<1>,2,1,<1>,3,0,<1>,2,1,<1>,3,0,<1>,3,0,<1>,2,1,<1>,3,0,<1>

z=['U1C','U2C','U3C','U4C','U1T','U2T','U3T','U4T','U1I','U2I','U3I','U4I','U1M','U2M','U3M','U4M']


def interpretar(x):
	i=2
	#print (x)
	y=[]
	while i < len(x[0]):
		if x[0,i]> 0.0:
			y.append('-')
			print(x[0,i])
		else:
			y.append('Reforzar')
			print(x[0,i])
		i=i+3
	i=0
	while i < len(z): 
		print (y[i],z[i])
		i=i+1