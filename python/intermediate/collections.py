#collections
#counter,namedtuple,orderedDict,defaultdict,deque
from collections import Counter#c is uppercase
a="aaaaabbbcccc"
mycounter=Counter(a)
print(mycounter)
#Counter({'a': 5, 'c': 4, 'b': 3})
print(mycounter.keys())
print(mycounter.values())
print(mycounter.most_common(1))


from collections import namedtuple
#easy to create , light weight object type
point=namedtuple('point','x,y' )
pt=point(1,-4)
print(pt.x,pt.y)

from collections import OrderedDict
#like regular dict, they rember the order of insertion

order_dict=OrderedDict()
order_dict['a']=1
order_dict['b']=2
order_dict['c']=3
order_dict['d']=5
print(order_dict)
#OrderedDict({'a': 1, 'b': 2, 'c': 3, 'd': 5})


from collections import defaultdict
#if not set it will use default
d=defaultdict(int)#float,string..
d['a']=1
d['b']=2
print(d)
print(d[a])
#print(d[c])#since c is not there it will give default 0


from collections import deque
#doble ened queue, we can add or remove
d=deque()
d.append(1)
d.append(2)
d.append(3)
print(d)


d.pop()
print(d)

d.popleft()
print(d)
d.extendleft([4,5,6])
print(d)









