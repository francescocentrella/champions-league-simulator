
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

