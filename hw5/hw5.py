# Name: Maryam Masood

# PROBLEM A
#==========================================
# Purpose: Takes in three lists of student names and evaluates who appear in all three lists, thus being a wizard.
#
# Input Parameter(s):
# grades - a list of students who get good grades
# life - a list of students who have a social life
# sleep - a list of students who get enough sleep.
#
# Return Value(s): The final list student names who appear in all three lists (wizards).
#
#==========================================


def wizards(grades, life, sleep):

    final_list = []

    for G in range(len(grades)):
        for L in range(len(life)):
            if grades[G] == life[L]:
                for S in range(len(sleep)):
                    if grades[G] == sleep[S]:
                        final_list.append(grades[G])

    return(final_list)


# PROBLEM B

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



# tic_tac_toe()
#==========================================
# Purpose: simulates a single game of tic-tac-toe in which the computer plays randomly against itself
#
# Input Parameter(s): None
# 
# Return Value(s):
# winner(list_1) - a value ('X', 'O', or 'D' for a draw) showing who won the game
#
#==========================================


import random

def tic_tac_toe():
    
    list_1 = ['-', '-', '-', '-', '-', '-', '-', '-', '-']

    count = 0
    
    while winner(list_1) == "-":
        if (count % 2 == 0):
            w = random.randint(0,8)

            if list_1[w] == "-":
                list_1[w] = "X"
                
                if winner(list_1) != "-":
                    return(winner(list_1))
                count += 1

        else:
            w = random.randint(0,8)

            if list_1[w] == "-":
                list_1[w] = "O"
                
                if winner(list_1) != "-":
                    return(winner(list_1))
                count += 1




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
    
        





































