# reading file
readFile=open("sampleCSV.csv",'r')
result=readFile.read()
print(result)
# read CSV file
import csv
with open('sampleCSV.csv') as csvFile:
    readFile=csv.reader(csvFile,delimiter=',')
    dates=[]
    colors=[]
    for row in readFile:
        dates.append(row[0])
        colors.append(row[3])
print(dates)
print(colors)
try:
    selectedColor=input('which color do you prefer to know its date?')
    print(dates[colors.index(selectedColor)])
except Exception as e:
    print(e)
