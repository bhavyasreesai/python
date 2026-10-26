#variables
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
