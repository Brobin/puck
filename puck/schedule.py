import requests

from datetime import datetime, timedelta
from pytz import timezone

from puck.constants import SCHEDULE_URL, TEAMS


class Schedule(object):

    def __init__(self, team_id):
        self.team_id = team_id

        self.todays_game = self.get_todays_game()
        self.yesterdays_game = self.get_yesterdays_game()

    def get_todays_game(self):
        today = datetime.now()
        return self.get_game_data(today)

    def get_yesterdays_game(self):
        yesterday = datetime.now() - timedelta(days=1)
        return self.get_game_data(yesterday)

    def get_game_data(self, game_datetime):
        game_date = game_datetime.strftime('%Y-%m-%d')
        url = SCHEDULE_URL.format(self.team_id, game_date)
        games = requests.get(url).json()
        if len(games['dates']) == 0:
            return False
        games = games['dates'][0]['games']
        if len(games) == 0:
            return False
        game_data = games[0]
        game = {}
        game['venue'] = game_data['venue']['name']
        game['broadcasts'] = ', '.join([b['name'] for b in game_data['broadcasts']])
        home = game_data['teams']['home']
        away = game_data['teams']['away']
        game['home'] = home
        game['away'] = away

        game['homeAbbrev'] = TEAMS.get(home['team']['id'])['abbreviation']
        game['awayAbbrev'] = TEAMS.get(away['team']['id'])['abbreviation']
        date = datetime.strptime(game_data['gameDate'], '%Y-%m-%dT%H:%M:%SZ')
        utc = timezone('UTC').localize(date)
        date = utc.astimezone(timezone('US/Central'))
        game['puckDrop'] = date.strftime("%I:%M %p")
        game['linescore'] = game_data['linescore']
        return game
