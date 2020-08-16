game=[[0,0,0],
      [0,2,0],
      [2,2,0],]
def winHorizontal(game_board):
    # one way to find the winner
        # for row in game:
        #     all_match=True
        #     for item in row:
        #         if item !=row[0]:
        #             all_match = False
        #     if  all_match== True:
        #         print('winner!')
    # another way
    for row in game:
       # print(row)
       # print(len(row))
       # print(row.count(row[0]))
       if row.count(row[0])==len(row) and row[0] !=0:
           print("winner")
winHorizontal(game)