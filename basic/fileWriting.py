# open will create a file if there is not file and you can give the whole directory to open command
# we must use w in arguman number 2 for writing purpose
text='This is first line of file\nthis is second line of file'
file=open("sampleFile.txt",'w')
file.write(text)
file.close()