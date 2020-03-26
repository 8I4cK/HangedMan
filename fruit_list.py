import random

from letter import EnteredLetter


class FruitList:

    def __init__(self):
        self.__fruits = ['banana', 'jabuticaba', 'pitanga', 'mirtilo', 'morango', 'abacaxi', 'cereja']
        self.random_word = ''
        self.entered_letter = EnteredLetter()

    def chose_random_word_from_list(self):
        fruit = self.__fruits
        return random.choice(fruit)

    def get_random_word(self):
        random_word = self.random_word
        return random_word

    def get_hidden_chosen_word(self):
        hidden_word = ''
        for letter in hidden_word:
            if letter in self.entered_letter.get_chosen_letter():
                hidden_word += letter
            else:
                hidden_word += ' - '
        return print(hidden_word)
