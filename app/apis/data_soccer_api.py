from flask import Blueprint, jsonify
from app.models.sap import SAP
from app import db


blueprint = Blueprint('sap', __name__, url_prefix='/api/sap')

@blueprint.route("/")
def list():
    saps = db.session.query(SAP).all()
    return jsonify(data=[dict(c) for c in saps])

@blueprint.route("/data_tables")
def data_tables():
    saps = db.session.query(SAP).all()
    return jsonify(data=[dict(c).values() for c in saps])
