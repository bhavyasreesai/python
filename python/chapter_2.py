#variables
from random import setstate

name="beau"
age=39

#expressions and statements
print(name)
#on a single line to have more than one statement by using semicolon

#*comments**
#this is a commented line,for a programmer or a reader to know the code
#evry thing intended belongs to a block

#**data types**
#anything that surround by quotes is a string, that is one type of data type
# we can check type of variable by using "type"
print (type(name))
#to check or compare , we use ==
print(type(name)==str)#true
#we can also use instance
print(isinstance(name,str))
#class - blueprint
#object/instace-a particular thing created using that blueprint

###operators
age=20
#arithmetic operations
1+1 #2
2-1 #1
2*2 #4
4/2 #2
4%3 #1
4**2 #16
4//2 #2

age=8
age+=8 #age=age+8
print(age)
print("scame"+" is a good dog")
#scame is a good dog

##comparisiton
#a==b
#a!=b
#a>=b
#a<=b


###boolean
#condi1 =True
#condi2 =False
#not condi1 = False
#condi1 and condi2 =False
#condi1 or condi2 =True


print(0 or 1)
print(False or True)
print('hi' or 'hey')

###bitwise operators
#  &=binary AND
#  |=BINARY OR
#   ~= BINARY NOT
#   ^= BINARY XOR
#   << = SHIFT LEFT
#   >> = SHIFT RIGHT


#  is and in
# is - an identity operator , returns true is both are same objects
# in - membership operator , it is used to tell if a value is contained in a list or another sequence


# ternary
def is_adult(age):
    if age>18:
        return True
    else:
        return False


# insetd of writing this we will write liike this
def is_adult2(age):
    return True if age>18 else False

###strings
#string should be in single or double qoutes
"beau"
'beau'
name='beau'
name+="is my name"
age=str(39)
print (name,age)
print("""beau is

39

years old
""")
#beau is

#39

#years old


### string methods

#string also have build in methods
print("beau".upper()) #BEAU
print("BeAu".lower()) #beau
print("beAu".title()) #Beau
print("beAu".islower()) #False


###string charrecters and slicing
#how to get a sopecific char
name = "beau"
print(name[1]) #b
print(name[-1]) #u
###slicing
print(name[1:2]) #star with index1 and end at before 2
#e
name="beau is cool"
print(name[5:7])
print(name[5:])# start eith 5 and go to end
print(name[:7])#start with 0 and end before 7



####booleans
done =True

if done:
    print("yes")
else:
    print("no")
    #yes
#if value is not in the boolean
# string are false only when empty###

done =""

if done:
    print("yes")
else:
    print("no")
    #no
done =True
print (type(done)==bool)
if done:
    print("yes")
else:
    print("no")
    #True
    #yes
done ="beau"
print (type(done)==bool)
if done:
    print("yes")
else:
    print("no")

#False
#yes
#because done is string

#####******  any   ****###
# any is a global function which is very useful in boolean
num=True
nums=False
numss=any([num,nums])
print(numss)

#True
#if one is true we will get true

###### all ####
num=True
nums=False
numss=all([num,nums])
print(numss)
#False
#if all are True only it will be true,even if oneis false over all will be false


## number data types
#complex numbers are extension of familiar real number system in which all numbers are expressed as a sum of a real part and a imagenary part
#i=-1,i^2=1
num1=2+3j
num2=complex(2,3)
print(num2.real,num2.imag)
#2.0 3.0


#####built-in functions
# abs() will return absalute value of a number
print(abs(-5))#5
print(round(5.46))#5
print(round(5.43,1))#5.4
print(round(5.46764,2))#5.47


####Enums
#enums are redable names that are bound to aconstant value
# to use emuns , we have to import from enums standard library module
from enum import Enum
class state(Enum):
    INACTIVE =0
    ACTIVE=1
print(state.ACTIVE.value)#1
print(state(1))#state.ACTIVE
#THIS IS THE ONLY WAY TO CREATE CONSTANTS IN PYTHON
#PYTHON IS no way to enforce the variable sholud be a constant
#so we use enums to create a constants, so no body  can reassign the values
#we have two ways
# 1 is bracket notation
print(state["ACTIVE"].value)#1
# and other way is
print(state.ACTIVE.value)#1

from enum import Enum
class state(Enum):
    inactive =0
    Active=1
print(state.inactive.value)#0
print(list(state)) #[<state.inactive: 0>, <state.Active: 1>]
print(len(state))#2


###user input
#we can do user input by input function
#age=input()
#print("your age is "+age)
#34-input given
#your age is 34
#print("what is your age?")
#age=input()
#print("your age is "+age)

#print(input("what is your age?"))


###control statements
condition=True
if condition==True:
    print("the condition ")
    print("was true")
#the condition
#was true

