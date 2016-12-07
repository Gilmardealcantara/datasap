from flask import Blueprint, jsonify
from app.models.sap import SAP


from app import db


blueprint = Blueprint('sap', __name__, url_prefix='/api/data_soccer')

@blueprint.route("/")
def country():
    saps = SAP.query.all()
    return jsonify(saps=[dict(c) for c in saps])


