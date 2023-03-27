# This is a game of Tic Tack Toe by Arik Vaserman

def main():
Intro = introduction()
game_board=create_playground()
printboard=printheboard(board)
mark, mark_player_2=game_marks()
fullboard=isTheBoardFull (board, mark, mark_player_2)



# Introduction to Arik's Tic Tack Toe game
def introduction():
    print("Hello and welcome to Arik's Tic Tac Toe game")
    print ("\n")
    print("Rules: This game is for two players, one will play as X and the other as O,"
          "This game play in turn, X begins. the game will be played un grid 3*3 "
          "the player who succeeds in placing three of their marks wins ")
    print("\n")
    input ("press enter to continue.")

# create playground
def crete_playground():
    board = [[" "," "," "],
             [" "," "," "],
             [" "," "," "]]
    return board

# Geme marks
def game_marks():
    mark = input("please pick X or O")
    if mark=="X":
        mark_player_2="O"
        print("player 2 you will play with O")
    else:
        mark_player_2="X"
    return (mark, mark_player_2)

# Start game
def game_start(board, mark, mark_player_2, count):
    if count % 2 ==0:
    player_1 = mark
    elif count % 2 ==1:
    player_1=mark_player_2
    print ("it's your turn")
    row = int (input("pick a row""[upper row: enter 0, middle row= enter 1, bottom row: enter 2]:"))
    column = int (input("pick a column:""[upper column: enter 0, middle column= enter 1, bottom column: enter 2]:"))

    while (row > 2 or row < 0) or (column > 2 or column < 0):
        outOfBoard(row, column)
        row = int(input("Pick a row[upper row:"
                        "[enter 0, middle row: enter 1, bottom row: enter 2]:"))
        column = int(input("Pick a column:"
                           "[left column: enter 0, middle column: enter 1, right column enter 2]"))

 # Check if filled
    while (board[row][column] == mark) or (board[row][column] == mark_player_2):
        filled = illegal(board, mark, mark_player_2, row, column)
        row = int(input("Pick a row[upper row:"
                        "[enter 0, middle row: enter 1, bottom row: enter 2]:"))
        column = int(input("Pick a column:"
                           "[left column: enter 0, middle column: enter 1, right column enter 2]"))

 # Locates player's spot on the board
    if player == mark:
        board[row][column] = mark

    else:
        board[row][column] = mark_player_2

    return (board)

# Check if the board is full
def isTheBoardFull (board, mark, mark_player_2):
    count = 1
    the_winner = True
    while count < 10 and the_winner == True:
        gaming = startGame(board, mark, mark_player_2, count)
        pretty = printmyboard(board)

        if count == 9:
            print("The board is full. Game over.")
            if the_winner == True:
                print("There is a tie")

        # Check if here is a winner
        the_winner = isWinner(board, mark, mark_player_2, count)
        count += 1
    if the_winner == False:
        print("Game over amigo.")

#  report
    report(count, the_winner, mark, mark_player_2)

# Tells the players that their selection is out of range
    def outOfTheBoard(row, column):
    print("Out of boarder")

# print the board
def printheboard(board):
    rows_of_the_board = len(board)
    col_of_the_board = len(board)
    print("---+---+---")
    for r in range(rows_of_the_board):
        print(board[r][0], " |", board[r][1], "|", board[r][2])
        print("---+---+---")
    return board

# who is the winner
def isWinner(board, mark, mark_player_2, count):
    the_winner = True
    # Check the rows
    for row in range(0, 3):
        if (board[row][0] == board[row][1] == board[row][2] == mark):
            the_winner = False
            print("Player " + mark + ", you won!")

        elif (board[row][0] == board[row][1] == board[row][2] == mark_player_2):
            the_winner = False
            print("Player " + mark_player_2 + ", you won!")

    # Check the columns
    for col in range(0, 3):
        if (board[0][col] == board[1][col] == board[2][col] == mark):
            the_winner = False
            print("Player " + mark + ", you won!")
        elif (board[0][col] == board[1][col] == board[2][col] == mark_player_2):
            winner = False
            print("Player " + mark_player_2 + ", you won!")

    # Check the diagnoals
    if board[0][0] == board[1][1] == board[2][2] == mark:
        the_winner = False
        print("Player " + mark + ", you won!")

    elif board[0][0] == board[1][1] == board[2][2] == mark_player_2:
        the_winner = False
        print("Player " + mark_player_2 + ", you won!")

    elif board[0][2] == board[1][1] == board[2][0] == mark:
        the_winner = False
        print("Player " + mark + ", you won!")

    elif board[0][2] == board[1][1] == board[2][0] == mark_player_2:
        the_winner = False
        print("Player " + mark_player_2 + ", you won!")

    return the_winner


def illegal(board, mark, mark_player_2, row, column):
    print("The square you picked is already filled. Pick another one.")


def report(count, the_winner, mark, mark_player_2):
    print("\n")
    input("Press enter to see the game summary. ")
    if (the_winner == False) and (count % 2 == 1):
        print("Winner : Player " + symbol_1 + ".")
    elif (the_winner == False) and (count % 2 == 0):
        print("Winner : Player " + symbol_2 + ".")
    else:
        print("There is a tie. ")

main()











