{% if schedule.todays_game %}{% set g=schedule.todays_game %}
# [](##{{ g.homeAbbrev }}90) {{ g.home }} vs. {{ g.away }} [](##{{ g.awayAbbrev }}90)

## **Puck Drop**: {{ g.puckDrop }}
## **Venue**: {{ g.venue }}
## **Broadcasts**: {{ g.broadcasts }}

-----
{% endif %}

# [](##{{ team.abbreviation }}TINY) {{ team.name }} Skater Stats

| [](##{{ team.abbreviation }}TINY) | Pos | GP | G | A | P | +/- | B | H | PIM | ATOI | PPG | PPA | S% | FOW% |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|{% for p in roster.skaters %}
| {{ p.playerName }} | {{ p.playerPositionCode }} | {{ p.gamesPlayed }} | {{ p.goals }} | {{ p.assists }} | {{ p.points }} | {{ p.plusMinus }} | {{ p.blockedShots }} | {{ p.hits }} | {{ p.penaltyMinutes }} | {{ p.atoi }} | {{ p.ppGoals }} | {{ p.ppAssists }} | {{ '%0.1f'|format(p.shootingPctg*100) }}% | {{ '%0.1f'|format(p.faceoffWinPctg*100) }}% |{% endfor %}


# [](##{{ team.abbreviation }}TINY) {{ team.name }} Goalie Stats

| [](##{{ team.abbreviation }}TINY) | GP | W | L | {% if not playoffs %}OT |{% endif %} SV% | GAA | SO |
|---|---|---|---|{% if not playoffs %}---|{% endif %}---|---|---|{% for g in roster.goalies %}
| {{ g.playerName }} | {{ g.gamesPlayed }} | {{ g.wins }} | {{ g.losses }} | {% if not playoffs %}{{ g.otLosses }} |{% endif %} {{ '%0.3f'|format(g.savePctg) }} | {{ '%0.3f'|format(g.goalsAgainstAverage) }} | {{ g.shutouts }} |{% endfor %}

&nbsp;

-----


# [](##NHLTINY) NHL Team Stats

| [](##NHLTINY) | GP | W | L | {% if not playoffs %}OT | P | ROW | P% |{% endif %} Diff | PP% | PK% | FOW% |
|---|---|---|---|{% if not playoffs %}---|---|---|---|{% endif %}---|---|---|---|{% for t in nhl.teams %}
| [](##{{ t.teamAbbrev }}TINY) {{ t.teamFullName }} | {{ t.gamesPlayed|int }} | {{ t.wins|int }} | {{ t.losses|int }} |{% if not playoffs %} {{ t.otLosses|int }} | {{ t.points|int }} | {{ t.regPlusOtWins|int }} | {{ '%0.3f'|format(t.pointPctg) }} |{% endif %} {{ t.diff|int }} | {{ '%0.1f'|format(t.ppPctg*100) }} | {{ '%0.1f'|format(t.pkPctg*100) }} | {{ '%0.1f'|format(t.faceoffWinPctg*100) }} |{% endfor %}

&nbsp;

-----

All stats retrieved from [nhl.com](https://www.nhl.com.stats) and [puckon.net](http://puckon.net)  | Gif highlights courtesy of /u/ChariotOfFire | Made for the State of Hockey by /u/ValarMorHodor