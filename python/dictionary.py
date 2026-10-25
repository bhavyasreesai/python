#key:value
data = {1:'ram',2:'ramu',3:'sita',5:'gita'}
print(data)
#output-{1: 'ram', 2: 'ramu', 3: 'sita', 5: 'gita'}

#fetching the particular value
print(data[3])
#output-sita

#print(data[4])
#output-error

## method-2
#we can use function
print(data.get(1))
#output-ram

print(data.get(4))
#output-None

print(data.get(1,'not found'))
#output-ram

print(data.get(4,'not found'))
#output-not found

#########
#dictionaries with help of lists

keys=['ram','ramu','sita','gita']
values=['python','java','js','cs']
data=dict(zip(keys,values))
print(data)
#output-{'ram': 'python', 'ramu': 'java', 'sita': 'js', 'gita': 'cs'}

keys=['ram','ramu','sita','gita']
values=['python','js','cs']
data=dict(zip(keys,values))
print(data)
#output-{'ram': 'python', 'ramu': 'js', 'sita': 'cs'}

keys=['ram','ramu','sita','gita']
values=['python','java','js','cs']
data=dict(zip(keys,values))
print(data)

#######
#to add new value

data['vani']='c++'
print(data)
#output- {'ram': 'python', 'ramu': 'java', 'sita': 'js', 'gita': 'cs', 'vani': 'c++'}

######
#to delete

del data['ram']
print(data)
#output-{'ramu': 'java', 'sita': 'js', 'gita': 'cs', 'vani': 'c++'}

##############
#list inside dict and dict inside dict

prog={'js':'atom','cs':'vs','python':['pycharm',"sublime"],'java':{'jse':'netbeans','jee':'eclipse'}}
print(prog)
#output-{'js': 'atom', 'cs': 'vs', 'python': ['pycharm', 'sublime'], 'java': {'jse': 'netbeans', 'jee': 'eclipse'}}

print(prog["js"])
#output-atom

print(prog['python'])
#output-['pycharm', 'sublime']

print(prog['java'])
#output-{'jse': 'netbeans', 'jee': 'eclipse'}

print(prog['java']['jee'])
#output-eclipse

for name in data.keys():
    print(name)

for name in data:
    print(name)
for language,value in prog.items():
    print(language,value)