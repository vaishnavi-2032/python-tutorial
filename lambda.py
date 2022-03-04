#lambda - anonynmous or nameless functions
#https://www.geeksforgeeks.org/python-lambda-anonymous-functions-filter-map-reduce/

#lambda keyword specifies that what follows is anonymous

#why used
#1 one-time use = also known as throw away functions as they are needed just once
#2 They are also passed as inputs or returned as outputs of other higher order functions
#3 Reduce code size = written in single line


#How to write anonymous functions
# can take any number of arguments from 0 to any
#lambda arguments : expression

#x=lambda a: a*a
#print(x(3))


#x=lambda a,b: a*b
#print(x(3,2))

#anonymous functions within user defined functions


def func(x):
	return(lambda y:x+y)

t = func(4)  #passing value to variable x

#print(t(8))


def func(x):
	return(lambda y:x*y)(x) #passing value to lambda

#print(func(4))


#using lambda wirhin filter()
#The filter() function in Python takes in a function and a list as arguments.his offers an elegant way to filter out all the elements of a sequence “sequence”, for which the function returns True.
#syntax = filter(function,iterables(in below case mylist))
mylist = [1,2,3,4,5,6,7,8,9,10,11,12]

filterlist = list(filter(lambda a:a%3==2,mylist))
#print(filterlist)


#Using lambda() Function with map()
#The basic function of map() is to manipulate iterables. 
#The map() function in Python takes in a function and a list as an argument. The function is called with a lambda function and a list and a new list is returned which contains all the lambda modified items returned by that function for each item.
#syntax= map(func,iterable)

mylist = [1,2,3,4,5,6,7,8,9,10,11,12]

maplist = list(map(lambda a:a%3!=2,mylist))
#print(maplist)

mylist = [1,2,3,4,5,6,7,8,9,10,11,12]

maplist2 = list(map(lambda a:a*3,mylist))
#print(maplist2)


#Using lambda() Function with reduce()
#The reduce() function in Python takes in a function and a list as an argument. The function is called with a lambda function and an iterable and a new reduced result is returned. 
# This performs a repetitive operation over the pairs of the iterable. The reduce() function belongs to the  functools module. 
#syntax = reduce(func,sequence)

from functools import reduce

ans = reduce(lambda a,b:a+b,[23,56,1,43,98,])
# 23+56=79,79+1=80 , 80+43=123 123+98=221=ans
#print(ans)


#filter within map

#mylist = [1,2,3,4,5,6,7,8,9,10,11,12]
#ourlist = list(map(lambda i:i**2,filter(lambda e:e>4 and e<9, mylist)))
#print(ourlist)


#map within filter

#mylist = [1,2,3,4,5,6,7,8,9,10,11,12]
#newlist = list(filter(lambda e:e>50,map(lambda i:i**2, mylist)))
#print(newlist)


#map,filter within reduce

mylist = [1,2,3,4,5,6,7,8,9,10,11,12]
result = reduce(lambda h,n:n/h,list(filter(lambda e:e>50,map(lambda i:i**2, mylist))))
print(int(result))




#lambda for algebra

s = (lambda a:a*a)(4)
#print(s)


#3x+3y

d = lambda x,y:3*x+3*y
#print(d(4,7))


#Quadratic eqn
#(a+b)^2

q = lambda p,b: (p+b)**2
#print(q(2,4))









