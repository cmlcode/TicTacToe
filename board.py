from cell import Cell

class Board(object):
    def __init__(self, num_cells: int) -> None:
        self.num_cells = num_cells
        self.board_obj = []
        '''
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
        '''
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

    def __str__(self):
        output_str =f'{self.get_cell(0)} | {self.get_cell(1)} | {self.get_cell(2)}'
        output_str+=f'\n----------'
        output_str+=f'\n{self.get_cell(3)} | {self.get_cell(4)} | {self.get_cell(5)}'
        output_str+=f'\n----------'
        output_str+=f'\n{self.get_cell(6)} | {self.get_cell(7)} | {self.get_cell(8)}'
        return output_str

    def get_num_cells(self) -> int:
        return self.num_cells
    def get_board(self):
        return self.board_obj
    def get_binary(self,cell_num):
        return self.binary_board[cell_num]

    def get_cell(self,cell_num) -> Cell:
        return self.get_board()[cell_num]

    def set_cell_val(self, cell_num: int, cell_val: str) -> bool:
        if type(self.get_cell(cell_num).get_val()) == int:
            self.get_cell(cell_num).set_val(cell_val)
            
            return True
        return False

    def reset_board(self):
        self.board_obj = []
        for cell_num in range(self.num_cells):
            self.board_obj.append(Cell(cell_num))
    
    