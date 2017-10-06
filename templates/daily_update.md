{% if schedule.todays_game %}{% set g=schedule.todays_game %}
# [](##{{ g.homeAbbrev }}90)[](##{{ g.homeSubreddit }}) {{ g.home.team.name }} vs. {{ g.away.team.name }} [](##{{ g.awayAbbrev }}90)[]({{ g.awaySubreddit }})

## **Puck Drop**: {{ g.puckDrop }}
## **Venue**: {{ g.venue }}
## **Broadcasts**: {{ g.broadcasts }}

{% if lines %}Projected Lines

| [](##MINTINY) | LW | C | RW | [](##MINTINY) | D | D | [](##MINTINY) | Goalie |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **1** | {{ lines.f1.0 }} | {{ lines.f1.1 }} | {{ lines.f1.2 }}  | **1** | {{ lines.d1.0 }} | {{ lines.d1.1 }} | **Start** | {{ lines.g1.0 }} |
| **2** | {{ lines.f2.0 }} | {{ lines.f2.1 }} | {{ lines.f2.2 }}  | **2** | {{ lines.d2.0 }} | {{ lines.d2.1 }} | **Backup** | {{ lines.g1.1 }} |
| **3** | {{ lines.f3.0 }} | {{ lines.f3.1 }} | {{ lines.f3.2 }}  | **3** | {{ lines.d3.0 }} | {{ lines.d3.1 }} | | |
| **4** | {{ lines.f4.0 }} | {{ lines.f4.1 }} | {{ lines.f4.2 }}  | | | |  | |{% endif %}

-----
{% endif %}{% if schedule.yesterdays_game %}{% set g=schedule.yesterdays_game %}
# Yesterday's Game

## [](##{{ g.homeAbbrev }}TINY)[]({{ g.homeSubreddit }}) {{ g.home.team.name }} vs. {{ g.away.team.name }} [](##{{ g.awayAbbrev }}TINY)[]({{ g.awaySubreddit }})

{% set p=g.linescore.currentPeriod %}{% set score=g.linescore.periods %}
| [](##NHLTINY) | 1 | 2 | 3 {% if p >= 4 %}| OT{% endif %} {% if p >= 5 %}| SO{% endif %} | F |
|---|---|---|---{% if p >= 4 %}|---{% endif %}{% if p >= 4 %}|---{% endif %}|---|
| [](##{{ g.homeAbbrev }}TINY)[]({{ g.homeSubreddit }}) {{ g.home.team.name }} |  {{ score.0.home.goals }} |  {{ score.1.home.goals }} |  {{ score.2.home.goals }} {% if score|length >= 4 %}| {{ score.3.home.goals }} {% endif %}{% if score|length >= 5 %}|  {{ score.4.home.goals }} {% endif %}| {{ g.home.score }} |
| [](##{{ g.awayAbbrev }}TINY)[]({{ g.awaySubreddit }}) {{ g.away.team.name }} |  {{ score.0.away.goals }} |  {{ score.1.away.goals }} |  {{ score.2.away.goals }} {% if score|length >= 4 %}| {{ score.3.away.goals }} {% endif %}{% if score|length >= 5 %}|  {{ score.4.away.goals }} {% endif %}| {{ g.away.score }} |

&nbsp;

| Period | [](##{{ team.abbreviation }}TINY)[]({{ team.subreddit }}) | |
|---|---|---|

-----
{% endif %}

# [](##{{ team.abbreviation }}TINY)[]({{ team.subreddit }}) {{ team.name }} Skater Stats

| [](##{{ team.abbreviation }}TINY) []({{ team.subreddit }}) | Pos | GP | G | A | P | +/- | B | H | PIM | ATOI | PPG | PPA | S | S% | FOW% | CF% | FF% |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|{% for p in roster.skaters %}
| {{ p.playerName }} | {{ p.playerPositionCode }} | {{ p.gamesPlayed }} | {{ p.goals }} | {{ p.assists }} | {{ p.points }} | {{ p.plusMinus }} | {{ p.blockedShots }} | {{ p.hits }} | {{ p.penaltyMinutes }} | {{ p.atoi }} | {{ p.ppGoals }} | {{ p.ppAssists }} | {{ p.shots }} | {{ '%0.1f'|format(p.shootingPctg*100) }}% | {{ '%0.1f'|format(p.faceoffWinPctg*100) }}% | {{ '%0.1f'|format(p.corsiForPct) }}% | {{ '%0.1f'|format(p.fenwickForPct) }}% |{% endfor %}


# [](##{{ team.abbreviation }}TINY)[]({{ team.subreddit }}) {{ team.name }} Goalie Stats

| [](##{{ team.abbreviation }}TINY)[]({{ team.subreddit }}) | GP | W | L | {% if not playoffs %}OT |{% endif %} SV% | GAA | SO |
|---|---|---|---|{% if not playoffs %}---|{% endif %}---|---|---|{% for g in roster.goalies %}
| {{ g.playerName }} | {{ g.gamesPlayed }} | {{ g.wins }} | {{ g.losses }} | {% if not playoffs %}{{ g.otLosses }} |{% endif %} {{ '%0.3f'|format(g.savePctg) }} | {{ '%0.3f'|format(g.goalsAgainstAverage) }} | {{ g.shutouts }} |{% endfor %}

&nbsp;

-----


# [](##NHLTINY) NHL Team Stats

| [](##NHLTINY) | | GP | W | L | {% if not playoffs %}OT | P | ROW | P% |{% endif %} Diff | PP% | PK% | FOW% |
|---|---|---|---|---|{% if not playoffs %}---|---|---|---|{% endif %}---|---|---|---|{% for t in nhl.teams %}
| [](##{{ t.teamAbbrev }}TINY)[]({{ t.subreddit }}) | {{ t.teamFullName }} | {{ t.gamesPlayed|int }} | {{ t.wins|int }} | {{ t.losses|int }} |{% if not playoffs %} {{ t.otLosses|int }} | {{ t.points|int }} | {{ t.regPlusOtWins|int }} | {{ '%0.3f'|format(t.pointPctg) }} |{% endif %} {{ t.diff|int }} | {{ '%0.1f'|format(t.ppPctg*100) }} | {{ '%0.1f'|format(t.pkPctg*100) }} | {{ '%0.1f'|format(t.faceoffWinPctg*100) }} |{% endfor %}

&nbsp;

-----

All stats retrieved from [nhl.com](https://www.nhl.com.stats) and [puckon.net](http://puckon.net)  | Gif highlights courtesy of /u/ChariotOfFire | Made for the State of Hockey by /u/ValarMorHodor
