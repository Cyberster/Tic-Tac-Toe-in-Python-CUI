##  Game name:  Tic-Tac-Toe
##  File name:  tictactoe.py
##  Author:     Arpan Das
##  Date:       24-Oct-2018
Version =       'v1.0.0'

import os

# clear screen and print the formatted game board, returns void
def print_board(board):
    # clear screen and print board
    os.system('cls')  # For Windows
    os.system('clear')  # For Linux/OS X
    
    # print initial messages
    print('=' * 80)
    print('\tWelcome to Tic-Tac-Toe ' + Version)
    print('=' * 80)
    
    print()
    print('\t' + board[0][0], end = ' | ')
    print(board[0][1], end = ' | ')
    print(board[0][2], end = '\n\t---------\n')
    print('\t' + board[1][0], end = ' | ')
    print(board[1][1], end = ' | ')
    print(board[1][2], end = '\n\t---------\n')
    print('\t' + board[2][0], end = ' | ')
    print(board[2][1], end = ' | ')
    print(board[2][2], end = '\n')
    print()
    return

# check if a player has won the game or not, returns boolean
def win_check(board, player):
    if board[0][0] == player and board[0][1] == player and board[0][2] == player \
       or board[1][0] == player and board[1][1] == player and board[1][2] == player \
       or board[2][0] == player and board[2][1] == player and board[2][2] == player \
       or board[0][0] == player and board[1][0] == player and board[2][0] == player \
       or board[0][1] == player and board[1][1] == player and board[2][1] == player \
       or board[0][2] == player and board[1][2] == player and board[2][2] == player \
       or board[0][0] == player and board[1][1] == player and board[2][2] == player \
       or board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    else:
        return False

# this loop continues until user enter 'q' as input to quit
while True:

    
    #board = [['X', 'O', 'X'], [0, 0, 0], ['X', 'O', 'X']]
    board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

    somebody_won = False
    all_filled = False

    player_X_moves = []
    player_O_moves = []
    turn = 'X' # starting turn is for player X

    print_board(board)
    
    while all_filled == False:
        # taking input from player i.e. coordination of board in 1 index
        while True:
            print('Enter coordinate for player ' + turn + ': ', end = '')
            ip = input().split()
            x = 0
            y = 0
            
            if len(ip) != 2:
                print('invalid input\n')
                continue
            else:
                try:
                    x = int(ip[0])
                    y = int(ip[1])
                except ValueError:
                    print('invalid input\n')
                    continue
            
            coord = [x, y] #list(map(int, ip))

            # convert to 0 index from 1 index
            coord[0] -= 1
            coord[1] -= 1

            # get the list of free valid cells
            coord_left = []
            for i in range(3):
                for j in range(3):
                    if board[i][j] == ' ':
                        coord_left.append([i, j])

            # validate user input coord
            if coord in coord_left:
                break
            else:
                print_board(board)
                print('invalid input\n')

        if turn == 'X':
            player_X_moves.append(coord)
            board[coord[0]][coord[1]] = 'X'
        else:
            player_O_moves.append(coord)
            board[coord[0]][coord[1]] = 'O'

        # clear screen and print board
        print_board(board)

        # check if player won
        somebody_won = win_check(board, turn)
        if somebody_won == True:
            print('Player ' + turn + ' has won the game!\n')
            break

        blank_count = 0
        for row in board:
            for col in row:
                if col == ' ':
                    blank_count += 1

        if blank_count == 0:
            all_filled = True

        # toggle turn
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'
        
    if somebody_won == False:
        print('Its a DRAW!\n')


    print('GAME OVER!\n')

    print('Press r for rematch or q to quit\n')
    print('ENter your choice: ', end = '')
    ip = input()
    if ip == 'q': break


