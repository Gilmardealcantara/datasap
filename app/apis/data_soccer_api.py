from flask import Blueprint, jsonify
from app.models.country import Country
from app.models.league import League
from app.models.player import Player
from app.models.player_attrs import PlayerAttr
from app.models.sqlite_sequence import SqliteSequence
from app.models.team import Team
from app.models.team_attrs import TeamAttr
from app.models.match import Match

from app import db


blueprint = Blueprint('data_soccer', __name__, url_prefix='/api/data_soccer')

@blueprint.route("/countries")
def country():
    countries = Country.query.all()
    return jsonify(countries=[dict(c) for c in countries])


@blueprint.route("/leagues")
def league():
    leagues = League.query.all()
    return jsonify(leagues=[dict(c) for c in leagues])


@blueprint.route("/players")
def player():
    players = Player.query.all()
    return jsonify(players=[dict(c) for c in players])


@blueprint.route("/players_attrs")
def player_attr():
    players_attr = PlayerAttr.query.all()
    return jsonify(players_attr=[dict(c) for c in players_attr])


@blueprint.route("/sqlite_sequence")
def sqlite_sequence():
    sqlite_sequence = SqliteSequence.query.all()
    return jsonify(sqlite_sequence=[dict(c) for c in sqlite_sequence])


@blueprint.route("/team")
def team():
    teams = Team.query.all()
    return jsonify(teams=[dict(c) for c in teams])

@blueprint.route("/team_attrs")
def team_attr():
    team_attrs = TeamAttr.query.all()
    return jsonify(team_attrs=[dict(c) for c in team_attrs])


@blueprint.route("/match")
def match():
    matchs = Match.query.all()
    return jsonify(matchs=[dict(c) for c in matchs])
