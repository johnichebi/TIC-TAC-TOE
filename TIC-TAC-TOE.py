                #!!!MY FIRST PROJECT.py!!!
board = ['#','X','O','X','O','X','O','X','O','X']

def display_board(board):
  
    print('\n' * 100)
    print(board[1]+' | '+board[2]+' | '+board[3])
    print(board[4]+' | '+board[5]+' | '+board[6])
    print(board[7]+' | '+board[8]+' | '+board[9])

def player_input():
    choice = 'a'
    while choice not in ['X','O']:
        choice = input('Player1, do you wish to be X or O!: ').upper()
    if choice == 'X':
        return ('X','O')
    else:
        return('O','X')

def how_to_play():
  
    print('In the board displayed below, you are to pick a number  and assign your marker(X or O) to it.')

def place_marker(board,choice,position):
    board[position] = choice

def win_check(board,choice):
    return((board[1] == board[2] ==board[3] == choice) or #COLUMN1
    (board[7] == board[8] ==board[9] == choice) or #COLUMN2
    (board[1] == board[4] ==board[7] == choice) or #COLUMN3
    (board[8] == board[5] ==board[2] == choice) or #ROW1
    (board[9] == board[6] ==board[3] == choice) or #ROW2
    (board[1] == board[5] ==board[9] == choice) or #ROW3
    (board[4] == board[5] ==board[6] == choice) or #DIAGONAL1
    (board[3] == board[5] ==board[7] == choice))   #DIAGONAL2

import random 

def choose_first():
    flip = random.randint(0,1)

    if flip == 0:
        return "Player 1"
    else:
        return "Player 2"

def space_check(board,position):

    return board[position] == ' '

def full_board(board):

    for i in board:
        if space_check:
            return False
        else:
            pass
    return True

def player_choice(board):

    position = 0

    while position not in range(1,10) or space_check(board,position) == False:
        position = int(input('Choose a valid position: (1-9) '))

    return position

def replay(): 

    choice1 = ' '
    while choice1 not in ["Y","N"]:
        choice1 = input('Do you wish to continue playing? Enter Y or N ')
    if choice1 == "Y":
        return True
    else:
        pass
    return False

 
print("Welcome to TIC TAC TOE!")

while True:
    board = [' ']*10
    player1,player2 = player_input()
    turn = choose_first()
    print(f"{turn} will go first")
    play_game = input('Ready to play? Y or N ')
    
    if play_game == 'Y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            display_board(board)
            position = player_choice(board)
            place_marker(board,player1,position)

            if win_check(board,player1):
                display_board(board)
                print("CONGRATULATIONS Player 1, you've won!")
                game_on = False
                
            else:
              
                if  full_board(board):
                    display_board(board)
                    print("The game is a tie!!")
                    game_on = False
                    
                else:
                  
                    turn = 'Player 2'
        else:
            display_board(board)
            position = player_choice(board)
            place_marker(board,player2,position)
            
            if win_check(board,player2):
                display_board(board)
                print("CONGRATULATIONS Player 2, you've won!")
                game_on = False
                
            else:

                if  full_board(board):
                    display_board(board)
                    print("The game is a tie!!")
                    game_on = False
                else:
                    turn = 'Player 2'

            

#how_to_play()
#display_board(['#','1','2','3','4','5','6','7','8','9'])
#choice = marker
