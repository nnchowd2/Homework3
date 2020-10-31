# Name: Nafisa Chowdhury
# PSID: 1591144

class Team:
    def init(self):
        self.team_name = "none"
        self.team_wins = 0
        self.team_losses = 0

    def get_win_percentage(self):
        win_perc = self.team_wins / (self.team_wins + self.team_losses)
        return win_perc


if __name__ == "__main__":
    team = Team()

    team_name = input()
    team_wins = int(input())
    team_losses = int(input())

    team.team_name = team_name
    team.team_wins = team_wins
    team.team_losses = team_losses

    if team.get_win_percentage() >= 0.5:
        print("Congratulations, Team {} has a winning average!".format(team.team_name))
    else:
        print("Team {} has a losing average.".format(team.team_name))
