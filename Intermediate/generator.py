currectPatern=(3,6,1)
# it generates tuple of x,y,z
# flag=False
# for x in range(10):
#     if flag==False:
#         for y in range(10):
#             if flag==False:
#                 for z in range(10):
#                     if (x,y,z)==currectPatern:
#                         print(x, y, z)
#                         print("patern finded!")
#                         flag = True
#                         break
#                     print(x,y,z)
# this function generates generator of  x,y,z and return it as yield
def findGen():
    for x in range(10):
        for y in range(10):
            for z in range(10):
                yield(x,y,z)
#  we can iterate over the generator of function and find best match!!
for x,y,z in findGen():
    if (x,y,z)==currectPatern:
        # we use .format for formating text
        print("patern finded!{}".format((x,y,z)))
        print(''.join(['patern finded!:',str((x,y,z))]))
        break