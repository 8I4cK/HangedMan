class Player:
    def __init__(self):
        self.__p_name = ''
        self.__p_lives = 5

    def get_players_name(self) -> str:
        return self.__p_name

    def set_players_name(self):
        self.__p_name = input("Please enter the player's name:\n» ").title()

    def get_players_lives(self) -> int:
        return self.__p_lives

    def set_lost_a_life(self):
        self.__p_lives -= 1
        print(f"{self.get_players_name()}, you've lost a life!")

    def show_life(self):
        print("\n"+"♥ " * self.get_players_lives()+"\n")

