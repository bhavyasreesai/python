import random 
a=random.uniform(1,10)
print(a)

b =random.randint(1,10)#includes upper bound
#print(b)
c=random.normalvariate(0,1)
print(c)


mylist=list("abcdefgh")
d=random.choice(mylist)
print(d)
#d=random.choice(mylist,k=3)

random.shuffle(mylist)

random.seed(1)
print(random.random())
print(random.randint(1,10))


import secrets
#has only 3 modules
#a=secrets.ranbleow(4)
#generate random numbers range 0-15
#2^0,2^1,2^2,2^3
print(a)
mylist=list("abcdefgh")
a=secrets.choice(mylist)
print( a)


import numpy as np
a1=np.random.randint(0,10,3)
print(a1)

a2=np.random.randint(0,10,(3,4))
print(a2)

arr=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr)
np.random.shuffle(arr) #it will shuffle thr rows but not elements inside row
print(arr)

















