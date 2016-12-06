from flask import Blueprint

blueprint = Blueprint('home_controller', __name__, url_prefix='/')


@blueprint.route("/")
def home():
    return "Home"

