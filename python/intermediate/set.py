# set
#set is a collection data type, unordered,mutable,no duplicates
myset={1,2,3}
print(myset)

set1=set("hhello")
print(set1)
#{'o', 'e', 'h', 'l'}

set2=set()#its not {}-it will recognize as dict
print(type(set2))#{'o', 'e', 'h', 'l'}
set2.add(1)
set2.add(3)
set2.add(5)
print(set2)

set2.pop()
print(set2)

odd={1,3,5,7}
even={2,4,6,8}
primes={2,3,5,7}
u=odd.union(even)
print(u)#{1, 2, 3, 4, 5, 6, 7, 8}
i=odd.intersection(even)
print(i)

























