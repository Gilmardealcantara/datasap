# https://www.kaggle.com/aljarah/xAPI-Edu-Data
from app import manager
from scripts.load_data import LoadData
from scripts.aggregation import AggregationData
from flask_migrate import MigrateCommand


manager.add_command('load', LoadData)
manager.add_command('agg', AggregationData)
manager.add_command('db', MigrateCommand)
manager.run()
