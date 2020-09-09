dic={'Behnaz':32,'Alireza':36,'Mahnaz':39,'Sheida':18}
print(dic)
# print value of list using index
print(dic['Mahnaz'])
# add index and value to the list
dic['Fatemeh']=58
print(dic)
dic['Ghazanfar']=120
print(dic)
# del one element from list
del(dic['Ghazanfar'])
print(dic)
# we can define every thing in value in a list for example list,function,dictionary
newDic={'Behnaz':[32,1367],'Alireza':[36,1364],'Mahnaz':[39,1360],'Sheida':[18,1381]}
print(newDic)
print(newDic['Sheida'][1])