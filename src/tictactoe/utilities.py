# Function Structure from -> CS50 AI - project 0 (tic-tac-toe)

def player(board):
    """
    Returns player whose turn is on the board.
    """
    return board.max_turn

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
    if board.contains[action[0]][action[1]] == '-':
            board.contains[action[0]][action[1]] = 'O' if board.max_turn else 'X'
            board.moves.append(action)
            board.max_turn = not board.max_turn
    else:
        raise ValueError("Invalid")
    
    return board

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if board.winner == 'X':
        return "X wins!"
    elif board.winner == 'O':
        return "O wins!"
    else:
        return "Draw"
        #return None # cs50 - default return
    
def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    return board.is_game_over()

def utility(board):
    """
    Returns 1 if O has won the game, -1 if X has won, 0 otherwise.
    """
    if board.winner == 'O':
        return 1
    elif board.winner == 'X':
        return -1
    
    return 0

def remove_move(board):
    '''Remove last move'''
    oldBoard = board
    if len(oldBoard.moves) == 0:
        return None
    move = oldBoard.moves.pop()
    oldBoard.contains[move[0]][move[1]] = '-'
    oldBoard.max_turn = not oldBoard.max_turn
    oldBoard.winner = '-'
    return oldBoard

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    # Check: Game is over
    if terminal(board):
        return None
    else:
        # go to helper functions - depending on turn
        if board.max_turn:
            _val, move = _maxVal(board)
        else:
            _val, move = _minVal(board)
    
    return move

def _maxVal(board):
    # Check: Game is over
    if terminal(board):
        return utility(board), None

    val = float('-inf')
    move = None

    for action in actions(board):
        # mutates board with new move to get value
        result(board, action)
        newVal, _move = _minVal(board)
        # mutate board back to original
        remove_move(board)

        if newVal > val:
            val = newVal
            move = action
            
            if val == 1:
                break
            
    return val, move
    
def _minVal(board):
    # Check: Game is over
    if terminal(board):
        return utility(board), None
    
    val = float('inf')
    move = None
    for action in actions(board):
        # mutates board with new move to get value
        result(board, action)
        newVal, _move = _maxVal(board)
        # mutate board back to original
        remove_move(board)

        if newVal < val:
            val = newVal
            move = action
            
            if val == -1:
                break

    return val, move