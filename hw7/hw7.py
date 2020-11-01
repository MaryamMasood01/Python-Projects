# Name: Maryam Masood
# x500: masoo013

# PROBLEM A
#==========================================
# Purpose: t takes in a single positive integer argument n and returns a list of numbers in the collatz sequence from n to 1, inclusive.
#
# Input Parameter(s):
# n - a single positive integer
#
# Return Value(s): a list of numbers in the collatz sequence from n to 1, inclusive
#
#==========================================

def collatz(n):
    if n == 1:
        return [1]
    elif (n % 2) == 0:
        return [n] + collatz(n // 2)
    else:
        return [n] + collatz((n * 3) + 1)
        
# PROBLEM B
#==========================================
# Purpose: takes in one argument, a list of integers num_list, and returns the minimum value in that list.
#
# Input Parameter(s):
# num_list - list of integers
#
# Return Value(s): the minimum value in num_list
#
#==========================================

def find_min(num_list):
    if len(num_list) == 1:
        return num_list[0]
    else:
        if num_list[0] > find_min(num_list[1:]):
           return find_min(num_list[1:])
        else:
            return num_list[0]


# PROBLEM C

import random

# open_slots(board)
#==========================================
# Purpose: Takes in a list "board" and returns a list of the indexes which still contain open spaces ('-')
#
# Input Parameter(s):
# board -  a list of values ("X", "O", "-") correlating with a tic-tac-toe array
#
# Return Value(s): a list of the indexes which still contain open spaces ('-')
#
#==========================================


def open_slots(board):

    final_list = []

    for B in range(len(board)):
        if board[B] == "-":
            final_list.append(B)

    return(final_list)



# winner(board)
#==========================================
# Purpose: Evaluates wheather the game is won by an x, an o, or was a draw
#
# Input Parameter(s):
# board -  a list of values ("X", "O", "-") correlating with a tic-tac-toe array
#
# Return Value(s):
# board[0] when (board[0] = board[1] = board[2]), (board[0] = board[3] = board[6]), or (board[0] = board[4] = board[8]), which equals "X" or "O" depending on which won the game.
# board[1] when (board[1] = board[4] = board[7]), which equals "X" or "O" depending on which won the game.
# board[2] when (board[2] = board[5] = board[8]) or (board[2] = board[4] = board[6]), which equals "X" or "O" depending on which won the game.
# board[3] when (board[3] = board[4] = board[5]), which equals "X" or "O" depending on which won the game.
# board[6] when (board[6] = board[7] = board[8]), which equals "X" or "O" depending on which won the game.
# "-" if there is at least one empty spot and neither player won
# 'D' if the game ended in a draw
#
#==========================================


def winner(board):
    if (board[0] == "X") or (board[0] == "O"):
        if (board[0] == board[1]) and (board[0] == board[2]):
            return(board[0])
        
    if (board[3] == "X") or (board[3] == "O"):
        if (board[3] == board[4]) and (board[3] == board[5]):
            return(board[3])
        
    if (board[6] == "X") or (board[6] == "O"):
        if (board[6] == board[7]) and (board[6] == board[8]):
            return(board[6])

    if (board[0] == "X") or (board[0] == "O"):
        if (board[0] == board[3]) and (board[0] == board[6]):
            return(board[0])
        
    if (board[1] == "X") or (board[1] == "O"):
        if (board[1] == board[4]) and (board[1] == board[7]):
            return(board[1])
        
    if (board[2] == "X") or (board[2] == "O"):
        if (board[2] == board[5]) and (board[2] == board[8]):
            return(board[2])

    if (board[0] == "X") or (board[0] == "O"):
        if (board[0] == board[4]) and (board[0] == board[8]):
            return(board[0])
        
    if (board[2] == "X") or (board[2] == "O"):
        if (board[2] == board[4]) and (board[2] == board[6]):
            return(board[2])

    if (open_slots(board) != []):
       return("-")
    
    return("D")




# play_games(n)
#==========================================
# Purpose: makes the computer play the game an "n" number of times and documents the number of times "X" wins, "O" wins, and how many times the result is a draw
#
# Input Parameter(s):
# n - the number of games to play
#
# Return Value(s): None
#
#==========================================

def play_games(n):

    x_wins = 0
    o_wins = 0
    draws = 0

    for i in range(n):
        game = tic_tac_toe()

        if game == "X":
            x_wins += 1
        elif game == "O":
            o_wins += 1
        elif game == "D":
            draws += 1

    print("X wins: ", x_wins)
    print("O wins: ", o_wins)
    print("Draws: ", draws)



# force_win(board)
#==========================================
# Purpose: 
#
# Input Parameter(s):
# board - 
#
# Return Value(s): 
#
#==========================================

def force_win(board):
    val = winner(board)
    if val != "-":
        if val == 'X':
            return 1
        elif val == 'O':
            return -1
        else:
            return 0
    else:
        list_index = open_slots(board)
        val_list = []
        val2_list = []
        if len(list_index) % 2 == 0:
            for i in list_index:
                board_copy = board[:]
                board_copy[i] = 'O'
                x = force_win(board_copy)
                if x != None:
                    val_list.append(x)
            return min(val_list)
        else:
            for i in list_index:
                board_copy = board[:]
                board_copy[i] = 'X'
                x = force_win(board_copy)
                if x != None:
                    val2_list.append(x)
            return max(val2_list)

    
            
                
# [REVISED] tic_tac_toe()
#==========================================
# Purpose: simulates a single game of tic-tac-toe in which the computer plays randomly X randomly and O placing itself where it will result in the best possible outcome
#
# Input Parameter(s): None
# 
# Return Value(s):
# winner(list_1) - a value ('X', 'O', or 'D' for a draw) showing who won the game
#
#==========================================


def tic_tac_toe():
    
    list_1 = ['-', '-', '-', '-', '-', '-', '-', '-', '-']
 
    while winner(list_1) == "-":
        x = open_slots(list_1)
        
        if (len(x) % 2 != 0):
            w = random.randint(0,8)

            if list_1[w] == "-":
                list_1[w] = "X"
                
                if winner(list_1) != "-":
                    return(winner(list_1))

        else:
            list_index = open_slots(list_1)
            val_list = []
            for i in list_index:
                board_copy = list_1[:]
                board_copy[i] = 'O'
                x = force_win(board_copy)
                if x != None:
                    val_list.append(x)
            y = min(val_list)
            cat = val_list.index(y)
            if y != 1:
                list_1[list_index[cat]] = 'O'
                
            if winner(list_1) != "-":
                return(winner(list_1))    
                


























        
