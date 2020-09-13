def startGame():
    gameBoardSiza=int(input("Please Enter Your Preferred Game Siza?"))
    print("This Is Game Board!Lets start...")
    text=' '
    for n in range(gameBoardSiza):
        text+='  '+str(n)
    print(text)
    gameBoard=[[0 for i in range(gameBoardSiza)] for i in range(gameBoardSiza)]
    print(gameBoard)

startGame()
# import random
# player=random.randint(1,2)
# print('Player',player,"It Is Your Turn")
# row=int(input("which row do you choose?"))
# column=int(input('which column do you choose?'))
