# def para pedir o nome do jogador
# def para embaralhar a lista(ver a opção de fzer isso como dicionario)
# def para pedir o input de uma letra
# def para ver se existe um letra na palavra selecionada..
# def para definir o maximo de tenttivas a mais que a maior palavra... +5
class HangManGame:
    def __init__(self):
        self.__menu = ''


    def principal_menu(self):
        self.__menu = '''
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
'''
        return print(self.__menu)

