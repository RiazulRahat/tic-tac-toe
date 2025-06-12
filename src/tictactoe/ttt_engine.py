#from RLTools.RLTools.utilities import seeding

#seeding()

class GS_tictactoe:

    def __init__(self):
        # current board state
        self.contains = [['-','-','-'],
                         ['-','-','-'],
                         ['-','-','-']]
        
        # contains stack of moves leading up to current board state
        self.moves = []
        self.winner = '-'
        self.max_turn = True

    # Private Functions
    def _rowCheck(self):
        for row in self.contains:
            if (row[0] != '-') and (row[0] == row[1] == row[2]):
                self.winner = row[0]
                return True
            
        return False
    
    def _colCheck(self):
        for col in range(3):
            if (self.contains[0][col] != '-') and (self.contains[0][col] == self.contains[1][col] == self.contains[2][col]):
                self.winner = self.contains[0][col]
                return True
        return False
    
    def _diagCheck(self):
        if (self.contains[0][0] != '-') and (self.contains[0][0] == self.contains[1][1] == self.contains[2][2]):
            self.winner = self.contains[0][0]
            return True
        if (self.contains[0][2] != '-') and (self.contains[2][0] == self.contains[1][1] == self.contains[0][2]):
            self.winner = self.contains[2][0]
            return True
        return False
    # ------------------

    def is_game_over(self):
        '''Check if game is over!'''
        return self._rowCheck() or self._colCheck() or self._diagCheck() or (len(self.moves) == 9)
    
    def remove_move(self):
        '''Remove last move'''
        if len(self.moves) == 0:
            return None
        move = self.moves.pop()
        self.contains[move[0]][move[1]] = '-'
        self.max_turn = not self.max_turn

    def print_winner(self):
        if self.winner == 'X':
            return "X wins!"
        elif self.winner == 'O':
            return "O wins!"
        else:
            return "Draw!"
    
    def make_move(self, move):
        if self.contains[move[0]][move[1]] == '-':
            self.contains[move[0]][move[1]] = 'O' if self.max_turn else 'X'
            self.moves.append(move)
            self.max_turn = not self.max_turn
