from player import Player


class Guild:
    def __init__(self, name: str):
        self.name = name
        self.players = []

    def assign_player(self, player: Player):
        if player.guild == "Unaffiliated":
            self.players.append(player)
            player.guild = self.name
            return f"Welcome player {player.name} to the guild {self.name}"
        elif player.guild == self.name:
            return f"Player {player.name} is already in the guild."
        elif player.guild != "Unaffiliated" and player.guild != self.name:
            return f"Player {player.name} is in another guild."

    def kick_player(self, player_name: str):
        for i in range(len(self.players)):
            if self.players[i].name == player_name:
                self.players[i].guild = "Unaffiliated"
                self.players.remove(self.players[i])

                return f"Player {player_name} has been removed from the guild."

        return f"Player {player_name} is not in the guild."

    def guild_info(self):
        players_str = [f"{player.player_info()}" for player in self.players]
        return (
            f"Guild: {self.name} \n" +
            '\n'.join(players_str)
        )
