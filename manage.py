# https://www.kaggle.com/aljarah/xAPI-Edu-Data
from app import manager
from scripts.load_data import LoadData
from scripts.aggregation import AggregationData
from flask_migrate import MigrateCommand
from flask_script import Server
from os import getenv

manager.add_command('load', LoadData)
manager.add_command('agg', AggregationData)
manager.add_command('db', MigrateCommand)
manager.add_command('runserver', Server(host='0.0.0.0', port=int(getenv('PORT', 5000))))
manager.run()
