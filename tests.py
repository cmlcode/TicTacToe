from board import Board
from cell import Cell
from controller import Controller
from player import Player
import pytest

#Board tests

def test_board_init():
    board_obj = Board(9)
    assert board_obj.get_num_cells() == 9
    assert len(board_obj.get_board()) == 9
    for x in range(9):
        assert board_obj.get_board()[x].get_val() == x


def test_board_set_cell_val():
    board_obj = Board(9)
    board_obj.set_cell_val(0,'x')
    board_obj.set_cell_val(1,'x')
    board_obj.set_cell_val(2,'x')

    assert board_obj.get_board()[0].get_val() == 'X'
    assert board_obj.get_board()[1].get_val() == 'X'
    assert board_obj.get_board()[2].get_val() == 'X' 

def test_board_set_cell_val_fail():
    board_obj = Board(9)
    board_obj = Board(9)
    board_obj.set_cell_val(0,'x')
    
    assert board_obj.set_cell_val(0,'y') == False
    assert board_obj.get_board()[0].get_val() == 'X'

#Cell tests

def test_cell_init():
    cell_obj = Cell(0)
    assert cell_obj.get_val() == 0


#Controller tests

def test_controller_init():
    controller_obj = Controller()
    board_obj = Board(9)
    assert controller_obj.get_turn_count() == 0
    assert controller_obj.get_player_one().get_symbol()=='X'
    assert controller_obj.get_player_two().get_symbol() == 'O'
    assert controller_obj.get_active_player() in [controller_obj.get_player_one(), controller_obj.get_player_two()]
    assert type(controller_obj.get_board()) == Board
    for x in range(9):
        assert board_obj.get_board()[x].get_val() == x

def test_controller_switch_no_active():
    controller_obj = Controller()
    player_one = Player('x')
    player_two = Player('o')
    controller_obj.set_player_one(player_one)
    controller_obj.set_player_two(player_two)
    controller_obj.switch_player()
    assert controller_obj.get_active_player() == player_one

def test_controller_switch_one_active():
    controller_obj = Controller()
    player_one = Player('x')
    player_two = Player('o')
    controller_obj.set_player_one(player_one)
    controller_obj.set_player_two(player_two)
    controller_obj.set_active_player(player_one)
    controller_obj.switch_player()
    assert controller_obj.get_active_player() == player_two

def test_controller_switch_two_active():
    controller_obj = Controller()
    player_one = Player('x')
    player_two = Player('o')
    controller_obj.set_player_one(player_one)
    controller_obj.set_player_two(player_two)
    controller_obj.set_active_player(player_two)
    controller_obj.switch_player()

    assert controller_obj.get_active_player() == player_one

def test_controller_play_turn_1():
    controller_obj = Controller()
    controller_obj.set_active_player(controller_obj.get_player_one())
    controller_obj.play_turn(0)

    assert controller_obj.get_active_player() == controller_obj.get_player_two()
    assert controller_obj.get_turn_count() == 1
    assert controller_obj.get_board().get_board()[0].get_val() == 'X'

def test_controller_play_turn_binary():
    controller_obj = Controller()
    controller_obj.set_active_player(controller_obj.get_player_one())
    controller_obj.play_turn(0)
    controller_obj.set_active_player(controller_obj.get_player_one())
    controller_obj.play_turn(1)
    controller_obj.switch_player()
    controller_obj.play_turn(2)

    assert controller_obj.get_active_player() == controller_obj.get_player_two()
    assert controller_obj.get_turn_count() == 3
    assert controller_obj.get_board().get_board()[0].get_val() == 'X'
    assert controller_obj.get_board().get_board()[1].get_val() == 'X'
    assert controller_obj.get_board().get_board()[2].get_val() == 'X'
    assert controller_obj.get_player_one().get_binary_board() == 0b111000000100100100100100

    controller_obj.switch_player()
    assert controller_obj.check_win() == True

