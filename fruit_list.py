import random

from letter import EnteredLetter


class FruitList:

    def __init__(self):
        self.__fruits = ['banana', 'jabuticaba', 'pitanga', 'mirtilo', 'morango', 'abacaxi', 'cereja']
        self.random_word = ''
        self.ended_word = False
        self.entered_letter = EnteredLetter()

    def chose_random_word_from_list(self):
        fruit = self.__fruits
        self.random_word = random.choice(fruit)

    def get_random_word(self) -> str:
        random_word = self.random_word
        return random_word

    def show_hidden_chosen_word(self):
        hidden_word = ''
        for letter in self.random_word:
            if letter in self.entered_letter.get_correct_players_guess():
                hidden_word += letter
            else:
                hidden_word += ' _ '
        if '_' not in hidden_word:
            self.ended_word = True
        print(hidden_word)
