#First-class object = in python everything is treated as an object including all the data types and functions too ,so it is called as first-class object
#https://www.geeksforgeeks.org/first-class-functions-python/

#inner-function = function inside function


#string interpolation
#https://www.geeksforgeeks.org/formatted-string-literals-f-strings-python/


def fun1(name):
	return f"Hello {name}"

	
def fun2(name):
	return f"{name} , how are you?"
	

def fun3(fun4):
	return fun4('dear learner')
	

print(fun3(fun1))
print(fun3(fun2))



def fun():
	print('parent')
	def childfun():
		print('1st child')
	def childfun2():
		print('2nd child')
		
	childfun()
	childfun2()

fun()
