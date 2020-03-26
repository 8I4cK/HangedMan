from hangedman import HangManGame
from player import Player
from letter import ChosenLetter
from fruit_list import FruitList

class GameLogic:
    def __init__(self):
        self.__hanged_man = HangManGame()
        self.__player = Player()
        self.__fruit_list = FruitList()
        self.__player_letter = ChosenLetter()


    def run_the_game(self):
        self.__hanged_man.principal_menu()
        self.__player.set_players_name()
        self.__player_letter.player = self.__player
        self.__player_letter.set_chosen_letter()




g = GameLogic()
g.run_the_game()
