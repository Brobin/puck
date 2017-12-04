import requests

from datetime import datetime, timedelta
from pytz import timezone

from puck.constants import SCHEDULE_URL, TEAMS


class Schedule(object):

    def __init__(self, team_id, weekly=False):
        self.team_id = team_id

        self.todays_game = self.get_todays_game()
        self.yesterdays_game = self.get_yesterdays_game()

        if weekly:
            self.last_weeks_games = self.get_last_weeks_games()
            self.this_weeks_games = self.get_this_weeks_games()

    def get_todays_game(self):
        today = datetime.now()
        return self.get_game_data(today)

    def get_yesterdays_game(self):
        yesterday = datetime.now() - timedelta(days=1)
        return self.get_game_data(yesterday)

    def get_last_weeks_games(self):
        today = datetime.now()
        games = []
        for days in range(1, 8):
            date = today - timedelta(days)
            game = self.get_game_data(date)
            if game:
                games.append(game)
        return reversed(games)

    def get_this_weeks_games(self):
        today = datetime.now()
        games = []
        for days in range(0, 7):
            date = today + timedelta(days)
            game = self.get_game_data(date)
            if game:
                games.append(game)
        return games

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
        game['homeSubreddit'] = TEAMS.get(home['team']['id'])['subreddit']
        game['awayAbbrev'] = TEAMS.get(away['team']['id'])['abbreviation']
        game['awaySubreddit'] = TEAMS.get(away['team']['id'])['subreddit']
        date = datetime.strptime(game_data['gameDate'], '%Y-%m-%dT%H:%M:%SZ')
        utc = timezone('UTC').localize(date)
        date = utc.astimezone(timezone('US/Central'))
        game['puckDrop'] = date.strftime("%-I:%M %p")
        game['date'] = date.strftime("%a %B %-d, %Y")
        game['linescore'] = game_data['linescore']
        return game
