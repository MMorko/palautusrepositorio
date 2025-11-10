from player import PlayerStats, PlayerReader

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2024-25/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    players = stats.top_scorers_by_nationality("FIN")

    stats.display_players(players)


if __name__ == "__main__":
    main()
