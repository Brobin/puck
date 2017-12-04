# [](##{{team.abbreviation}}TINY) {{ team.name }} Weekly Update!

---

## Last Week's Games

| [](##NHLTINY) Home | [](##NHLTINY) Away | Date | Result | Recap |
|---|---|---|---|---|
{% for g in schedule.last_weeks_games %}| [](##{{ g.homeAbbrev }}TINY) {{ g.homeAbbrev }} | [](##{{ g.awayAbbrev}}TINY) {{ g.awayAbbrev }} | {{ g.date }} {{ g.puckDrop }}| {% if team.abbreviation == g.homeAbbrev and g.home.score > g.away.score %}**W**{% else %}{% if team.abbreviation == g.awayAbbrev and g.away.score > g.home.score %}**W**{% else %}L{% endif %}{% endif %} {{ g.home.score }}-{{ g.away.score }} {% if g.linescore.currentPeriod == 4 %}OT{% elif g.linescore.currentPeriod == 5 %}SO{% endif %}| [Recap Video]()
{% endfor %}

&nbsp;

---

## This Week's Games

| [](##NHLTINY) Home | [](##NHLTINY) Away |  Puck Drop | Venue | Broadcasts |
|---|---|---|---|---|
{% for g in schedule.this_weeks_games %}| [](##{{ g.homeAbbrev}}TINY) {{ g.homeAbbrev }} | [](##{{ g.awayAbbrev}}TINY) {{ g.awayAbbrev }} | {{ g.date }} {{ g.puckDrop }} | {{ g.venue }} | {{ g.broadcasts }}|
{% endfor %}

&nbsp;

---

# [](##{{ team.abbreviation }}TINY)[]({{ team.subreddit }}) {{ team.name }} Skater Stats

| [](##{{ team.abbreviation }}TINY) []({{ team.subreddit }}) | Pos | GP | G | A | P | +/- | B | H | PIM | ATOI | PPG | PPA | S | S% | FOW% | CF% | FF% |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|{% for p in roster.skaters %}
| {{ p.playerName }} | {{ p.playerPositionCode }} | {{ p.gamesPlayed }} | {{ p.goals }} | {{ p.assists }} | {{ p.points }} | {{ p.plusMinus }} | {{ p.blockedShots }} | {{ p.hits }} | {{ p.penaltyMinutes }} | {{ p.atoi }} | {{ p.ppGoals }} | {{ p.ppAssists }} | {{ p.shots }} | {{ '%0.1f'|format(p.shootingPctg*100) }}% | {{ '%0.1f'|format(p.faceoffWinPctg*100) }}% | {{ '%0.1f'|format(p.corsiForPct) }}% | {{ '%0.1f'|format(p.fenwickForPct) }}% |{% endfor %}


# [](##{{ team.abbreviation }}TINY)[]({{ team.subreddit }}) {{ team.name }} Goalie Stats

| [](##{{ team.abbreviation }}TINY)[]({{ team.subreddit }}) | GP | W | L | {% if not playoffs %}OT | {% endif %}SV | SA | SV% | GAA | SO |
|---|---|---|---|{% if not playoffs %}---|{% endif %}---|---|---|---|---|{% for g in roster.goalies %}
| {{ g.playerName }} | {{ g.gamesPlayed }} | {{ g.wins }} | {{ g.losses }} | {% if not playoffs %}{{ g.otLosses }} |{% endif %} {{ g.saves }} | {{ g.shotsAgainst }} | {{ '%0.3f'|format(g.savePctg) }} | {{ '%0.3f'|format(g.goalsAgainstAverage) }} | {{ g.shutouts }} |{% endfor %}

&nbsp;

-----

# [](##NHLTINY) NHL Team Stats

| [](##NHLTINY) | | GP | W | L | {% if not playoffs %}OT | P | ROW | P% |{% endif %} Diff | PP% | PK% | FOW% | CF% |
|---|---|---|---|---|{% if not playoffs %}---|---|---|---|{% endif %}---|---|---|---|---|{% for t in nhl.teams %}
{% include "_team_stat_line.md" %}{% endfor %}

&nbsp;

-----

All stats retrieved from [nhl.com](https://www.nhl.com.stats) and [puckon.net](http://puckon.net)  | Gif highlights courtesy of /u/ChariotOfFire | Made for the State of Hockey by /u/ValarMorHodor
