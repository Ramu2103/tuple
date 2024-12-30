tuple=(11,22,33,44,1,2,3,4,5,5,10,15,20,25,30)
x=slice(5)
print(tuple[x])
print(tuple)

#Tuple Concatenation
a=(10,20,30,40)
b=(1,2,3)
result=a+b
print(result)

#Repetititon of tuple
b=(1,2,3,)
result=b*3
print(result)

#Nested tuple
tuple=((1,2,3),(4,5,6),(7,8,9))
print(tuple)
print(type(tuple))
print(tuple[0])
print(tuple[1])
print(tuple[2])

#Add tuple
set={'black','red','yellow','green','orange'}
print(set)
print(type(set))
set.add('puple')
print(set)
set.add('pink')
set.add('blue')
set.add('violet')
print(set)

#Adding Multiple Elements
set1={'Lavendra','Indigo','Rosegold','Peach'}
set.update(set1)
print("----------------------------------------")
print(set)