def test_controller_play_turn_9():
    controller_obj = Controller()
    controller_obj.set_turn_count(8)
    controller_obj.set_active_player(controller_obj.get_player_two())
    controller_obj.play_turn(0)
    assert controller_obj.get_player_one().get_record()['draw'] == 1
    assert controller_obj.get_player_two().get_record()['draw'] == 1
    assert controller_obj.get_turn_count() == 9
    assert controller_obj.get_board().get_board()[0].get_val() == 'O'
    assert controller_obj.get_active_player() == controller_obj.get_player_two()

def test_controller_check_win_diagnols():
    controller_obj = Controller()
    for x in [0,4,8]:
        controller_obj.set_active_player(controller_obj.get_player_one())
        assert controller_obj.check_win() == False
        controller_obj.play_turn(x)
        
    controller_obj.switch_player()

    assert controller_obj.get_active_player() == controller_obj.get_player_one()
    assert controller_obj.check_win() == True
    controller_obj.set_result(True)
    controller_obj.end_game()
    assert controller_obj.get_cell_val(0) == 'X'
    assert controller_obj.get_cell_val(4) == 'X'
    assert controller_obj.get_cell_val(8) == 'X'
    assert controller_obj.get_player_one().get_record()['win'] == 1
    assert controller_obj.get_player_one().get_record()['loss'] == 0
    assert controller_obj.get_player_one().get_record()['draw'] == 0
    assert controller_obj.get_player_two().get_record()['win'] == 0
    assert controller_obj.get_player_two().get_record()['loss'] == 1
    assert controller_obj.get_player_two().get_record()['draw'] == 0

    controller_obj = Controller()
    for x in [2,4,6]:
        controller_obj.set_active_player(controller_obj.get_player_two())
        assert controller_obj.check_win()==False
        controller_obj.play_turn(x)
    assert controller_obj.get_active_player() == controller_obj.get_player_one()
    assert controller_obj.check_win()==False
    controller_obj.switch_player()

    assert controller_obj.get_active_player() == controller_obj.get_player_two()
    assert controller_obj.check_win() == True
    controller_obj.set_result(True)
    controller_obj.end_game()
    assert controller_obj.get_cell_val(2) == 'O'
    assert controller_obj.get_cell_val(4) == 'O'
    assert controller_obj.get_cell_val(6) == 'O'
    assert controller_obj.get_player_two().get_record()['win'] == 1
    assert controller_obj.get_player_two().get_record()['loss'] == 0
    assert controller_obj.get_player_two().get_record()['draw'] == 0
    assert controller_obj.get_player_one().get_record()['win'] == 0
    assert controller_obj.get_player_one().get_record()['loss'] == 1
    assert controller_obj.get_player_one().get_record()['draw'] == 0

