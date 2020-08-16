# import itertools as iter
# array = [1, 2]
# player=iter.cycle(array)
# for i in range(10):
#     a=next(player)
#     print(a)


# player=[1,2]
# choice=0
# for i in range(10):
#     print(player[choice])
#     print(player[choice+1])
#     # print(player[choice+1])

# game_map = [[1, 2, 3],
#             [4, 0, 6],
#             [7, 5, 9]]
# empty_position=False
# for row in game_map:
#     for item in row:
#         if item==0:
#             empty_position=True
#             break
#     if empty_position==True:
#         break
# print(empty_position)

game_size=int(input("please enter game size"))
# game=[]
# for i in range(game_size):
#     row=[]
#     for j in range(game_size):
#         row.append(0)
#     game.append(row)
# print(game)


game=[[0 for i in range(5)]for i in range(game_size)]
print(game)

# use and import library
# 1 import library and use command defined in it
import library_name
library_name.command_name()

# 2
# import command from a library and use command defined in it
from library_name import command_name
command_name()

# 2-1
# import many commands from a library and use commands defined in it
from library_name import command_name1,command_name2
command_name1()
command_name2()

# 3
# import library defined in a folder
from folder_name.library_name import command_name
command_name()
