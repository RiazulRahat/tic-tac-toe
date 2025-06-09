from RLTools.RLTools.utilities import seeding

seeding()

class GS_tictactoe:

    # initialize board state in the beginning
    def __init__(self):
        self.contains = [['-','-','-'],
                         ['-','-','-'],
                         ['-','-','-']]
        
        self.moves = []