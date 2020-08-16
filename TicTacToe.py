game_map=[[0,0,0],
            [0,0,0],
            [0,0,0],]
#  define function for showing game_map
def showGameMap():
    # first method of creating game_board by tutorial
    #             print('   a, b, c')
    #             for count,row in enumerate(game_map):
    #                 print(count, row)
    #  second method of creating game_board
    char=" "
    #  if you want character A, B, C
            # asci_code=65
            # for j in range(len(game_map[0])):
            #     char+="  "+chr(asci_code)
            #     asci_code+=1
            # print(char)
    #  if you want 0, 1, 2,... for column
    for j in range(len(game_map[0])):
        char+="  "+str(j)
    print(char)
    for i in range(len(game_map)):
        print(i, game_map[i])
print("THis Is Game Board...\n"
      "Lets Start!!")
showGameMap()
row=int(input('which row do you prefer?!'))
column=int(input('which column do you prefer?!'))
game_map[row][column]=1
showGameMap()