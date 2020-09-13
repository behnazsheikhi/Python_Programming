myList=['Behnaz','Mahnaz','Sahar','Alireza']
for i in range(len(myList)):
    print(i,myList[i])

for i in enumerate(myList) : # use enumerate(myList) instead of range(len(muList)) --> it creates an iterable object
   print(i)
[print(i,j)for i,j in enumerate(myList)]


newDic=dict(enumerate(myList))
print(newDic)
[print(i,newDic[i])for i,j in enumerate(newDic)]
for i,j in enumerate(newDic):
    print(i,newDic[i])
newTuple=tuple(enumerate(myList))
print(newTuple)
newList=list(enumerate(myList))
print(newList)

for i in enumerate(myList): # it makes an object of a tuple of key and value
    print(i)
