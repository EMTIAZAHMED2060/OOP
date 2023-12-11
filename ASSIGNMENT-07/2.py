class Tournament:
    def __init__(self,name='Default'):
        self.__name = name
    def set_name(self,name):
        self.__name = name
    def get_name(self):
        return self.__name 
class Cricket_Tournament(Tournament):
    def __init__(self, name='Default', num_teams=0, tournament_type='No type'):
        super().__init__(name)
        self.__num_teams = num_teams
        self.__tournament_type = tournament_type

    def detail(self):
        return f"Cricket Tournament Name: {self.get_name()}\nNumber of Teams: {self.__num_teams}\nType: {self.__tournament_type}"


class Tennis_Tournament(Tournament):
    def __init__(self, name='Default', num_players=0):
        super().__init__(name)
        self.__num_players = num_players

    def detail(self):
        return f"Tennis Tournament Name: {self.get_name()}\nNumber of Players: {self.__num_players}"

ct1 = Cricket_Tournament()
print(ct1.detail())
print("-----------------------")
ct2 = Cricket_Tournament("IPL",10,"t20")
print(ct2.detail())
print("-----------------------")
tt = Tennis_Tournament("Roland Garros",128)
print(tt.detail())

