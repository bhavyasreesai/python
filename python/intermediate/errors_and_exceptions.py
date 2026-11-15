#errors and exceptions
#a=[1,2,3]
#a.remove(4)
#print(a)


#my_dict={'name':'max'}
#my_dict['age']

#x=-5
#if x<0:
 # raise Exception ('x should be positive')
#assert(x>=0)


#try:
 # a=5/0
#except:
 # print('an error happend')


try :
  a=5/1
  b=a+4
except Exception as e:
  print(e)
except TypeError as e:
  print(e)
else:
  print('every thing is fine')
finally:
  print('cleaning up...')
















  
