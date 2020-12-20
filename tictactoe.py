import copy
import random
import math
"""
Tic Tac Toe Player
"""



X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    numOfX = 0
    numOfY = 0

    for i in board:
        numOfX += i.count(X)
        numOfY += i.count(O)

    if numOfX == numOfY:
        return X
    return O



def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possibleWays = set()
    row = 0
    for i in board:
        column = 0
        for j in i:
            if j == EMPTY:
                possibleWays.add((row, column))
            column += 1
        row += 1

    return possibleWays


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    newboard = copy.deepcopy(board)
    # print(newboard)
    if action == None:
        raise Exception
    row , column = action

    if newboard[row][column] is not EMPTY:
        raise Exception("Ooops! There is some value on your coords.")
    newboard[row][column] = player(newboard)
    return newboard


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for line in lines(board):
        if len(set(line)) == 1 and line[0] is not None:
            print(line[0])
            return line[0]
    return None





def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    numOfEmptys = 0

    for i in board:
        numOfEmptys += i.count(EMPTY)

    if numOfEmptys == 0 or winner(board) == X or winner(board) == O:
        return True
    return False




def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0



def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    current_player = player(board)
    if terminal(board):
        return None

    if board == initial_state():
        return (random.randint(0,2),random.randint(0,2))

    if current_player == X:
        move = None
        value = -math.inf
        for action in actions(board):
            tempVal = maxValue(result(board,action))
            if tempVal > value:
                value = tempVal
                move = action
    if current_player == O:
        move = None
        value = math.inf
        for action in actions(board):
            tempVal = minValue(result(board,action))
            if tempVal < value:
                value = tempVal
                move = action

    return move

def _lines(board):
    yield from board  # the rows
    yield [board[i][i] for i in range(len(board))]  # one of the diagonals

def lines(board):
    yield from _lines(board)
    # rotate the board 90 degrees to get the columns and the other diagonal
    yield from _lines(list(zip(*reversed(board))))

def maxValue(board):
    value = -math.inf
    if terminal(board):
        return utility(board)

    for action in actions(board):
        value = max(value,minValue(result(board,action)))
    return value


def minValue(board):
    value = math.inf
    if terminal(board):
        return utility(board)

    for action in actions(board):
        value = min(value, maxValue(result(board, action)))
    return value