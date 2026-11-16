import multiprocessing
def task():
    print("hello from child")
if __name__=="__main__":
    p1=multiprocessing.Process(target=task)
    p1.start()

import multiprocessing
def student(name,age):
  print(name)
  print(age)
if __name__=="__main__":
  p1=multiprocessing.Process(target=student, args=("Alex",21))
  p1.start()
  p1.join()


import multiprocessing
def calculate(a,b):
  sum=a+b
  print(sum)
if __name__=="__main__":
  p1=multiprocessing.Process(target=calculate,args=(10,20))
  p1.start()
  p1.join()



import multiprocessing
def task1():
  print("hello from process 1")
def task2():
  print("hello from process 2")
if __name__=="__main__":
  p1=multiprocessing.Process(target=task1)
  p2=multiprocessing.Process(target=task2)
  p1.start()
  p2.start()
  p1.join()
  p2.join()


