#decorators
#they are very powerfull tools in python

# 2 diff decoratoe . 1 - function decorator  , 2. class decorator
#@mydecorator
def dosomething():
  pass
  #it is a function that takes another function argment and extends the behavious of this function of our  explicitly modifing it
  #it allows yo to add new function to exsting function
  #fnction in pythons are first class objects


def start_end_decorator(func):
    def wrapper():
        print('start')
        func()
        print('end')
    return wrapper
def print_name():
    print("alex")
print_name=start_end_decorator(print_name)
print_name()


#*args-arguments
#**kwargs=kew word argumentsm






def start_end_decorator():
  print("hello")
def decorator(func):
  def wrapper():
    print('start')
    func()
    print('stop')
  return wrapper
output=decorator(start_end_decorator)
output()#this contains wrapper func , so we call it in ()
