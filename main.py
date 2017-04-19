import argparse
import jinja2
import os

from datetime import datetime

from puck.constants import TEAMS
from puck.schedule import Schedule
from puck.stats import NHL, Roster


def main(team_id, outfile, season, game_type):
    team = TEAMS.get(team_id)
    name = team['name']
    print('Generating report for {0}'.format(name))

    print('Loading {0} schedule'.format(name))
    schedule = Schedule(team_id)

    print('Loading {0} Team stats'.format(name))
    nhl = NHL(season, game_type)

    print('Loading {0} player stats'.format(name))
    roster = Roster(season, game_type, team_id)
    context = {
        'nhl': nhl,
        'roster': roster,
        'playoffs': game_type == 3,
        'schedule': schedule,
        'team': team,
    }
    output = jinja2.Environment(
        loader=jinja2.FileSystemLoader('./templates/')
    ).get_template('daily_update.md').render(context)
    filename = os.path.join('.output', outfile)
    with open(filename, 'w+') as _out:
        _out.write(output)
    print(filename)
    print('Completed!')


if __name__ == '__main__':
    date = datetime.now().date()
    default_name = '{0}-update-test.md'.format(date)

    parser = argparse.ArgumentParser(
        description='Generate a daily update report for your NHL team'
    )
    parser.add_argument(
        '--team', type=int, default='30',
        help='team id for the report, defaults to Wild'
    )
    parser.add_argument(
        '--season', type=str, default='20162017',
        help='season for the report, e.g. 20162017'
    )
    parser.add_argument(
        '--playoffs', dest='playoffs', action='store_true',
        help='Is it the playoffs?'
    )
    parser.add_argument(
        '--outfile', type=str, default=default_name,
        help='name of the output file'
    )
    args = parser.parse_args()
    game_type = 3 if args.playoffs else 2
    main(args.team, args.outfile, args.season, game_type)
