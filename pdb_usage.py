def fact(x):
	f = 1
	for i in range(1,x+1):
		print(i)
		f = f * i
	return f 


if __name__ == "__main_":
	print("factorial of 3 = ", fact(3))


''' for debugging the above code with the use of pdb library'''
#write the below code at the command prompt to debug the file 'pdb_usage.py'
#python -m pdb pdb_usage.py