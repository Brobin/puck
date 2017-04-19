import requests

from puck.constants import (
    GOALIE_URL,
    SKATER_URL,
    SKATER_EXTRA_URL,
    TEAMS_URL,
    TEAM_TRANSLATION,
)


class NHL(object):
    """NHL model

    Creates a list of teams represented as a dictionary
    with all relevant stats. Also appends a league average
    and league leader pseudo-team
    """

    def __init__(self, season, game_type):
        self.season = season
        self.game_type = game_type
        # Load all of the data and compute league avg and leader
        self.teams = self.retrieve_data()
        if game_type != 3:  # if we're not in the playoffs
            self.leader = self.get_league_leaders()
            self.average = self.get_league_average()
            # Add leader and avg to league and sort
            self.teams.append(self.leader)
            self.teams.append(self.average)

        for team in self.teams:
            # add diff
            team['diff'] = team['goalsFor'] - team['goalsAgainst']
            # Translate the team abbreviations
            if team['teamAbbrev'] in TEAM_TRANSLATION.keys():
                team['teamAbbrev'] = TEAM_TRANSLATION[team['teamAbbrev']]

        # Sort teams by points
        self.teams.sort(key=lambda x: x['points'], reverse=True)

    def retrieve_data(self):
        # pull the stats from the API
        url = TEAMS_URL.format(self.season, self.game_type)
        data = requests.get(url).json()['data']
        return data

    def keys(self):
        # Get the keys, or stats that we're tracking
        return [
            t for t in self.teams[0].keys()
            if not isinstance(self.teams[0][t], str)
        ]

    def get_league_leaders(self):
        # Get the league leader in every stat
        leader = {}
        for key in self.keys():
            reverse = key not in ['losses']
            team_stats = sorted([t[key] for t in self.teams], reverse=reverse)
            leader[key] = team_stats[0]
        leader['teamAbbrev'] = 'NHL'
        leader['teamFullName'] = '**NHL Leader**'
        return leader

    def get_league_average(self):
        # Get the league average for every stat
        average = {}
        for key in self.keys():
            team_stats = [t[key] for t in self.teams]
            average[key] = sum(team_stats) / len(team_stats)
        average['teamAbbrev'] = 'NHL'
        average['teamFullName'] = '**NHL Average**'
        return average


class Roster(object):

    def __init__(self, season, game_type, team_id):
        self.season = season
        self.game_type = game_type
        self.team_id = team_id
        self.skaters = self.get_skaters()
        self.skaters.sort(key=lambda x: x['points'], reverse=True)
        self.goalies = self.get_goalies()
        self.goalies.sort(key=lambda x: x['wins'], reverse=True)

    def get_skaters(self):
        url = SKATER_URL.format(self.season, self.game_type, self.team_id)
        extra_url = SKATER_EXTRA_URL.format(self.season, self.game_type, self.team_id)
        data = requests.get(url).json()['data']
        extra_data = requests.get(extra_url).json()['data']

        # combine the data from both enpoints into a dict of players
        players = {p['playerName']: p for p in data}
        for x in extra_data:
            players[x['playerName']].update(x)

        # turn our player dict back into a list
        data = [player for key, player in players.items()]

        # calculate supplementay stats
        for player in data:
            player['ppAssists'] = player['ppPoints'] - player['ppGoals']
            player['atoi'] = self.average_time_on_ice(player)
        return data

    def average_time_on_ice(self, player):
        total = player['timeOnIcePerGame']
        seconds = total % 60
        minutes = (total - seconds) / 60
        return '{0:02d}:{1:02d}'.format(int(minutes), int(seconds))

    def get_goalies(self):
        url = GOALIE_URL.format(self.season, self.game_type, self.team_id)
        data = requests.get(url).json()['data']
        return data
