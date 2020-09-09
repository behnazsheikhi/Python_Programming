def compareVariables(x,y,z):
    mylist = []
    if x==0 or y==0 or z==0:
        mylist.append('c')
    if  x==1 or y==1 or z==1:
         mylist.append('d')
    if  x==2 or y==2 or z==2:
         mylist.append('e')
    if  x==3 or y==3 or z==3:
         mylist.append('f')
    else:
        print("wrong input value!")
    print('first:',mylist)
compareVariables(1, 3, 2)

def compareVariables(x,y,z):
    mylist = []
    if 0 in (x,y,z):
        mylist.append('c')
    if 1 in (x,y,z):
         mylist.append('d')
    if 2 in (x,y,z):
         mylist.append('e')
    if 3 in (x,y,z):
         mylist.append('f')
    else:
        print("wrong input value!")
    print(mylist)
compareVariables(1, 3, 2)
