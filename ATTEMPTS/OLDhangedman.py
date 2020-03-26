# def para pedir o nome do jogador
# def para embaralhar a lista(ver a opção de fzer isso como dicionario)
# def para pedir o input de uma letra
# def para ver se existe um letra na palavra selecionada..
# def para definir o maximo de tenttivas a mais que a maior palavra... +5
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
 |                »ENTER YOUR NAME TO START THE GAME
 |                »A WORD WILL BE CHOSEN RANDOMLY. YOU'LL BE ASKED TO ENTER A LETTER
 |                »YOU OWN 5 CHANCES TO GUESS WRONG ♡ ♡ ♡ ♡ ♡
_|___                      
═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════
''')

    def game_logic(self):
        pass





class Player:
    def __init__(self):
        self.__p_name = ''


    def get_players_name(self) -> str:
        return self.__p_name
    def set_players_name(self):
        p_name = str(input("Please enter the player's name:\n» "))
        self.__p_name = p_name


#import Player
class ChosenLetter:

    def __init__(self):
        self.__player = Player()
        self.__chosen_letter = ''
        self.__wrong_guessed_letter = []
        self.__correct_guessed_letter = []
        self.__p_lives = 5


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
        letter = input(f"{self.__player.get_players_name()}, please, choose a random letter:\n» ")
        return letter

    def get_players_lives(self):
        return self.__p_lives
    def lose_a_life(self):
        self.__p_lives -= 1
        print(f"{self.__player.get_players_name()}, you've lost a life!")



import random
class FruitList:

    def __init__(self):
        self.__fruits = ['banana', 'jabuticaba', 'pitanga', 'mirtilo', 'morango', 'abacaxi', 'cereja']

    def chose_random_word_from_list(self):
        fruit = self.__fruits
        return random.choice(fruit)






