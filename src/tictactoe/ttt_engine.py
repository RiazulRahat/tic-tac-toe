#from RLTools.RLTools.utilities import seeding

#seeding()

class GS_tictactoe:

    # initialize contains state in the beginning
    def __init__(self):
        self.contains = [['-','-','-'],
                         ['-','-','-'],
                         ['-','-','-']]
        
        self.moves = []

    # Private Functions
    def _rowCheck(self):
        for row in self.contains:
            if (row[0] != '-') and (row[0] == row[1] == row[2]):
                return True
            
        return False
    
    def _colCheck(self):
        for col in range(3):
            if (self.contains[0][col] != '-') and (self.contains[0][col] == self.contains[1][col] == self.contains[2][col]):
                return True
            
        return False
    
    def _diagCheck(self):
        if (self.contains[0][0] != '-') and (self.contains[0][0] == self.contains[1][1] == self.contains[2][2]):
            return True
        if (self.contains[0][2] != '-') and (self.contains[2][0] == self.contains[1][1] == self.contains[0][2]):
            return True
        
        return False
    
    def is_game_over(self):
        if len(self.moves) == 9:
            return True
        
        return self._rowCheck() or self._colCheck() or self._diagCheck()
    