def test_controller_check_win_horizontals():
    controller_obj = Controller()
    for x in [0,1,2]:
        controller_obj.set_active_player(controller_obj.get_player_one())
        assert controller_obj.check_win() == False
        controller_obj.play_turn(x)
        
    controller_obj.switch_player()

    assert controller_obj.get_active_player() == controller_obj.get_player_one()
    assert controller_obj.check_win() == True
    controller_obj.set_result(True)
    controller_obj.end_game()
    assert controller_obj.get_cell_val(0) == 'X'
    assert controller_obj.get_cell_val(1) == 'X'
    assert controller_obj.get_cell_val(2) == 'X'
    assert controller_obj.get_player_one().get_record()['win'] == 1
    assert controller_obj.get_player_one().get_record()['loss'] == 0
    assert controller_obj.get_player_one().get_record()['draw'] == 0
    assert controller_obj.get_player_two().get_record()['win'] == 0
    assert controller_obj.get_player_two().get_record()['loss'] == 1
    assert controller_obj.get_player_two().get_record()['draw'] == 0

    controller_obj = Controller()
    for x in [3,4,5]:
        controller_obj.set_active_player(controller_obj.get_player_two())
        assert controller_obj.check_win()==False
        controller_obj.play_turn(x)
    assert controller_obj.get_active_player() == controller_obj.get_player_one()
    assert controller_obj.check_win()==False
    controller_obj.switch_player()

    assert controller_obj.get_active_player() == controller_obj.get_player_two()
    assert controller_obj.check_win() == True
    controller_obj.set_result(True)
    controller_obj.end_game()
    assert controller_obj.get_cell_val(3) == 'O'
    assert controller_obj.get_cell_val(4) == 'O'
    assert controller_obj.get_cell_val(5) == 'O'
    assert controller_obj.get_player_two().get_record()['win'] == 1
    assert controller_obj.get_player_two().get_record()['loss'] == 0
    assert controller_obj.get_player_two().get_record()['draw'] == 0
    assert controller_obj.get_player_one().get_record()['win'] == 0
    assert controller_obj.get_player_one().get_record()['loss'] == 1
    assert controller_obj.get_player_one().get_record()['draw'] == 0

    controller_obj = Controller()
    for x in [6,7,8]:
        controller_obj.set_active_player(controller_obj.get_player_two())
        assert controller_obj.check_win()==False
        controller_obj.play_turn(x)
    assert controller_obj.get_active_player() == controller_obj.get_player_one()
    assert controller_obj.check_win()==False
    controller_obj.switch_player()

    assert controller_obj.get_active_player() == controller_obj.get_player_two()
    assert controller_obj.check_win() == True
    controller_obj.set_result(True)
    controller_obj.end_game()
    assert controller_obj.get_cell_val(6) == 'O'
    assert controller_obj.get_cell_val(7) == 'O'
    assert controller_obj.get_cell_val(8) == 'O'
    assert controller_obj.get_player_two().get_record()['win'] == 1
    assert controller_obj.get_player_two().get_record()['loss'] == 0
    assert controller_obj.get_player_two().get_record()['draw'] == 0
    assert controller_obj.get_player_one().get_record()['win'] == 0
    assert controller_obj.get_player_one().get_record()['loss'] == 1
    assert controller_obj.get_player_one().get_record()['draw'] == 0

def test_controller_end_game_win_verticals():

    controller_obj = Controller()
    for x in [0,3,6]:
        controller_obj.set_active_player(controller_obj.get_player_one())
        assert controller_obj.check_win() == False
        controller_obj.play_turn(x)
        
    controller_obj.switch_player()

    assert controller_obj.get_active_player() == controller_obj.get_player_one()
    assert controller_obj.check_win() == True
    controller_obj.set_result(True)
    controller_obj.end_game()
    assert controller_obj.get_cell_val(0) == 'X'
    assert controller_obj.get_cell_val(3) == 'X'
    assert controller_obj.get_cell_val(6) == 'X'
    assert controller_obj.get_player_one().get_record()['win'] == 1
    assert controller_obj.get_player_one().get_record()['loss'] == 0
    assert controller_obj.get_player_one().get_record()['draw'] == 0
    assert controller_obj.get_player_two().get_record()['win'] == 0
    assert controller_obj.get_player_two().get_record()['loss'] == 1
    assert controller_obj.get_player_two().get_record()['draw'] == 0

    controller_obj = Controller()
    for x in [1,4,7]:
        controller_obj.set_active_player(controller_obj.get_player_two())
        assert controller_obj.check_win()==False
        controller_obj.play_turn(x)
    assert controller_obj.get_active_player() == controller_obj.get_player_one()
    assert controller_obj.check_win()==False
    controller_obj.switch_player()

    assert controller_obj.get_active_player() == controller_obj.get_player_two()
    assert controller_obj.check_win() == True
    controller_obj.set_result(True)
    controller_obj.end_game()
    assert controller_obj.get_cell_val(1) == 'O'
    assert controller_obj.get_cell_val(4) == 'O'
    assert controller_obj.get_cell_val(7) == 'O'
    assert controller_obj.get_player_two().get_record()['win'] == 1
    assert controller_obj.get_player_two().get_record()['loss'] == 0
    assert controller_obj.get_player_two().get_record()['draw'] == 0
    assert controller_obj.get_player_one().get_record()['win'] == 0
    assert controller_obj.get_player_one().get_record()['loss'] == 1
    assert controller_obj.get_player_one().get_record()['draw'] == 0

    controller_obj = Controller()
    for x in [2,5,8]:
        controller_obj.set_active_player(controller_obj.get_player_two())
        assert controller_obj.check_win()==False
        controller_obj.play_turn(x)
    assert controller_obj.get_active_player() == controller_obj.get_player_one()
    assert controller_obj.check_win()==False
    controller_obj.switch_player()

    assert controller_obj.get_active_player() == controller_obj.get_player_two()
    assert controller_obj.check_win() == True
    controller_obj.set_result(True)
    controller_obj.end_game()
    assert controller_obj.get_cell_val(2) == 'O'
    assert controller_obj.get_cell_val(5) == 'O'
    assert controller_obj.get_cell_val(8) == 'O'
    assert controller_obj.get_player_two().get_record()['win'] == 1
    assert controller_obj.get_player_two().get_record()['loss'] == 0
    assert controller_obj.get_player_two().get_record()['draw'] == 0
    assert controller_obj.get_player_one().get_record()['win'] == 0
    assert controller_obj.get_player_one().get_record()['loss'] == 1
    assert controller_obj.get_player_one().get_record()['draw'] == 0


