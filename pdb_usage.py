def fact(x):
	f = 1
	for i in range(1,x+1):
		print(i)
		f = f * i
	return f 


if __name__ == "__main_":
	print("factorial of 3 = ", fact(3))


