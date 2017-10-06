TEAMS_URL = 'http://www.nhl.com/stats/rest/grouped/team/basic/season/teamsummary?cayenneExp=seasonId={0} and gameTypeId={1}'  # NOQA
SKATER_URL = 'http://www.nhl.com/stats/rest/grouped/skaters/basic/season/skatersummary?cayenneExp=seasonId={0} and gameTypeId={1} and teamId={2}'  # NOQA
SKATER_EXTRA_URL = 'http://www.nhl.com/stats/rest/grouped/skaters/basic/season/realtime?cayenneExp=seasonId={0} and gameTypeId={1} and teamId={2}'  # NOQA
SKATER_SHOOTING_URL = 'http://www.nhl.com/stats/rest/grouped/skaters/shooting/season/skatersummaryshooting?cayenneExp=seasonId={0} and gameTypeId={1} and teamId={2}'  # NOQA
GOALIE_URL = 'http://www.nhl.com/stats/rest/grouped/goalies/goalie_basic/season/goaliesummary?cayenneExp=seasonId={0} and gameTypeId={1} and playerPositionCode="G" and teamId={2}'  # NOQA
SCHEDULE_URL = 'https://statsapi.web.nhl.com/api/v1/schedule?expand=schedule.broadcasts.all,schedule.linescore&teamId={0}&startDate={1}&endDate={1}'  # NOQA

TEAM_TRANSLATION = {
    'LAK': 'LA',
    'NJD': 'NJ',
    'SJS': 'SJ',
    'TBL': 'TB',
}

TEAMS = {
    1: {
        'abbreviation': 'NJ',
        'name': 'New Jersey Devils',
        'subreddit': '/r/devils'
    },
    2: {
        'abbreviation': 'NYI',
        'name': 'New York Islanders',
        'subreddit': '/r/newyorkislanders'
    },
    3: {
        'abbreviation': 'NYR',
        'name': 'New York Rangers',
        'subreddit': '/r/rangers'
    },
    4: {
        'abbreviation': 'PHI',
        'name': 'Philadelphia Flyers',
        'subreddit': '/r/flyers'
    },
    5: {
        'abbreviation': 'PIT',
        'name': 'Pittsburgh Penguins',
        'subreddit': '/r/penguins'
    },
    6: {
        'abbreviation': 'BOS',
        'name': 'Boston Bruins',
        'subreddit': '/r/bostonbruins'
    },
    7: {
        'abbreviation': 'BUF',
        'name': 'Buffalo Sabres',
        'subreddit': '/r/sabres'
    },
    8: {
        'abbreviation': 'MTL',
        'name': 'Montreal Canadiens',
        'subreddit': '/r/habs'
    },
    9: {
        'abbreviation': 'OTT',
        'name': 'Ottawa Senators',
        'subreddit': '/r/ottawasenators'
    },
    10: {
        'abbreviation': 'TOR',
        'name': 'Toronto Maple Leafs',
        'subreddit': '/r/leafs'
    },
    12: {
        'abbreviation': 'CAR',
        'name': 'Carolina Hurricanes',
        'subreddit': '/r/canes'
    },
    13: {
        'abbreviation': 'FLA',
        'name': 'Florida Panthers',
        'subreddit': '/r/floridapanthers'
    },
    14: {
        'abbreviation': 'TB',
        'name': 'Tampa Bay Lightning',
        'subreddit': '/r/tampabaylightning'
    },
    15: {
        'abbreviation': 'WSH',
        'name': 'Washington Capitals',
        'subreddit': '/r/caps'
    },
    16: {
        'abbreviation': 'CHI',
        'name': 'Chicago Blackhawks',
        'subreddit': '/r/hawks'
    },
    17: {
        'abbreviation': 'DET',
        'name': 'Detroit Red Wings',
        'subreddit': '/r/detroitredwings'
    },
    18: {
        'abbreviation': 'NSH',
        'name': 'Nashville Predators',
        'subreddit': '/r/predators'
    },
    19: {
        'abbreviation': 'STL',
        'name': 'St. Louis Blues',
        'subreddit': '/r/stlouisblues'
    },
    20: {
        'abbreviation': 'CGY',
        'name': 'Calgary Flames',
        'subreddit': '/r/calgaryflames'
    },
    21: {
        'abbreviation': 'COL',
        'name': 'Colorado Avalanche',
        'subreddit': '/r/coloradoavalanche'
    },
    22: {
        'abbreviation': 'EDM',
        'name': 'Edmonton Oilers',
        'subreddit': '/r/edmontonoilers'
    },
    23: {
        'abbreviation': 'VAN',
        'name': 'Vancover Canucks',
        'subreddit': '/r/canucks'
    },
    24: {
        'abbreviation': 'ANA',
        'name': 'Anaheim Ducks',
        'subreddit': '/r/anaheimducks'
    },
    25: {
        'abbreviation': 'DAL',
        'name': 'Dallas Stars',
        'subreddit': '/r/dallasstars'
    },
    26: {
        'abbreviation': 'LA',
        'name': 'Los Angeles Kings',
        'subreddit': '/r/losangeleskings'
    },
    28: {
        'abbreviation': 'SJ',
        'name': 'San Jose Sharks',
        'subreddit': '/r/sanjosesharks'
    },
    29: {
        'abbreviation': 'CBJ',
        'name': 'Columbus Blue Jackets',
        'subreddit': '/r/bluejackets'
    },
    30: {
        'abbreviation': 'MIN',
        'name': 'Minnesota Wild',
        'subreddit': '/r/wildhockey'
    },
    52: {
        'abbreviation': 'WPG',
        'name': 'Winnipeg Jets',
        'subreddit': '/r/winnipegjets'
    },
    53: {
        'abbreviation': 'ARI',
        'name': 'Arizona Coyotes',
        'subreddit': '/r/coyotes'
    },
    54: {
        'abbreviation': 'VGK',
        'name': 'Vegas Golden Knights',
        'subreddit': '/r/goldenknights'
    }
}