def test_controller_end_game_tie():
    controller_obj = Controller()
    controller_obj.set_result(False)
    controller_obj.end_game()
    assert controller_obj.get_player_one().get_record()['win'] == 0
    assert controller_obj.get_player_one().get_record()['draw'] == 1
    assert controller_obj.get_player_one().get_record()['loss'] == 0
    assert controller_obj.get_player_two().get_record()['win'] == 0
    assert controller_obj.get_player_two().get_record()['draw'] == 1
    assert controller_obj.get_player_two().get_record()['loss'] == 0

def test_controller_end_game_one_wins():
    controller_obj = Controller()
    controller_obj.set_active_player(controller_obj.get_player_one())
    controller_obj.set_result(True)
    controller_obj.end_game()
    assert controller_obj.get_player_one().get_record()['win'] == 1
    assert controller_obj.get_player_two().get_record()['loss'] == 1

def test_controller_end_game_two_wins():
    controller_obj = Controller()
    controller_obj.set_active_player(controller_obj.get_player_two())
    controller_obj.set_result(True)
    controller_obj.end_game()
    assert controller_obj.get_player_one().get_record()['loss'] == 1
    assert controller_obj.get_player_two().get_record()['win'] == 1

#Player tests

def test_player_init():
    player_obj = Player('x')
    assert player_obj.get_symbol() == 'X'
    assert player_obj.get_record()['win'] == 0
    assert player_obj.get_record()['draw'] == 0
    assert player_obj.get_record()['loss'] == 0

def test_player_add_win():
    player_obj = Player('x')
    player_obj.add_record(1)
    assert player_obj.get_record()['win'] == 1
    assert player_obj.get_record()['draw'] == 0
    assert player_obj.get_record()['loss'] == 0

def test_player_add_draw():
    player_obj = Player('x')
    player_obj.add_record(0)
    assert player_obj.get_record()['win'] == 0
    assert player_obj.get_record()['draw'] == 1
    assert player_obj.get_record()['loss'] == 0

def test_player_add_loss():
    player_obj = Player('x')
    player_obj.add_record(-1)
    assert player_obj.get_record()['win'] == 0
    assert player_obj.get_record()['draw'] == 0
    assert player_obj.get_record()['loss'] == 1