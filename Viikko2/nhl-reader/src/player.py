import requests

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
    
    def top_scorers_by_nationality(self, nationality):
        players= []
        for dict in self.players:
            if dict['nationality'] == nationality:
                players.append(dict)
        players.sort(key=lambda x: x['goals'] + x['assists'], reverse=True)
        
        return players