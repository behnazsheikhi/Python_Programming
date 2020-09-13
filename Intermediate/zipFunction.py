x=[1, 8, 9, 10]
y=[15, 7, 62, 3]
z=['a', 'c', 'd', 'e']
zipObject=zip(x,y,z)
print(zipObject)    # it does not show anything because it is an iterable object and you must use for to iterate over it
# for objects in zipObject:
#     print(objects) # it creates a tuple data type of combination of
(print(x,y,z) for x,y,z in zipObject)  # it does not store any parameter after for
print(x) # we can see original value of x
for x,y,z in zipObject:   # it stores new value through each iterate
    print(x,y,z)
print(x)  # it shows last value of x 