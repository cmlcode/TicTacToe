class Cell(object):
    def __init__(self, cell_num: int) -> None:
        self.val = cell_num

    def __str__(self) -> str:
        '''
        Gets the cell as a string of its value

        Returns:
            Cell value as a string
        '''
        return f'{self.get_val()}'

    def set_val(self,val: str):
        '''
        Sets the cell's value to string provided

        Args:
            val: string version of cell's new value
        '''
        self.val = val.capitalize()
    def get_val(self) -> str:
        return self.val