#lists
mylist=["banana","cherry","apple"]
print(mylist)
mylist.sort()
print(mylist)

list2=[2,4,1,5,-1,8,4]
new_list=sorted(list2)
print(new_list) #[-1, 1, 2, 4, 4, 5, 8]
print(list2)#[2, 4, 1, 5, -1, 8, 4]

list3=[0]*5
print(list3)#[0, 0, 0, 0, 0]


new_list=list2+list3
print(new_list)#[2, 4, 1, 5, -1, 8, 4, 0, 0, 0, 0, 0]


#@slicing
list4=[1,2,3,4,5,6,7,8,9]
a=list4[1:5]
print(a)#[2, 3, 4, 5]


b=list4[:5]#no start , it will take default from start
print(b)#[1, 2, 3, 4, 5]

c=list4[4:]#no stop , default end
print(c)#[5, 6, 7, 8, 9]


#step index
d=list4[0:1:9]
print(d)

e=list4[::-1]
print(e)#[9, 8, 7, 6, 5, 4, 3, 2, 1]

list5=["banana","cherry","apple"]
list5_cpy=list5
print(list5_cpy)#['banana', 'cherry', 'apple']
#to add/modify
list5.append("lemon")
print(list5)#['banana', 'cherry', 'apple', 'lemon']
print(list5_cpy)#['banana', 'cherry', 'apple', 'lemon']
list5_cpy=list5.copy()
print(list5_cpy)

list6=[1,2,3,4,5]
f=[i*i for i in list6]
print(f)#[1, 4, 9, 16, 25]