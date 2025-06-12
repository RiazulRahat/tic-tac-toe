
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