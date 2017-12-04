import argparse
import jinja2
import os

from datetime import datetime

from puck.constants import TEAMS
from puck.lines import get_lines
from puck.schedule import Schedule
from puck.stats import NHL, Roster

GET_LINES = False


def main(team_id, outfile, season, game_type, weekly):
    context = {}

    context['team'] = TEAMS.get(team_id)
    name = context['team']['name']
    print('Generating report for {0}'.format(name))

    print('Loading {0} schedule'.format(name))
    context['schedule'] = Schedule(team_id, weekly)

    print('Loading {0} Team stats'.format(name))
    context['nhl'] = NHL(season, game_type)

    print('Loading {0} player stats'.format(name))
    context['roster'] = Roster(season, game_type, team_id)

    if team_id == 30 and GET_LINES:
        print('Loading {0} Starting Lines'.format(name))
        context['lines'] = get_lines()

    context['playoffs'] = game_type == 3

    template_name = 'weekly_update.md' if weekly else 'daily_update.md'
    output = jinja2.Environment(
        loader=jinja2.FileSystemLoader('./templates/')
    ).get_template(template_name).render(context)

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
        '--season', type=str, default='20172018',
        help='season for the report, e.g. 20172018'
    )
    parser.add_argument(
        '--weekly', dest='weekly', action='store_true',
        help='Weekly report?'
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
    main(args.team, args.outfile, args.season, game_type, args.weekly)
