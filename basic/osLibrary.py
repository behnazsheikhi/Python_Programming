import os
import time
# get current directory path
currentDir=os.getcwd()
print(currentDir)
# make a directory in current directory
os.mkdir('test')
# rename a directory
os.rename('test','test2')
time.sleep(1)
# remove a directory from current directory
os.rmdir('test')