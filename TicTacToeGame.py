import itertools as iter


def valid_status(game):
    valid_position = False
    for row in game_map:
        for item in row:
            if item == 0:
                valid_position = True
                break
        if valid_position == True:
            break
    if valid_position == False:
        print("There is no empty space!")
        return False
    return True

# check the win status
def win(game):
    # check the same status
    def check_same(list):
        if list.count(list[0]) == len(list) and list[0] != 0:
            return True
        else:
            return False

    # horizontally
    for row in game:
        if check_same(row):
            print("winner is horizontally ")
            return True

    # vertically
    for i in range(len(game[0])):
        item = []
        for row in game:
            item.append(row[i])
        if check_same(item):
            print("winner is vertically ")
            return True

    # diagonally
    Dias = []
    cols = list(reversed(range(len(game))))
    rows = list(range(len(game)))
    for row, col in zip(rows, cols):
        Dias.append(game[row][col])
    if check_same(Dias):
        print("winner is diagonally ")
        return True

    Dias = []
    for ix in range(len(game)):
        Dias.append(game[ix][ix])
    if check_same(Dias):
        print("winner is diagonally ")
        return True

    return False


# update game board after each selection
def showGame(game_map, current_player=0,row=0, column=0, just_display=False):
    try:
        if game_map[row][column] != 0:
            print("this position is accupied! choose another one!")
            return False
        if not just_display:
            game_map[row][column] = current_player
        char = " "
        for j in range(len(game_map[0])):
            char += "  " + str(j)
        print(char)
        for i in range(len(game_map)):
            print(i, game_map[i])
        return game_map

    except IndexError as e:
        print("Error:make sure you input row/column as 0,1 and 2! ", e)
        return False
    except Exception as e:
        print("something is wrong!")
        return False


play= True
while play:
    # game_map = [[0, 0, 0],
    #             [0, 0, 0],
    #             [0, 0, 0]]
    game_size = int(input("please enter game size"))
    # create matrix
    # game_map = []
    # for i in range(game_size):
    #     row = []
    #     for j in range(game_size):
    #         row.append(0)
    #     game_map.append(row)

    # create matrix with one line for
    game_map = [[0 for i in range(game_size)] for i in range(game_size)]

    print("THis Is Game Board...\n"
          "Lets Start!!")
    showGame(game_map, just_display=True)
    game_won = False
    player = [1, 2]
    turn = iter.cycle(player)
    while not game_won:
        empty_status=valid_status(game_map)
        if empty_status==False:
           game_won = True
           answer = input("There is no empty space do you like to continue?(y/n)")
           if answer.lower() == 'y':
               print("restarting...")
           elif answer.lower() == 'n':
               print("Finish")
               play = False
           else:
               print("your answer is not valid!")
               play = False
        current_player = next(turn)
        print(f"its your turn:{current_player}")
        row_choice = int(input(f"which row do you choose?{0, 1, 2}: "))
        column_choice = int(input(f"which row do you choose?{0, 1, 2}:  "))
        result = showGame(game_map, current_player,row_choice, column_choice, False)
        while not result:
            row_choice = int(input(f"which row do you choose?{0, 1, 2}: "))
            column_choice = int(input(f"which row do you choose?{0, 1, 2}:  "))
            result = showGame(game_map, current_player,row_choice, column_choice, False)
        game_status=win(game_map)
        if game_status==True:
           game_won=True
           answer=input("Game is finished do you like to contine?(y/n)")
           if answer.lower()=='y':
              print("restarting...")
           elif answer.lower()=='n':
              print("Finish")
              play=False
           else:
               print("your answer is not valid!")
               play = False
