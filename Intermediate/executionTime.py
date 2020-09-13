import timeit
print(timeit.timeit('''myinput=range(100)
def divisionByFive(x):
    if x%5==0:
        return True
    else:
        return False
numbers=(i for i in myinput if divisionByFive(i)) #create a generators then iterate over it
for i in numbers:
    print(i)''',number=5000)) # earn execution time of creating generators and iterate through it

print(timeit.timeit('''myinput=range(100)
def divisionByFive(x):
    if x%5==0:
        return True
    else:
        return False
numbers=[i for i in myinput if divisionByFive(i)] #create a generators then iterate over it
for i in numbers:
    print(i)''',number=5000)) # earn execution time of creating list and iterate through it
# myinput=range(100)
# def divisionByFive(x):
#     if x%5==0:
#         return True
#     else:
#         return False
# numbers=(i for i in myinput if divisionByFive(i)) #create a generators then iterate over it
# for i in numbers:
#     print(i)
print(timeit.timeit('1+3',number=5000)) # help to know execution time of 1+3 you can put every script instead of it
import  time   # use time module to earn original and execution time
originalTime=time.time()
myinput=range(100)
def divisionByFive(x):
    if x%5==0:
        return True
    else:
        return False
numbers=(i for i in myinput if divisionByFive(i)) #create a generators then iterate over it
for i in numbers:
    print(i)
executionTime=time.time()-originalTime
print(executionTime)