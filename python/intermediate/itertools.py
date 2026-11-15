#itertools
#product,permutations,combinations,accumulate,groupby,infinite iterals
#an iterale is anything that you can loop through using a for loop
numbers=[10,20,30]
for i in numbers:
  print(i)
#lists,tuples,string,sets,dict are the examples of iterable

#iterator
#an iterator gives you elments one at a time
numbers=[10,20,30]
x=iter(numbers)
print(next(x))
print(next(x))
print(next(x))


#itertolls is a built-in python module that provided special tools to work with iterators and loops
import itertools
for i in itertools.count(1,2):
  #itertools.count(start, step)
  print(i)
  if i>=9:
    break
  #count() is an infinite iterator. It will keep generating numbers unless you stop it.


#cycle()-it is the repeatedly repeats the elements of an iterable forever

#subjects=['python','c','java']
#for subject in itertools.cycle(subjects):
 # print(subject)

colours=['red','green','blue']
count=0
for colour in itertools.cycle(colours):
  print(colour)
  count+=1
  if count==7:
    break


from itertools import permutations
#a=[1,2]
#b=[3]
#prod=product(a,b,repeat=2)
#print(list(prod))

a=[1,2,3]
prem=permutations(a,2)
print(list(prem))

#combinations
from itertools import combinations
a=[1,2,3,4]
comb=combinations(a,2)
print(list(comb))

from itertools import combinations
a=[1,2,3,4]
comb=combinations(a,3)
print(list(comb))

from itertools import accumulate
import operator
a=[1,2,5,4,3]
acc=accumulate(a,func=max)
print(a)
print(list(acc))

from itertools import groupby
def smaller_than_3(x):
  return x<3
a=[1,2,3,4]
group_obj=groupby(a,key=smaller_than_3)
for key,value in group_obj:
  print(key,list(value))




    
