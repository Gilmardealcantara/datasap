from flask import Blueprint, render_template

blueprint = Blueprint('home_controller', __name__, url_prefix='/')


@blueprint.route("/")
def home():
    return render_template('home/index.html')


@blueprint.route("tables")
def table():
    return render_template('home/table.html')

@blueprint.route("views")
def views():
    return render_template('home/views.html')

