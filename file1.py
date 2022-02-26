#print('hello world');

#Numerical data types
x=10  #int
print(type(x))

x=10.35  #float
print(type(x))

x=10j #complex number
print(type(x))

x=10>9  #boolean
print(type(x))




#string
#note : strings are immutable you can't cnange them

x="hi"  #string
print(type(x))

x='hi'  #this is also string
print(type(x))

x=input();  #input from user
print(type(x))

print(x.upper()) #change to uppercase

print(len(x)) #length of string

print(x[0]) #first index of string
print(x[0:1]) #from range 0 to 4
print(x[-2]) #second last index of string




#list
#https://www.geeksforgeeks.org/difference-between-list-and-array-in-python/

mylist = [1,'absdj',40,28.4,'a']  #can contain multiple data types
print(type(mylist))  
print(mylist) #no need of loop to print list
print(mylist[3])
print(mylist[1:4])












