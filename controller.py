from player import Player
from board import Board
import random

class Controller(object):
    def __init__(self):
        self.set_turn_count(0)
        self.create_players()
        self.set_board(Board(9))
        self.playing=True
        self.result=None

    def set_playing(self,playing: bool):
        '''
        Sets whether game is going on

        Args:
            playing: Boolean value of whether game is active
        '''
        self.playing = playing
    def get_playing(self) -> bool:
        '''
        Returns whether the game is going on

        Returns:
            Whether game is still going on as a boolean value
        '''
        return self.playing
    def set_result(self,result: bool):
        '''
        Sets the result of the game

        Args:
            results: Boolean result of the game (True if there is a winner, False otherwise)
        '''
        self.result = result
    def get_result(self) -> bool:
        '''
        Returns the result of the game

        Returns:
            Whether someone won the game as a boolean value (True if there is a winner, False otherwise)
        '''
        return self.result
    def set_active_player(self,active_player: Player):
        '''
        Sets which player is actively playing

        Args:
            active_player: Player object for the player that is actively playing
        '''
        self.active_player = active_player
    def get_active_player(self) -> Player:
        '''
        Gets which player is actively playing

        Returns:
            Player object that is actively playing
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
        
        Args:
            player_one: player object to become player one
        '''
        self.player_one = player_one
    def get_player_one(self) -> Player:
        '''
        Gets the player object for player one

        Returns:
            Player object for player one
        '''
        return self.player_one
    def set_player_two(self,player_two: Player):
        '''
        Sets a player object to player two
        
        Args:
            player_one: player object to become player two
        '''
        self.player_two = player_two
    def get_player_two(self) -> Player:
        '''
        Gets the player object for player two

        Returns:
            Player object for player two
        '''
        return self.player_two
    def set_turn_count(self,turn_count: int):
        '''
        Sets the turn number

        Args:
            turn_count: int value for the turn number
        '''
        self.turn_count = turn_count
    def get_turn_count(self) -> int:
        '''
        Gets the turn number as an int

        Returns:
            Turn count as an int
        '''
        return self.turn_count

    def set_board(self, board: Board):
        '''
        Sets the board class the game is played on

        Args:
            
        '''
        self.board = board

    def get_board(self) -> Board:
        return self.board

    def play_turn(self,cell_position: int) -> bool:
        if self.get_board().set_cell_val(cell_position,self.get_active_player().get_symbol()):
            self.get_active_player().set_binary_board(self.get_active_player().get_binary_board()|self.get_board().get_binary(cell_position))
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
        if self.active_player == self.player_one:
            self.set_active_player(self.get_player_two())
        else:
            self.set_active_player(self.get_player_one())

    def get_cell_val(self, cell_num: int) -> str:
        return self.get_board().get_cell(cell_num).get_val()
    
    def check_win(self) -> bool:
        original_binary=self.get_active_player().get_binary_board()
        shift_left=self.get_active_player().get_binary_board() << 1
        shift_right=self.get_active_player().get_binary_board() >> 1
        win_val=original_binary & shift_left & shift_right & 0b010010010010010010010010
        if int(win_val)!=0:
            return True
        else:
            return False
        
    def end_game(self):
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
        self.get_player_one().reset_binary()
        self.get_player_two().reset_binary()
        self.get_board().reset_board()
        self.set_turn_count(0)