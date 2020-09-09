game=[[1,0,0],
      [0,1,0],
      [2,2,1],]
def winDiagonal(game):
      # item=[]
      # i = 0
      # for row in game:
      #       k = 0
      #       for j in row:
      #            if i==k:
      #               item.append(j)
      #            k += 1
      #       i+=1
      # if item.count(item[0]) == len(item) and item[0] != 0:
      #       print('winner', 'column ' + str(item))
      # else:
      #       print("opsssssssssss")
      Dias=[]
      flag=False
      cols=list(reversed(range(len(game))))
      rows=list(range(len(game)))
      for row,col in zip(rows,cols):
            Dias.append(game[row][col])
      if Dias.count(Dias[0]) == len(Dias) and Dias[0] != 0:
            print('winner', 'column ' + str(Dias))
      # else:
      #       print("opssssssssssss")
      Dias = []
      for ix in range(len(game)):
            Dias.append(game[ix][ix])
      print(Dias)
      if Dias.count(Dias[0]) == len(Dias) and Dias[0] != 0:
            print('winner', 'column ' + str(Dias))
      else:
            print("opssssssssssss")

winDiagonal(game)
