
class Team:
    def __init__(self, name, logo):
        self.name = name
        self.logo = logo
        self.game_played = 0
        self.wins = 0
        self.losses = 0
        self.draws = 0
        self.points = 0
        self.scored = 0
        self.conceded = 0
        self.difference = 0
        self.opponents = []
        self.eliminated = False

    def add_opponent(self, temp):
        self.opponents.append(temp)

    def get_opponent(self):
        return self.opponents

