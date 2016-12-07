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

@blueprint.route("/graph/1")
def graph1():
    saps = db.session.query(SAP).all()
    data={}

    for row in [dict(c) for c in saps]:
        if data.has_key(row['Topic']) : 
            data[row['Topic']] = [data[row['Topic']][0] + row['Discussion'],  data[row['Topic']][1] + 1 ]
        else:
            data[row['Topic']] = [row['Discussion'], 1]

    data2 = []
    for topic in data:
        data2 += [{'topic' : topic, 'discussion' :  data[topic][0] / data[topic][1]}]
        

    return jsonify(data=data2)
