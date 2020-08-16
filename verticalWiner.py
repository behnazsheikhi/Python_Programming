game=[[2,0,1],
      [0,0,1],
      [2,2,1],]
def winVertical(game):
    for i in range(len(game[0])):
        item = []
        for row in game:
             print(row[i])
             item.append(row[i])
        print(item)
        if item.count(item[0])==len(item) and item[0]!=0:
           print('winner','column '+str(i+1))
        else:
           print("opsssssssssss")
winVertical(game)
