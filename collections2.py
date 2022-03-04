#There are four collection data types in python which are used to store collection of data. 1.list 2.tuples 3.sets 4.dictionary


#specialized collection data types in collection module

#1 namedtuple() returns a tuple with a named value for each element in the tuple
#https://www.geeksforgeeks.org/namedtuple-in-python/
from collections import namedtuple
from collections import deque
from collections import ChainMap
from collections import Counter
from collections import OrderedDict
from collections import defaultdict


a = namedtuple('courses' ,'name,technology')
s = a('ML','python')
print(s)

s = a._make(['AI','python'])
print(s)

#2 deque 'deck' is optimised list to perform insertion and deletion easily
#https://www.geeksforgeeks.org/deque-in-python/
a = ['a','p','p','l','e']
d = deque(a)

d.append('python')
d.appendleft('AI')
print(d)
d.pop()
print(d)
d.popleft()
print(d)


#3 ChainMap() is a dictionary like class for creating a single view of multiple mapping
#https://www.geeksforgeeks.org/chainmap-in-python/

a = {1:'hi',2:'hello',3:'Namaste'}
b = {4:'ML',5:'AI'}

cp = ChainMap(a,b)

print(cp)


#Counter - to count hashable object
#https://www.geeksforgeeks.org/counters-in-python-set-1/
#https://www.geeksforgeeks.org/counters-in-python-set-2-accessing-counters/
a =[1,4,2,3,1,2,5,15,2,1,2,1,]

c = Counter(a)
print(c)


#OrderedDict - remember the order in which entries were done
#https://www.geeksforgeeks.org/ordereddict-in-python/

d = OrderedDict()
d[1] = 'a'
d[2] = 'p'
d[3] = 'p'
d[4] = 'l'
d[5] = 'e'

print(d)

#Defaultdict -Defaultdict is a sub-class of the dictionary class that returns a dictionary-like object. The functionality of both dictionaries and defaultdict are almost same except for the fact that defaultdict never raises a KeyError. It provides a default value for the key that does not exists.
#https://www.geeksforgeeks.org/defaultdict-in-python/

d =defaultdict(int)

d[1] = 'python'
d[2] = 'Ml'

print(d[3])


#UserDict,Userlist,UserString
#search on gfg








