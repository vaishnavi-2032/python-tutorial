#https://www.geeksforgeeks.org/python-arrays/

import array as arr

a = arr.array('i',[1,2,3,4,5,6])
#arr is module. raay is constructor and i indicates int data type

print(a)
print(a[2],a[-2])

print(len(a))  #length of an array

#adding elements to array
#append() -adds single element at the end of the array
#extend() - one or more element at the end
#inset() - add at specific position

a.append(100)
a.extend([1,2,3])
a.insert(2,4)

print(a)


#removing elements from array
#pop() - remove and return it. if you do not specify parameter then it will remove last index
#remove() - remove an element with specific value without returning.takes one parameter which is an element to be removed

a.pop()
print(a)
x = a.pop(2)
print(x)
a.remove(100)
print(a)



#Array concatenation

b = arr.array('i',[4,8,4,2])
c = arr.array('i')

c = b+a

print("array c is : ",c)


#slicing an array

print(a[0:3]) #value at 3 won't print
print(a[0:-2])



#looping through an array

print("values in b :")

for x in b:
	print(x)

for x in b[0:-2]:
	print(x)


x=0
while x<len(b):
	print(b[x])
	x=x+1;























