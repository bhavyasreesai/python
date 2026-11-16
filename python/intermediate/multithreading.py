#normal code
import time
def task1():
  print("task1 started")
  time.sleep(2)
  print('task1 finished')
def task2():
  print('task2 started')
  time.sleep(2)
  print('task2 finished')
task1()
task2()

#Task 1 started
#Task 1 completed
#Task 2 started
#Task 2 completed



#multithreading code
import threading
import time
def task1():
  print("task1 started")
  time.sleep(2)
  print('task1 finished')
def task2():
  print('task2 started')
  time.sleep(2)
  print('task2 finished')
t1=threading.Thread(target=task1)
t2=threading.Thread(target=task2)
t1.start()
t2.start()


#task1 started
#task2 started
#task1 finished
#task2 finished


#start() vs run()
#run()
import threading
import time
def task():
  print("task started")
  time.sleep(2)
  print('task completed')
t1=threading.Thread(target=task)
t1.run()
print('main completed')

#task started
#task completed
#main completed


#start() vs run()
#start()
import threading
import time
def task():
  print("task started")
  time.sleep(2)
  print('task completed')
t1=threading.Thread(target=task)
t1.start()
print('main completed')

#task started
#main completed
#task completed

#start() → Starts a new thread and allows concurrent execution with the main thread
#run() → Executes the function directly in the calling thread, without creating a new thread

