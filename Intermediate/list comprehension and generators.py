# create list
myList=[]
for i in range(5):
    myList.append(i)
print(myList)

# create list --> myList is a list which is more quick than generator but it uses memory to store item
myList=[i for i in range(5)]
print(myList)

# generatoe is slower but it doesnot use memory
xyz=(i for i in range(5))
print(xyz)