#TICTACTOE
'''
1 | 2 | 3
----------
4 | 5 | 6
-----------
7 | 8 | 9
'''
def drawBoard(board):
    print(' ',board[0],' | ', board[1],' | ', board[2])
    print('-'*16)
    print(' ',board[3],' | ', board[4],' | ', board[5])
    print('-'*16)
    print(' ',board[6],' | ', board[7],' | ', board[8])

def determineWinner(board):
    if board[0] == board[1] and board[1] == board[2]:
        return board[0]
    elif board[3] == board[4] and board[4] == board[5]:
        return board[3]
    elif board[6] == board[7] and board[7] == board[8]:
        return board[6]
    elif board[0] == board[3] and board[3] == board[6]:
     return board[0]
    elif board[1] == board[4] and board[4] == board[7]:
        return board[1]
    else:
        return '?'

def isAvailable(board,pos):
    if board[pos - 1] ==str(pos):
        return True
    return False

#check if the board is full
def isFull(board):
    for i in range(9):
        if board[i] == str(i+1):
            return False
        return True



def main():
#define the board
    board = list('123456789')
    
 #ASSIGN PLAYERS' PIECES
player1 = 'X'
player2 = 'O'

if determineWinner(board) == '?' and not isFull(board):
    drawBoard(board)
    pos = int(input("Select your move: "))
    while str(pos) not in '123456789' and isAvailable(board, pos):
     pos = int(input("Select your move: "))  
#Store the move in the board
     board[pos-1] = player1

    if determineWinner(board) == '?' and not isFull(board):
        drawBoard(board)
    pos = int(input("Select your move: "))
    while str(pos) not in '123456789' and isAvailable(board, pos):
     pos = int(input("Select your move: "))  
#Store the move in the board
     board[pos-1] = player2

#did someone win?
    winner = determineWinner(board)
     if winner == player1:
         print('Player One won!!!')
    elif winner == player2:
    print('Player two won!!')
else:
    print("it was a tie!")

main() 