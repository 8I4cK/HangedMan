from player import Player

class EnteredLetter:

    def __init__(self):
        self.player = Player()
        self.__chosen_letter = ''
        self.__wrong_guessed_letter = []
        self.__correct_guessed_letter = []



    def get_wrong_players_guess(self):
        return self.__wrong_guessed_letter
    def set_wrong_players_guess(self):
        self.__wrong_guessed_letter.append(self.__chosen_letter)
        return self.__wrong_guessed_letter


    def get_correct_players_guess(self):
        return self.__correct_guessed_letter
    def set_correct_players_guess(self):
        self.__correct_guessed_letter.append(self.__chosen_letter)
        return self.__correct_guessed_letter


    def get_chosen_letter(self):
        return self.__chosen_letter
    def set_chosen_letter(self):
        letter = input(f"{self.player.get_players_name()}, please, choose a random letter:\n» ")
        return letter





