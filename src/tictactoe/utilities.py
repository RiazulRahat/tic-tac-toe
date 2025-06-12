
from ttt_engine import GS_tictactoe as ttt

board = ttt()

def player(board):
    """
    Returns player who has the next turn on a board.
    """
    return not board.max_turn

def actions(board):
    """
    Returns set of all possible actions (row, col) available on the board.
    """
    movesList = []
    for row in range(3):
        for col in range(3):
            if board.contains[row][col] == '-':
                movesList.append((row,col))
    
    return movesList

def result(board, action):
    """
    Returns the board that results from making move action - (i, j) on the board.
    """

    # Currently changes the current board object
    if board.contains[action[0]][action[1]] == '-':
            board.contains[action[0]][action[1]] = 'O' if board.max_turn else 'X'
            board.moves.append(action)
            board.max_turn = not board.max_turn

    return board