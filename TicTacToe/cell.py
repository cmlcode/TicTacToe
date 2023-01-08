class Cell(object):
    '''
    Individual cell in the board

    :param cell_num: cell's spot on the board, becomes the default cell value
    '''

    def __init__(self, cell_num: str) -> None:
        self.val = cell_num

    def __str__(self) -> str:
        '''
        Gets the cell as a string of its value

        :returns: cell value as a string
        '''
        return f'{self.get_val()}'

    def set_val(self,val: str):
        '''
        Sets the cell's value to string provided

        :param val: string version of cell's new value
        '''
        self.val = val.capitalize()
    def get_val(self) -> str:
        '''
        Returns the cell's val

        :returns: cell's val as a string
        '''
        return self.val