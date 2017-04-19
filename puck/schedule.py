import requests

from datetime import datetime
from pytz import timezone

from puck.constants import SCHEDULE_URL, TEAMS


class Schedule(object):

    def __init__(self, team_id):
        self.team_id = team_id

        self.todays_game = self.get_todays_game()
        self.yesterdays_game = self.get_todays_game()

    def get_todays_game(self):
        today = datetime.now()
        date = today.strftime('%Y-%m-%d')
        url = SCHEDULE_URL.format(self.team_id, date)
        games = requests.get(url).json()
        if len(games['dates']) == 0:
            return False
        games = games['dates'][0]['games']
        if len(games) == 0:
            return False
        game_data = games[0]
        return self.parse_game_data(game_data)

    def get_yesterdays_game(self):
        return {}

    def parse_game_data(self, game_data):
        game = {}
        game['venue'] = game_data['venue']['name']
        game['broadcasts'] = ', '.join([b['name'] for b in game_data['broadcasts']])
        home = game_data['teams']['home']['team']
        away = game_data['teams']['away']['team']
        game['home'] = home['name']
        game['away'] = away['name']
        game['homeAbbrev'] = TEAMS.get(home['id'])['abbreviation']
        game['awayAbbrev'] = TEAMS.get(away['id'])['abbreviation']
        date = datetime.strptime(game_data['gameDate'], '%Y-%m-%dT%H:%M:%SZ')
        utc = timezone('UTC').localize(date)
        date = utc.astimezone(timezone('US/Central'))
        game['puckDrop'] = datetime.strftime(date, "%I:%M %p")
        return game
