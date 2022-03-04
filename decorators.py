#https://www.geeksforgeeks.org/decorators-in-python/
#Decorators allow us to wrap another function in order to extend the behaviour of the wrapped function, without permanently modifying it.

#In Decorators, functions are taken as the argument into another function and then called inside the wrapper function.


def fun1(function):
	def wrapper():
		print('hello')
		function()
		print('Welcome!!')
	return wrapper

def fun2():
	print('python!!!')
	
fun2 = fun1(fun2)

#fun2()


#another approach using pysyntax

def fun1(function):
	def wrapper():
		print('hello')
		function()
		print('Welcome!!')
	return wrapper

@fun1
def fun2():
	print('python!!!')
	
#fun2()


#*args and **kwargs in Python
#https://www.geeksforgeeks.org/args-kwargs-python/


def fun1(function):
	def wrapper(*args,**kwargs):
		print('hello')
		function(*args,**kwargs)
		print('Welcome!!')
	return wrapper

@fun1
def fun2(name):
	print(f'{name}')
	
#fun2('python!!!')



#return values from decorated function

def fun1(function):
	def wrapper(*args,**kwargs):
		print('it worked')
	return wrapper

@fun1
def fun2(name):
	print(f'{name}')
	
fun2('python!!!')








