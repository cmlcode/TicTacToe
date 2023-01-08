from cell import Cell

class Board(object):
    '''
    Board object the game is played on with num_cells number of cell objects
    Contains a board of binary values with the following logic,

    Binary Table:

        0|1|2
        -----
        3|4|5
        -----
        6|7|8

        '0':'0b 100 000 000 100 000 000 100 000',
        '1':'0b 010 000 000 000 100 000 000 000',
        '2':'0b 001 000 000 000 000 100 000 100',
        '3':'0b 000 100 000 010 000 000 000 000',
        '4':'0b 000 010 000 000 010 000 010 010',
        '5':'0b 000 001 000 000 000 010 000 000',
        '6':'0b 000 000 100 001 000 000 000 001',
        '7':'0b 000 000 010 000 001 000 000 000',
        '8':'0b 000 000 001 000 000 001 001 000',

        '9':'0b 010 010 010 010 010 010 010 010',

        Row 1: 1st byte
        Row 2: 2nd byte
        Row 3: 3rd byte
        Col 1: 4th byte
        Col 2: 5th byte
        Col 3: 6th byte
        Dia 1: 7th byte (Top left to bottom right)
        Dia 2: 8th byte (Top right to bottom left)

        Whenever a player plays on a cell, their binary board is OR'd against the cell they play
        For example, if a player plays on cells 0,1, and 2 their binary board would be,
        111000000100100100100100 because it was OR'd against the binary board cells for 0, 1, and 2
        This is used to detect a winner as described in controller's check_win function

    :param num_cells: number of cells on the board
    '''

    def __init__(self, num_cells: int) -> None:
        self.num_cells = num_cells
        self.board_obj = []
        self.binary_board={
            0:0b100000000100000000100000,
            1:0b010000000000100000000000,
            2:0b001000000000000100000100,
            3:0b000100000010000000000000,
            4:0b000010000000010000010010,
            5:0b000001000000000010000000,
            6:0b000000100001000000000001,
            7:0b000000010000001000000000,
            8:0b000000001000000001001000,
        }
        for cell_num in range(num_cells):
            self.board_obj.append(Cell(cell_num))

    def __str__(self) -> str:
        '''
        Gets the board as a string 3x3 square of cells with borders
        
        :returns: string value of the board with borders
        '''
        output_str =f'{self.get_cell(0)} | {self.get_cell(1)} | {self.get_cell(2)}'
        output_str+=f'\n----------'
        output_str+=f'\n{self.get_cell(3)} | {self.get_cell(4)} | {self.get_cell(5)}'
        output_str+=f'\n----------'
        output_str+=f'\n{self.get_cell(6)} | {self.get_cell(7)} | {self.get_cell(8)}'
        return output_str

    def get_num_cells(self) -> int:
        '''
        Returns the number of cells in the board

        :returns: int value of number of cells in the board
        '''
        return self.num_cells
    def get_board(self):
        '''
        Returns the array of Cells that makes up the board

        :returns: Cell array of the board
        '''
        return self.board_obj
    def get_binary(self,cell_num: int):
        '''
        Gets the binary value of the cell in position cell_num

        :param cell_num: cell position to get binary value of

        :returns: binary value of the cell_position provided
        '''
        return self.binary_board[cell_num]

    def get_cell(self,cell_num: int) -> Cell:
        '''
        Gets the cell object at position cell_num

        :param cell_num: position of cell to get

        :returns: Cell object at the position given
        '''
        return self.get_board()[cell_num]

    def set_cell_val(self, cell_num: int, cell_val: str) -> bool:
        '''
        Checks if the cell at position given is an integer that has not been played on yet
        If the cell has not been played on yet, the value of the cell at position given is updated
        

        :param cell_num: position of cell object to set value of
        :param cell_val: value to set the cell's val to

        :returns: True if can set the cell's value, false otherwise
        '''
        if type(self.get_cell(cell_num).get_val()) == int:
            self.get_cell(cell_num).set_val(cell_val)
            
            return True
        return False

    def reset_board(self):
        '''Resets the board to new cell objects for the number of cells in the board object'''
        self.board_obj = []
        for cell_num in range(self.get_num_cells()):
            self.board_obj.append(Cell(cell_num))
    
    