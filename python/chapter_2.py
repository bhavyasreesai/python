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