class Player(object):
    '''
    Player object with it's symbol that it plays, record of results, and binary board of positions played
    Binary board starts as all 0's and OR's it's values against the binary value of cell on the board as updates
    To check wins, the binary board is compared with the binary board shifted both directions and repeated 010's
    For more information on how binary board works, check board object's comments and controller's check win comments

    :param symbol: string value of symbol the player will use, symbol is automatically capitalized
    '''

    def __init__(self,symbol:str):
        self.symbol = symbol.capitalize()
        self.record = {'win':0,'loss':0,'draw':0}
        self.binary_board=0b000000000000000000000000000

    def set_symbol(self,symbol:str):
        '''
        Sets the symbol the player object will use

        :param symbol: String symbol player will use, symbol is automatically capitalized
        '''
        self.symbol = symbol.capitalize()

    def get_symbol(self) -> str:
        '''
        Gets the player's symbol

        :returns: string value of symbol player will play
        '''
        return self.symbol

    def set_record(self,record):
        '''
        Sets the player's record

        param: dictionary of player's win, draw, and loss records
        '''
        self.record = record

    def get_record(self):
        '''
        Returns the player's record

        :returns: dictionary of player's win, draw, and loss records
        '''
        return self.record

    def set_binary_board(self,binary_board):
        '''
        Sets the binary board the player willl play with

        :param binary_board: the binary value the player's binary_board will become
        '''
        self.binary_board = binary_board

    def get_binary_board(self):
        '''
        Gets the player's binary board

        :returns: binary value of the positions the player has played on
        '''
        return self.binary_board

    def add_record(self,result: int):
        '''
        Adds the result of the round to the player's record
        If result is 1, player won
        If result is 0, player drew
        If result is -1, player lost

        :param result: int value of player's result from the round 
        '''
        if result == 1:
            self.record['win'] += 1
        elif result == 0:
            self.record['draw'] += 1
        elif result == -1:
            self.record['loss'] += 1

    def reset_binary(self):
        '''Resets the binary board to binary value of all 0's'''
        self.set_binary_board(0b000000000000000000000000000)