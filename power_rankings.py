import requests
from datetime import date, timedelta


TEAMS_URL = 'http://www.nhl.com/stats/rest/team?isAggregate=false&reportType=basic&isGame=false&reportName=teamsummary&cayenneExp=seasonId={0} and gameTypeId={1}'  # NOQA
URL = 'http://www.nhl.com/stats/rest/team?isAggregate=false&reportType=basic&isGame=true&reportName=teamsummary&cayenneExp=gameDate>="{0}" and gameDate<="{1}" and gameTypeId="2" and teamId={2}' # NOQA

TEAMS = {
    1: 'NJD',
    2: 'NYI',
    3: 'NYR',
    4: 'PHI',
    5: 'PIT',
    6: 'BOS',
    7: 'BUF',
    8: 'MTL',
    9: 'OTT',
    10: 'TOR',
    12: 'CAR',
    13: 'FLA',
    14: 'TBL',
    15: 'WSH',
    16: 'CHI',
    17: 'DET',
    18: 'NSH',
    19: 'STL',
    20: 'CGY',
    21: 'COL',
    22: 'EDM',
    23: 'VAN',
    24: 'ANA',
    25: 'DAL',
    26: 'LAK',
    28: 'SJS',
    29: 'CBJ',
    30: 'MIN',
    52: 'WPG',
    53: 'ARI',
    54: 'VGK',
}


class NHLPowerRankings(object):

    def __init__(self):
        today = date.today()
        idx = (today.weekday() + 1) % 7
        saturday = today - timedelta(idx - 6)
        self.sunday = '2017-10-04'
        self.saturday = saturday.strftime('%Y-%m-%d')
        self.teams = self.get_teams()

    def get_teams(self):
        teams = {}
        url = TEAMS_URL.format('20172018', '2')
        data = requests.get(url).json()['data']
        for team in data:
            teams[team['teamAbbrev']] = team
        for id, abbrev in TEAMS.items():
            teams[abbrev]['id'] = id
        return teams

    def calculate_rankings(self):
        for abbrev, team in self.teams.items():
            url = URL.format(self.sunday, self.saturday, team['id'])
            data = requests.get(url).json()['data']
            # W, L, OT
            team['rp1'] = 0  # 1, -1, 0
            team['rp2'] = 0  # 2, -1, 0
            team['rp3'] = 0  # 1, -1, -0.5
            team['rp4'] = 0  # 1, -1, -1
            team['weekWin'], team['weekLoss'], team['weekOt'] = 0, 0, 0
            for game in data:
                opp_pctg = self.teams[game['opponentTeamAbbrev']]['pointPctg']
                if game['points'] == 2:
                    team['weekWin'] += 1
                    team['rp1'] += opp_pctg
                    team['rp2'] += opp_pctg * 2
                    team['rp3'] += opp_pctg
                    team['rp4'] += opp_pctg * 2
                elif game['points'] == 0:
                    team['weekLoss'] += 1
                    team['rp1'] -= opp_pctg
                    team['rp2'] -= opp_pctg
                    team['rp3'] -= opp_pctg
                    team['rp4'] -= opp_pctg
                elif game['points'] == 1:
                    team['weekOt'] += 1
                    team['rp3'] -= opp_pctg / 2
                    team['rp4'] -= opp_pctg

            team['rp'] = (team['rp1'] + team['rp2'] + team['rp3'] + team['rp4']) / 4.0

            if len(data):
                team['rp'] = team['rp'] / len(data)
                team['rp1'] = team['rp1'] / len(data)
                team['rp2'] = team['rp2'] / len(data)
                team['rp3'] = team['rp3'] / len(data)
                team['rp4'] = team['rp4'] / len(data)
        return self.assign_rankings()

    def assign_rankings(self):
        teams = [team for key, team in self.teams.items()]
        teams.sort(key=lambda x: x['pointPctg'], reverse=True)
        teams.sort(key=lambda x: x['rp1'], reverse=True)

        for i, team in enumerate(teams):
            team['rp1'] = i +1
        teams.sort(key=lambda x: x['rp2'], reverse=True)
        for i, team in enumerate(teams):
            team['rp2'] = i +1
        teams.sort(key=lambda x: x['rp3'], reverse=True)
        for i, team in enumerate(teams):
            team['rp3'] = i +1
        teams.sort(key=lambda x: x['rp4'], reverse=True)
        for i, team in enumerate(teams):
            team['rp4'] = i +1
        teams.sort(key=lambda x: x['rp'], reverse=True)
        for i, team in enumerate(teams):
            team['rp'] = i +1
        return self.print_rankings(teams)


    def print_rankings(self, teams):
        print('team, W -L, 2W -L, W -L -.5OT, W -L -OT, AVG, P%, Record')
        for team in teams:
            print(
                '{0}, {1}, {2}, {3}, {4}, {5}, {6:.3f}, {7}'.format(
                    team['teamAbbrev'],
                    team['rp1'],
                    team['rp2'],
                    team['rp3'],
                    team['rp4'],
                    team['rp'],
                    team['pointPctg'],
                    '({0}-{1}-{2})'.format(team['weekWin'], team['weekLoss'], team['weekOt'])
                )
            )



nhl = NHLPowerRankings()

nhl.calculate_rankings()
