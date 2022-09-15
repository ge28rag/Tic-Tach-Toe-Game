
def display(board):
    print('Below is the grid')
    print('__'+board[7]+'_|_'+board[8]+'_|_'+board[9]+'__')
    print('__' + board[4] + '_|_' + board[5] + '_|_' + board[6] + '__')
    print( '  '+board[1] + ' | ' + board[2] + ' | ' + board[3] )

sttt = ['#','X','O','X','O','X','O','X','O','X']


def player_input():
    marker=''
    while marker not in ['X','O']:
        marker=input("Pleas enter X or O: ")
        if marker not in ['X','O']:
            print('Please write the correct option')
    player1 = marker
    if player1 == 'X':
        return ('X','O')
    else:
        return ('O','X')

def place_marker(board, marker, position):
    acceptable_list= range(1,10)
    board[position] = marker
    while position not in acceptable_list:
        position=int(input("Write position again: "))
        board[position]= marker




def win_check(board, mark):
    return (board[7]==mark and board[8]==mark and board[9]==mark) or (board[4]==mark and board[5]==mark and board[6]==mark) or (board[1]==mark
    and board[2]==mark and board[3]==mark) or (board[7]==mark and board[4]==mark and board[1]==mark)or (board[8]==mark and
    board[5]==mark and board[2]==mark) or (board[9]==mark and board[6]==mark and board[3]==mark) or (board[7]==mark and
    board[5]==mark and board[3]==mark) or (board[1]==mark and board[5]==mark and board[9]==mark)


import random
def choose_first():
    flip= random.randint(0,1)

    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'

def space_check(board,position):
    return board[position] == ' '


def full_board_check(board):
    for x in range(1,10):

        if board[x] == ' ':
            return False
    return True


def player_choice(board):
    position=0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position = int(input("Enter a position: "))

    return position

def replay():
    ag= input("Want to play again? (Y or N) : ")
    if ag == 'Yes':
        return True
    else:
        return False

print("Welcome to Tic Tac Toe!")
bo = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
while True:
# Play the game
## SET UP EVERYTHING (BOARD, WHO FIRST, MARKER)
    player1_marker,player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first!')

    play_game = input('Ready to play? (y or n)  ')
### Game Play
    if play_game == 'y':
        game_on= True
    else:
        game_on= False
    while game_on:
#### Player 1
        if turn == 'Player 1':
            # Show the board
            display(bo)
            # Choose a position
            position= player_choice(bo)
            # Place a marker on the position
            place_marker(bo,player1_marker,position)
            #check if they won
            if win_check(bo,player1_marker):
                display(bo)
                print("Player 1 has won")
                game_on=False
            # check if there is a tie
            else:
                if full_board_check(bo):
                    display(bo)
                    print("Tie")
                    break
                else:
                    turn= 'Player 2'
        else:
            # Show the board
            display(bo)
            # Choose a position
            position = player_choice(bo)
            # Place a marker on the position
            place_marker(bo, player2_marker, position)
            # check if they won
            if win_check(bo, player2_marker):
                display(bo)
                print("Player 2 has won")
                game_on = False
            # check if there is a tie
            else:
                if full_board_check(bo):
                    display(bo)
                    print("Tie")
                    break
                else:
                    turn = 'Player 1'

    if not replay():
            break




