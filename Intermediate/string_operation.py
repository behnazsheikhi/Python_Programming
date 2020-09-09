# string Concatenation
names=["behnaz","asghar","alireza","mohammad"]
# print(names)
for name in names:
    # print(name)
    # use + to concat string
    # print("hello there, "+name)
    # join() use to concat string and it gives exactly one parameter
    print(' '.join(["hello there, ",name]))
# to show all items in one line
print(' , '.join(names))
# use os.path.join() to open and read file
import os
location_of_files='D:\\python_programming'
file_name='test.txt'
print(location_of_files+'\\'+file_name)
with open(os.path.join(location_of_files,file_name)) as file:
    print(file.read())

# string Formating
who='behnaz'
how_many=12
print(who , 'bought', how_many , 'apples today!')
print('{} bought {} apples today!'.format(who,how_many))
print('{0} bought {1} apples today!'.format(who,how_many))
