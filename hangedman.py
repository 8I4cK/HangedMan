# def para pedir o nome do jogador
# def para embaralhar a lista(ver a opção de fzer isso como dicionario)
# def para pedir o input de uma letra
# def para ver se existe um letra na palavra selecionada..
# def para definir o maximo de tenttivas a mais que a maior palavra... +7
import random
class HangManGame:
    def __init__(self):
        pass


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

    def return_players_name(self):
        self.__p_name = input("Please enter the player's name:\n» ")
        return self.__p_name

    def return_wrong_players_guess(self):
        self.__wrong_guessed_letter = input(f"{self.__p_name}, you've guessed the wrong letter, "
                                            f"please enter a new letter: \n» ")
        return self.__wrong_guessed_letter

    def return_correct_players_guess(self):
        self.__correct_guessed_letter = input(f'{self.__p_name}, please enter a letter: \n» ')
        return self.__correct_guessed_letter


import random
class FruitList:

    def __init__(self):
        self.__fruits = ['banana', 'jabuticaba', 'pitanga', 'mirtilo', 'morango', 'abacaxi', 'cereja']


    def chose_random_word_from_list(self):
        fruit = self.__fruits
        return random.choice(fruit)








h = FruitList()
print(h.chose_random_word_from_list())
