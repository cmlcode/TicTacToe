class Player(object):
    '''


    '''
    def __init__(self,symbol:str):
        self.symbol = symbol.capitalize()
        self.record = {'win':0,'loss':0,'draw':0}
        self.binary_board=0b000000000000000000000000000

    def set_symbol(self,symbol:str):
        self.symbol = symbol
    def get_symbol(self) -> str:
        return self.symbol
    def set_record(self,record):
        self.record = record
    def get_record(self):
        return self.record
    def set_binary_board(self,binary_board):
        self.binary_board = binary_board
    def get_binary_board(self):
        return self.binary_board
    def add_record(self,result):
        if result == 1:
            self.record['win'] += 1
        elif result == 0:
            self.record['draw'] += 1
        elif result == -1:
            self.record['loss'] += 1
    def reset_binary(self):
        self.set_binary_board(0b000000000000000000000000000)