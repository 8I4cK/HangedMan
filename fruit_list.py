import random


class FruitList:

    def __init__(self):
        self.__fruits = ['banana', 'jabuticaba', 'pitanga', 'mirtilo', 'morango', 'abacaxi', 'cereja']

    def chose_random_word_from_list(self):
        fruit = self.__fruits
        return random.choice(fruit)

    def hidden_chosen_word(self):
        pass