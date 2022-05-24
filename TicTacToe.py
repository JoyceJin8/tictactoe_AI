import random
import time
global comIcon, userIcon

def printBoard(board):
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('-----------')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('-----------')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])

def getboardCopy(board):
    boardCopy = []

    for i in board:
        boardCopy.append(i)

    return boardCopy

def playAgain(answer):
    if answer == "yes":
        playGame()
    else:
        exit()

def goFirst(turnNum):
    if turnNum == 1:
        return "computer"
    else:
        return "player"

def isBoardFull(board):
    #check if the board is full, if so ask to replay
    boardFull = True
    for x in range(1,10):
        if board[x] == " ":
            boardFull = False

    if boardFull == True:
        print("TIE! Would you like to play again? (yes or no)")
        answer = input().lower()
        playAgain(answer)

def isWinner(board, userIcon, comIcon):
    #checks who wins
    if board[1] == userIcon and board[2] == userIcon and board[3] == userIcon or board[4] == userIcon and board[5] == userIcon and board[6] == userIcon or board[7] == userIcon and board[8] == userIcon and board[9] == userIcon or board[1] == userIcon and board[4] == userIcon and board[7] == userIcon or board[2] == userIcon and board[5] == userIcon and board[8] == userIcon or board[3] == userIcon and board[6] == userIcon and board[9] == userIcon or board[1] == userIcon and board[5] == userIcon and board[9] == userIcon or board[3] == userIcon and board[5] == userIcon and board[7] == userIcon:
        print("YOU WIN! Would you like to play again? (yes or no)")
        answer = input().lower()
        playAgain(answer)

    if board[1] == comIcon and board[2] == comIcon and board[3] == comIcon or board[4] == comIcon and board[5] == comIcon and board[6] == comIcon or board[7] == comIcon and board[8] == comIcon and board[9] == comIcon or board[1] == comIcon and board[4] == comIcon and board[7] == comIcon or board[2] == comIcon and board[5] == comIcon and board[8] == comIcon or board[3] == comIcon and board[6] == comIcon and board[9] == comIcon or board[1] == comIcon and board[5] == comIcon and board[9] == comIcon or board[3] == comIcon and board[5] == comIcon and board[7] == comIcon:
        print("THE COMPUTER WINS. Would you like to play again? (yes or no)")
        answer = input().lower()
        playAgain(answer)

def playerMove(board,userIcon):
    #lets user input their icon
    while True:
        number = int(input("Choose where you want to play (1-9): "))
        if 0<number<10:
            if board[number] == " ":
                board[number] = userIcon
                printBoard(board)
                break
            else:
                print("That spot is taken, choose again")
        else:
            print("Only choose a number between 1-9")

def computerMove(board,comIcon, userIcon):
    #choose winning play
    for i in range(1, 10):
        if board[i] == " ":
            copy = getboardCopy(board)
            copy[i] = comIcon
            if comWinner(copy, comIcon) == True:
                board[i] = comIcon
                time.sleep(1.2)
                printBoard(board)
                return

    #choose block
    for i in range(1, 10):
        if board[i] == " ":
            copy = getboardCopy(board)
            copy[i] = userIcon
            if userWinner(copy, userIcon) == True:
                board[i] = comIcon
                time.sleep(1.2)
                printBoard(board)
                return

    #choose middle spot if not taken
    if board[5] == " ":
        time.sleep(1.2)
        board[5] = comIcon
        printBoard(board)
        return
    else:
    #choses randomly
        while True:
            number = random.randint(1, 9)
            if board[number] == " ":
                board[number] = comIcon
                time.sleep(1.2)
                printBoard(board)
                return

def comWinner(copy, comIcon):
    if copy[1] == comIcon and copy[2] == comIcon and copy[3] == comIcon or copy[4] == comIcon and copy[5] == comIcon and copy[6] == comIcon or copy[7] == comIcon and copy[8] == comIcon and copy[9] == comIcon or copy[1] == comIcon and copy[4] == comIcon and copy[7] == comIcon or copy[2] == comIcon and copy[5] == comIcon and copy[8] == comIcon or copy[3] == comIcon and copy[6] == comIcon and copy[9] == comIcon or copy[1] == comIcon and copy[5] == comIcon and copy[9] == comIcon or copy[3] == comIcon and copy[5] == comIcon and copy[7] == comIcon:
        return True

def userWinner(copy, userIcon):
    if copy[1] == userIcon and copy[2] == userIcon and copy[3] == userIcon or copy[4] == userIcon and copy[5] == userIcon and copy[6] == userIcon or copy[7] == userIcon and copy[8] == userIcon and copy[9] == userIcon or copy[1] == userIcon and copy[4] == userIcon and copy[7] == userIcon or copy[2] == userIcon and copy[5] == userIcon and copy[8] == userIcon or copy[3] == userIcon and copy[6] == userIcon and copy[9] == userIcon or copy[1] == userIcon and copy[5] == userIcon and copy[9] == userIcon or copy[3] == userIcon and copy[5] == userIcon and copy[7] == userIcon:
        return True

def playGame():
    #clears the board
    for x in range(1,10):
        board[x] = " "

    #chose X or O
    while True:
        userIcon = input("Would you like to be X or O?: ").upper()

        if userIcon != "X" and userIcon != "O":
            print("Please chose only X or O")
        else:
            break

    if userIcon == "X":
        comIcon = "O"
    else:
        comIcon = "X"

    printBoard(board)
    numStart = random.randint(0, 2)
    turn = goFirst(numStart)

    while True:
        if turn == "player":
            print("Your turn")
            playerMove(board, userIcon)
            isWinner(board, userIcon, comIcon)
            isBoardFull(board)
            turn = "computer"
        else:
            print("Computers turn")
            computerMove(board, comIcon, userIcon)
            isWinner(board, userIcon, comIcon)
            isBoardFull(board)
            turn = "player"

print(' ' + "1" + ' | ' + "2" + ' | ' + "3")
print('-----------')
print(' ' + "4" + ' | ' + "5" + ' | ' + "6")
print('-----------')
print(' ' + "7" + ' | ' + "8" + ' | ' + "9")
board = [' ']*10
playGame()