#block is part that is intendes one level,block can be formed by single line or multiple line


####Lists
#lists are the essential python data structures
dogs=["roger",1,'syd',True,7,'quincy']
print("roger"in dogs)#true
print("beau" in dogs)#false
print(dogs[0])#roger
print(dogs[2])#syd
#update
dogs[2]='beau'
print(dogs)#['roger', 1, 'beau', True]
print(dogs[-2])#beau
#slicing
print(dogs[2:5])#['beau', True, 7]
print(len(dogs))#6
dogs.append('judah')
print(dogs)#['roger', 1, 'beau', True, 7, 'quincy', 'judah']
dogs.extend('chup')
print(dogs)#['roger', 1, 'beau', True, 7, 'quincy', 'judah', 'c', 'h', 'u', 'p']
dogs+='moy'
print(dogs)#['roger', 1, 'beau', True, 7, 'quincy', 'judah', 'c', 'h', 'u', 'p', 'm', 'o', 'y']
dogs+=['moy']
print(dogs)#['roger', 1, 'beau', True, 7, 'quincy', 'judah', 'c', 'h', 'u', 'p', 'm', 'o', 'y', 'moy']
#look at the output in line 274 and 276 , when you write in square bracket you will get like name
#when you don't write in square bracket you will get letters separated
dogs.remove('quincy')
print(dogs)#['roger', 1, 'beau', True, 7, 'judah', 'c', 'h', 'u', 'p', 'm', 'o', 'y', 'moy']

dogs.insert(2,'hay')#index, value
print(dogs)#['roger', 1, 'hay', 'beau', True, 7, 'judah', 'c', 'h', 'u', 'p', 'm', 'o', 'y', 'moy']

####sorting lists
items=['phone','laptop','box','chair']
items.sort()
print(items)#['box', 'chair', 'laptop', 'phone']

items=['Phone','laptop','box','chair']
items.sort()
print(items)#['Phone', 'box', 'chair', 'laptop']
#firat it will sort the letters with upper case
#then it will sort lower case letters

print(sorted(items,key=str.lower))#this crates the new list without modifying the list
print(items)



####tuples
#tuples is also another data structers in python
#they allow you to create immutable groups of objects
# which means once tuples are created can not be modified
#they use parantheses insted of brackets
names=('roger','syd','beau')
names[0]
names.index('roger')
len(names)
print('roger' in names)#true
print(sorted(names))#['beau', 'roger', 'syd']

###dictionaries
# dict uses curly braces
dog={'name':'roger','age':14}
print(dog)#{'name': 'roger', 'age': 14}
print(dog.pop('name'))#roger
print(dog)#{'age': 14}
print('colour' in dog)#False


#sets

#python data structures
#sets are not ordered
set1={'roger','syd'}
set2={'roger'}
intersect=set1&set2
print(intersect)#{'roger'}

mod=set1|set2
print(mod)#{'syd', 'roger'}
mod=set1-set2
print(mod)#{'syd'}
mod=set1>set2
print(mod)#True
#sets does not give duplicates
set={'roger','syd','roger'}
print(set)#{'syd', 'roger'}


###functions
def hello():
    print('hello!')
hello()
#hello!

def hello (name=' my friend'):
    print('hello'+name)
hello()
#hello my friend
def hello (name,age):
    return 'hello '+ name + ', you are '+str(age)+ ' years old'
print( hello (name,age))
print('hello '+ name + ', you are '+str(age)+ ' years old')
hello('beau',39)
#hello beau, you are 39 years old


def change(value):
    value=2
val=1
change(val)
print(val)#1


###variable scope
age=8



###nested functions
#functions inpython can nested inside other functions

#def talk(phrase):
 #   def say(word):
  #      print(word)
   # words=phrase.split('')
    #for word in words:
     #   say(word)
#talk('I am going to buy milk'

def count():
    count=0
    def increment():
        nonlocal count
        count=count+1
        print(count)
    increment()
count()

###objects
age=8
print(age.real)#8
print(age.imag)#0
print (age.bit_length())#4

#items=[1,2]
#items.append(3)
#items.pop()
#print(id(items))#2682165967616

age=8
age=age+1

##loops
#in python we have two kind of loops
#for and while
condition=True
while condition==True:
    print("condi id true")
    condition=False

count=0
while count<10:
    print("condi is True")
    count = count+1
print("after the loop")

#for
#to execute predetermined amount of time
#item=[1,2,3,4]
#for item in items:
 #   print(item)
#for item in range(15):
 #   print(item)
#item=[1,2,3,4]
#for index,item in enumerate(items):
 #   print(index,item)

#break and continue
#continue stops the current iteration and tells python to execute the next one
#breaks stops all the loops together and goes on whith the next intruction after the loop ends

item=[1,2,3,4]
for item in items:
    if item==2:
        continue
    print(item)