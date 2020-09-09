# we must use  a in arguman number 2 for appending purpose
appendText="this line will be appended to other lines in file"
file=open('sampleFile.txt','a')
file.write('\n')
file.write(appendText)
file.close()