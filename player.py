class Player:
    def __init__(self):
        self.p_name = ''


    def get_players_name(self) -> str:
        return self.p_name
    def set_players_name(self):
        self.p_name = input("Please enter the player's name:\n» ")
        return self.p_name
