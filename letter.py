from player import Player


class EnteredLetter:

    def __init__(self):
        self.player = Player()
        self.__chosen_letter = ''
        self.__wrong_guessed_letter = []
        self.__correct_guessed_letter = []

    def get_wrong_players_guess(self) -> list:
        return self.__wrong_guessed_letter

    def set_wrong_players_guess(self):
        self.__wrong_guessed_letter.append(self.__chosen_letter)
        print(self.get_wrong_players_guess())

    def get_correct_players_guess(self) -> list:
        return self.__correct_guessed_letter

    def set_correct_players_guess(self):
        self.__correct_guessed_letter.append(self.__chosen_letter)

    def get_chosen_letter(self) -> str:
        return self.__chosen_letter

    def set_chosen_letter(self):
        letter = input(f"{self.player.get_players_name()}, please enter your letter:\n» ")
        self.__chosen_letter = letter
