from player import Player
from board import Board
import random

class Controller(object):
    '''Class that controls the individual component's of the game'''

    def __init__(self):
        self.set_turn_count(0)
        self.create_players()
        self.set_board(Board(9))
        self.playing=True
        self.result=None

    def set_playing(self,playing: bool):
        '''
        Sets whether game is going on

        :param playing: boolean value of whether game is active
        '''
        self.playing = playing

    def get_playing(self) -> bool:
        '''
        Returns whether the game is going on

        :returns: whether game is still going on as a boolean value
        '''
        return self.playing

    def set_result(self,result: bool):
        '''
        Sets the result of the game

        :param result: boolean result of the game (True if there is a winner, False otherwise)
        '''
        self.result = result

    def get_result(self) -> bool:
        '''
        Returns the result of the game

        :returns: whether someone won the game as a boolean value (True if there is a winner, False otherwise)
        '''
        return self.result

    def set_active_player(self,active_player: Player):
        '''
        Sets which player is actively playing

        :param active_player: player object for the player that is actively playing
        '''
        self.active_player = active_player

    def get_active_player(self) -> Player:
        '''
        Gets which player is actively playing

        :returns: player object that is actively playing
        '''
        return self.active_player

    def create_players(self):
        '''
        Creates objects for player one and two and sets their default symbols(X for player 1 and O for player 2)
        Randomly selects a player object to be the first active player
        '''
        self.set_player_one(Player('x'))
        self.set_player_two(Player('o'))
        self.set_active_player(random.choice([self.get_player_one(),self.get_player_two()]))

    def set_player_one(self,player_one: Player):
        '''
        Sets a player object to player one
        
        :param player_one: player object to become player one
        '''
        self.player_one = player_one

    def get_player_one(self) -> Player:
        '''
        Gets the player object for player one

        :returns: player object for player one
        '''
        return self.player_one

    def set_player_two(self,player_two: Player):
        '''
        Sets a player object to player two
        
        :param player_one: player object to become player two
        '''
        self.player_two = player_two

    def get_player_two(self) -> Player:
        '''
        Gets the player object for player two

        :returns: player object for player two
        '''
        return self.player_two

    def set_turn_count(self,turn_count: int):
        '''
        Sets the turn number

        :param turn_count: int value for the turn number
        '''
        self.turn_count = turn_count

    def get_turn_count(self) -> int:
        '''
        Gets the turn number as an int

        :returns: turn count as an int
        '''
        return self.turn_count

    def set_board(self, board: Board):
        '''
        Sets the board object the game is played on

        :param board: board object that controller will use
        '''
        self.board = board

    def get_board(self) -> Board:
        '''
        Gets the board object the game is played on

        :returns: board object the controller object is using
        '''
        return self.board

    def play_turn(self,cell_num: int) -> bool:
        '''
        Plays one player's turn in the game
        Uses switch_players(), check_win(), end_game(), and player's binary board

        :param cell_num: which cell the player is playing on

        :returns: boolean value of if user can pay on a cell(True if can, False otherwise)
        '''
        if self.get_board().set_cell_val(cell_num,self.get_active_player().get_symbol()):
            self.get_active_player().set_binary_board(self.get_active_player().get_binary_board() | self.get_board().get_binary(cell_num))
            self.turn_count+=1
            if self.turn_count>=9:
                if self.check_win():
                    self.set_result(True)
                    self.end_game()
                else:
                    self.set_result(False)
                    self.end_game()
                return True
            if self.turn_count>=5 and self.check_win():
                self.set_result(True)
                self.end_game()
                return True
            self.switch_player()
            return True
        else:
            return False

    def switch_player(self):
        '''Switches which player is active'''
        if self.active_player == self.player_one:
            self.set_active_player(self.get_player_two())
        else:
            self.set_active_player(self.get_player_one())

    def get_cell_val(self, cell_num: int) -> str:
        '''
        Gets the value of the cell at a certain position

        :param cell_num: number of cell accessed
        
        :returns: str value of cell accessed

        '''
        return self.get_board().get_cell(cell_num).get_val()

    def check_win(self) -> bool:
        '''
        Checks if winner is accessed
        Gets the active player's binary board
        Shifts binary board to the left one and stores value
        Shifts binary board to the right one and stores value
        AND's all binary boards
        AND's combined boards with repeated 010's
        Repeated 010's checks that only 1 that passes through can be in the middle, so must be a winning case
        If integer value is not 0, the player has a winning position
        
        Example,
        If player wins by only playing on first column their binary board is,
        100100100111000000100001
        Left bitshift value is,
        001001001110000001000010
        Right bitshift value is,
        010010010011100000010000

         100100100111000000100001
        &001001001110000001000010
        &010010010011100000010000
         ------------------------
         000000000010000000000000
        &010010010010010010010010
         ------------------------
         000000000010000000000000

        Because the int value of the binary value is not 0, the player won at a position

        The repeated 010's works because bitshift can make the value a non-zero number by combining wrong cells without it
        However, the combined binary values is not centered in the middle of the three values
        For example, we'll show if a player only played on cells 1, 2, and 3, which is not a winning combination
        Their binary board is,
        011100000010100100000100
        Left bitshift value is,
        111000000101001000001000
        Right bitshift value is,
        001110000001010010000010

         011100000010100100000100
        &111000000101001000001000
        &001110000001010010000010
         ------------------------
         001000000000000000000000

        The int value of the binary is not zero. However, when AND'ed with 010's the binary value becomes,
        000000000000000000000000

        Therefore, the int value of the binary becomes 0, so the player did not win

        :returns: boolen value for if there is a winner. True if there is a winner, False otherwise
        '''
        original_binary=self.get_active_player().get_binary_board()
        shift_left=self.get_active_player().get_binary_board() << 1
        shift_right=self.get_active_player().get_binary_board() >> 1
        win_val=original_binary & shift_left & shift_right & 0b010010010010010010010010
        if int(win_val)!=0:
            return True
        else:
            return False

    def end_game(self):
        '''
        Adds the game's result to each players records
        Stops the game from continuing and resets the result vaue
        '''
        if self.get_result():
            self.get_active_player().add_record(1)
            self.switch_player()
            self.get_active_player().add_record(-1)
        else:
            self.get_player_one().add_record(0)
            self.get_player_two().add_record(0)
        self.set_playing(False)
        self.set_result(False)

    def reset_game(self):
        '''
        Resets each player's binary board of where they have played
        Resets the board the player's see
        Resets the turn count
        '''
        self.get_player_one().reset_binary()
        self.get_player_two().reset_binary()
        self.get_board().reset_board()
        self.set_turn_count(0)