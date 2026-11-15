#generators
#grnerators -function 
 #they genarate the items one at a time , only when they are needed
def mygenerator():
  yield 1# yield gives one value at a time.
  yield 2
  yield 3
result=mygenerator()
print(next(result))
print(next(result))
print(next(result))

# the generator remembers where you stopped and continues from there when next value asked

#yeild is like return , both gives values , return stops after one return and doesnt continue. but yeild pause the function and contines from thre when it is clled next



#using for loop
def numbers():
  yield 10
  yield 20
  yield 30
  yield 40
for num in numbers():
  print(num)


def fruits():
  yield "apple"
  yield "banana"
  yield "mango"
for fruit in fruits():
  print(fruit)

  #python also allow us to create a generator in just one line . this is called ####generator expression

def numbers():
  for i in range(1,6):
    yield i
for num in numbers():
  print(num)


numbers=(x *x for x in range(1,6))#generator expression
for num in numbers:
  print(num)




#generators with conditions
def even():
  for num in range(1,6):
    if num%2==0:
      yield num
for number in even ():
  print(number)


def fibonaci(limit):
  a,b=0,1
  while a< limit:
    yield a
    a,b=b, a+b
fib = fibonaci(30)
for i in fib:
  print(i)












  
  
