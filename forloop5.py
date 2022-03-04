n = int(input("Enter number to find factorial: "))

facto = 1

if(n<0):
	print('Enter positive number')
else:
	for i in range(1,n+1):
		facto = facto*i

	print(facto)

