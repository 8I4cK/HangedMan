# def para pedir o nome do jogador
# def para embaralhar a lista(ver a opção de fzer isso como dicionario)
# def para pedir o input de uma letra
# def para ver se existe um letra na palavra selecionada..
# def para definir o maximo de tenttivas a mais que a maior palavra... +7
import random
class HangManGame:
    def __init__(self):
        self.player_wrong_guess = []
        self.player_correct_guess = []
        self.random_word = []


    def principal_menu(self):
        print('''
═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════ _                                             
                     _
                    | |                                            
                    | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
                    | '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
                    | | | | (_| | | | | (_| | | | | | | (_| | | | |    _
                    |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|   (_)
                                        __/ |                      
                                       |___/          
                                                    
  _______
 |/      |                                             
 |      (_)
 |      \|/
 |       |
 |      / \ »» Rules:
 |
_|___                      
═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════
''')

class Player:
    def __init__(self):
        self.__p_name = ''
        self.__wrong_guessed_letter = []
        self.__correct_guessed_letter = []

    def return_player_name(self):
        self.__p_name = input("Please enter the player's name:\n» ")
        return self.__p_name

    def return_wrong_player_guess(self):
        self.__wrong_guessed_letter = input('Please enter a letter: \n» ')
        return self.__wrong_guessed_letter

    def return_correct_player_guess(self):
        self.__correct_guessed_letter = input('Please enter a letter: \n» ')
        return self.__correct_guessed_letter

import random
class FruitList:

    def __init__(self):
        self.__fruits = ['banana', 'jabuticaba', 'pitanga', 'mirtilo', 'morango', 'abacaxi', 'cereja']


    def chose_random_list(self, fruit):
        for fruit in len(self.__fruits):

        return self.__random_list


class PlayerGuesses:
    def __init__(self):
        pass
        





    def random_word_list(self):
        pass






h = Player()
print(h.return_player_name())
