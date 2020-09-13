# string concatenating

myList=['behnaz', 'alireza', 'sheida', 'shamim']
print(myList)
print(','.join(myList))
for name in myList:
    # print('Hello, ',name)
    print(' '.join(['hello,',name]))
import os
currentDirectory='/home/behnaz/Documents/python_programming/basic'
fileName='sampleFile.txt'
print(currentDirectory,'/',fileName)
print('/'.join([currentDirectory,fileName]))
with open(os.path.join(currentDirectory,fileName)) as file:
    print(file.read())

# string Formating
name='alireza'
howMany=15
# alireza bought 15 golden coins
print(name, 'bought', howMany , 'golden coins')
print('{} bought {} golden coins'.format(name,howMany))