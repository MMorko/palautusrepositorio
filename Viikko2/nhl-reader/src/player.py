import requests
from rich.console import Console
from rich.table import Table

class PlayerReader:
    def __init__(self, url):
        self.url = url
    
    def get_players(self):
        response = requests.get(self.url)
        response.raise_for_status()
        return response.json()
    
class PlayerStats:
    def __init__(self, players):
        self.players = players.get_players()
        self.console = Console()
    
    def top_scorers_by_nationality(self, nationality):
        players= [player for player in self.players if player['nationality'] == nationality]
        players.sort(key=lambda x: x['goals'] + x['assists'], reverse=True)

        return players
    
    def display_players(self, players):
        table = Table(title="Top Scorers")

        table.add_column("Name", style="cyan")
        table.add_column("Team", style="magenta")
        table.add_column("Goals", style="green")
        table.add_column("Assists", style="green")
        table.add_column("Points", style="green")

        for player in players:
            points = player["goals"] + player["assists"]
            table.add_row(
                player["name"],
                player["team"],
                str(player["goals"]),
                str(player["assists"]),
                str(points),
            )

        self.console.print(table)