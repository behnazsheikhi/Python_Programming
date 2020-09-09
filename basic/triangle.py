totalNumber=int(input("how many stars do you want in last line?"))
for i in range(1,totalNumber+1):
    print(i*'*')
for j in range(totalNumber-1,0,-1):
    print(j*'*')