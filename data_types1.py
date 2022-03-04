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
#ordered
#https://www.geeksforgeeks.org/difference-between-list-and-array-in-python/

mylist = [1,'absdj',40,28.4,'a']  #can contain multiple data types
print(type(mylist))  
print(mylist) #no need of loop to print list
print(mylist[3])
print(mylist[1:4])

mylist[4]=5  #lists are mutable
mylist.append('hi') #append at the end
print(mylist)

mylist.insert(2,100) #at index 2 insert 100
mylist.reverse()
print(mylist)




#Dictionary
#unordered,key-value pair
#keys act as indexes
#values can be duplicate but keys can't
#dictionary is mutable
courses = {1:'ML',2:'ANN','third':'sp',4:'ES',5:'ES'}
print(courses['third'],courses.get(2))
print(courses)
courses[4]='Algo'
courses['six']='ADBMS'
print(courses)


#Tuple
#ordered,immutable,duplicate entries allowed,various data types allowed

animals = (10,'tiger',20,30,'lion',30,'tiger')

print(animals)
print(animals[1])
print(animals.count(30)) #count number of times it apeeared in tuple



#set
#unordered(does not support indexing),no duplicate entries

myset = {10,20,30,40,20} #20 will be print only 1 time

print(myset)


#misc
a=[1,2,34,46]  #list
b={66,'fhsf',52.25} #tuple

c= [a,b] #list with other data types
print(c)



#type conversion
#int() - canges any data type to int data type
#float()-    to float
#str()- to str
#tuple() - to tuple
#list() - to list
#dict() - to dictionary
#set() - to set

x=10
name = 'name'
print(list(range(11)))  #range function 0 to 11 
print(str(x)+name)
print(range(11))
print(list(b))





