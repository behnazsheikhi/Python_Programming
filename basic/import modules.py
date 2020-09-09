# 1.
import statistics as s
# import library_name as alias_name
list_number=[2,9,11,12,15,20,28,70,10,13,60]
x=s.variance(list_number)
print(x)
# library_name.command
# 2.
from  statistics import variance
# from library_name import command_name
list_number=[2,9,11,12,15,20,28,70,10,13,60]
y=variance(list_number)
# just write command_name
print(y)
# 3.
from  statistics import variance as v
list_number=[2,9,11,12,15,20,28,70,10,13,60]
y=v(list_number)
print(y)
# 4.
from  statistics import variance as v,mean as m
list_number=[2,9,11,12,15,20,28,70,10,13,60]
y=v(list_number)
z=m(list_number)
# 5.
# 4.
from  statistics import *
# all command in library will be imported
list_number=[2,9,11,12,15,20,28,70,10,13,60]
y=v(list_number)
z=m(list_number)