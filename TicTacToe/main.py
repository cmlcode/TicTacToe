import os
from controller import Controller

def clear_screen():
    '''Checks the user's system and runs terminal command to clear terminal'''
    os.system('cls' if os.name == 'nt' else 'clear')

def game_loop(controller_obj):
    '''
    Tells the player whose turn it is
    Prints the board
    Asks player where they want to play
    '''
    while controller_obj.get_playing()==True:
        print(f'{controller_obj.get_active_player().get_symbol()}\'s turn')
        print(f'\n{controller_obj.get_board()}')
        ans=int(input("\nWhere would you like to play?\n"))
        controller_obj.play_turn(ans)
        clear_screen()

def show_stats(controller_obj):
    '''
    Tells the players who won
    Shows players' win loss records
    '''
    if controller_obj.get_result()==True:
        print(f'{controller_obj.get_active_player().get_symbol()} WON')
    else:
        print("DRAW")
    print(f'\n{controller_obj.get_board()}')
    print(f'\nSTATS:')
    print('X WIN: {controller_obj.get_player_one().get_record()["win"]}')
    print('O WIN: {controller_obj.get_player_one().get_record()["loss"]}')
    print('DRAW: {controller_obj.get_player_one().get_record()["draw"]}\n')

def main():
    controller_obj = Controller()
    while True:
        ans=input("Start new game? (Y/N)\n").capitalize()
        if ans=='Y':
            clear_screen()
            controller_obj.set_playing(True)
            controller_obj.reset_game()
            game_loop(controller_obj)
            controller_obj.switch_player()
            show_stats(controller_obj)
            controller_obj.switch_player()
        elif ans=='N':   
            break

if __name__ == '__main__':
    main()