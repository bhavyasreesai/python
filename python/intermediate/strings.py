#strings
#ordered,immutable,text representation
mystring="hello world"
print(mystring)
string1="""hello \
world"""
print(string1)

string2="hello world"
#char =string[3]
#string2[1]='u'#error - can not change,immutable

string3=string2[:4]
print(string3)


greet="hello"
name="tom"
print(greet + name)


#to remove white space-strip()
string="             hello"
print(string.strip())

print(string2.upper())
print(string2.title())

print(string2.find('l'))

print(string2.replace('hello', 'universe'))
print(string2.split())
print(list(string2))
print(" | ".join(string2))


#%,format(),f-string
print("the greet is %s" %string2)
#the greet is 'hello world'
# for sting -%s
#for numbers - %d
#floting-%f


#format
print("the greet is {}".format(string2))

#f-sting
print(f"the greet is { string2 * 2 } ")






















