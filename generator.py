#https://www.geeksforgeeks.org/generators-in-python/


#iterator
#behind the scene for for loop iterator works
#So, For loop in nothing but an implementation of Iterator in an infinite while loop.
#Iterator in python is an object that is used to iterate over iterable objects like lists, tuples, dicts, and sets. 
#iterator object is initialized using the iter() method. It uses the next() method for iteration.
#iter function converts list into iterator
#syntax iter(iterable)

#nums = [1,3,5,7]

#it = iter(nums)

#print(it.__next__())   #or print(next(it))
#print(it.__next__()) 
#when we call next again it will preserve old value and give us next

#internal implementation of for loop
itvalue = 'apple'
it = iter(itvalue)

while True:
	try:
		print(next(it))
	except:
 		break




# If the body of a def contains yield, the function automatically becomes a generator function.
#The yield statement suspends function’s execution and sends a value back to the caller, but retains enough state to enable function to resume where it is left off. When resumed, the function continues execution immediately after the last yield run. 
#https://www.geeksforgeeks.org/use-yield-keyword-instead-return-keyword-python/

def new(dict):
	for x,y in dict.items():
		yield x,y

a = {1:"hi",2:"welcome"}
b = new(a)	
print(b)
print(next(b))
print(next(b))
#print(next(b))  #stopiteration is called


def myfun(i):
	while i<=3:
		yield i
		i+=1
j = myfun(2)
print(next(j))
print(next(j))


def ex():
	n=6
	yield n
	n *=n
	yield n

d = ex()
print(next(d))
print(next(d))
#print(next(d))  #print(next(d))



#to execute the generator function at once we can use for loop.this loop iterates over all the objects and after all implementations ,it executes Stopiteration

def ex():
	n=6
	yield n
	n *=n
	yield n

d = ex()
for x in d:
	print(x)
	


#GENERATOR EXPRESSIONS

#Resemble list comprehensions and like lambda functions generator expressions create anonymous generator functions


f = range(6)
#https://www.geeksforgeeks.org/gfact-50-python-end-parameter-in-print/
print("list comp",end=":")

q =[x+2 for x in f]  #all values generated at once

print(q)
print("gen exp",end=":")

r = (x+2 for x in f)
print(r)
for x in r:
	print(x) #generated values one after other



print("gen exp",end=":")
r = (x+2 for x in f)
print(max(r))






#use cases

#fibonacci series

def fib():
	f,s=0,1
	while True:
		yield f
		f,s = s,f+s

for x in fib():
	if x>50:
		break
	print(x,end=' ')


#number stream
#even
a = range(2,15,2)

b = (x for x in a)
print(b)
for y in b:
	print(y)
	





