#tuples
#they are ordered
#they are immutable-tuple can not change after its creation
#allow duplicate elements
#tuples used for objects that beong together
mytuple=("max",28,"fox")
print(mytuple)#('max', 28, 'fox')
tuple1="max",28,"fox"
print(tuple1)#('max', 28, 'fox')
#tuple can be written in paranthesis or without paranthesis


#in tuple if you write a single element it will recognize as string
tuple2=("max")
print(type(tuple2))#<class 'str'>

#to make it as tuple you have to keep a comma(,) after single an element
tuple3=("max",)
print(type(tuple3))#<class 'tuple'>


#tuple built in function

tuple4=tuple(["max",28,"fox"])
print(tuple4)#('max', 28, 'fox')
item=tuple4[0]
print(item)#max

item=tuple4[-1]
print(item)#fox

##tuple4[0]="more"
##print(tuple4)
#TypeError: 'tuple' object does not support item assignment
#bcz tuple is immutable
tuple5="max",87,"nore",56
for i in  tuple5:
    print(i)#max
#87
#nore
#56

#to check whether tuple inside or not
if "max" in tuple5:
    print("yes")
else:
    print("no")
    #yes


tuple6=('m','b','g','j')
print(len(tuple6))
print(tuple6.count('b'))
print(tuple6.index('m'))

#change tuple to list
list1=list(tuple6)
print(list1)#['m', 'b', 'g', 'j']
tuple7=tuple(list1)
print(tuple7)#('m', 'b', 'g', 'j')

#slicing
tuple8=(1,2,3,4,5,6,7,8,9)
b=tuple8[1:5]
print(b)#(2, 3, 4, 5)

#unpacking
tuple9="max",45,"more"
