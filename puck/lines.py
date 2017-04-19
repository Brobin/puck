import requests

from bs4 import BeautifulSoup as soup


# Currently only supporting the minnesota Wild. Not really even
# sure if this website is accurate
url = 'http://www2.dailyfaceoff.com/teams/lines/27/minnesota-wild'


def add_table_to_lines(prefix, table, lines):
    for i, tr in enumerate(table.findAll('tr')):
        key = '{0}{1}'.format(prefix, i + 1)
        for td in tr:
            a = td.find('a')
            if a != -1:
                name = a.contents[3]
                last = ' ' .join(name.split(' ')[1:])
                lines[key].append(last)
    return lines


def get_lines():
    lines = {
        'f1': [],
        'f2': [],
        'f3': [],
        'f4': [],
        'd1': [],
        'd2': [],
        'd3': [],
        'g1': [],
    }
    html = requests.get(url).text
    html = soup(html, 'html.parser')

    table = html.find(id='forwards').tbody
    lines = add_table_to_lines('f', table, lines)

    table = html.find(id='defense').tbody
    lines = add_table_to_lines('d', table, lines)

    table = html.find(id='goalie_list').tbody
    lines = add_table_to_lines('g', table, lines)

    return lines
