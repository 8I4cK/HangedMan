from hangedman import HangManGame
from player import Player
from letter import EnteredLetter
from fruit_list import FruitList


class GameLogic:
    def __init__(self):
        self.__hanged_man = HangManGame()
        self.__player = Player()
        self.__player_letter = EnteredLetter()
        self.__fruit_list = FruitList()

    def run_the_game(self):
        self.__hanged_man.principal_menu()
        self.__hanged_man.player = self.__player
        self.__player.set_players_name()
        self.__player_letter.player = self.__player
        self.__fruit_list.entered_letter = self.__player_letter
        self.__hanged_man.fruit_list = self.__fruit_list
        self.__fruit_list.chose_random_word_from_list()
        self.__fruit_list.show_hidden_chosen_word()
        while self.__player.get_players_lives() > 0 and not self.__fruit_list.ended_word:
            self.__player.show_life()
            self.__player_letter.set_chosen_letter()
            if self.__player_letter.get_chosen_letter() in self.__fruit_list.random_word:
                self.__player_letter.set_correct_players_guess()
            else:
                self.__player_letter.set_wrong_players_guess()
                self.__player.set_lost_a_life()
            self.__fruit_list.show_hidden_chosen_word()
        if self.__player.get_players_lives() == 0:
            self.__hanged_man.get_lost_game()
        else:
            self.__hanged_man.get_won_game()






g = GameLogic()
g.run_the_game()
