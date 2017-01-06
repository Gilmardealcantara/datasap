# https://www.kaggle.com/aljarah/xAPI-Edu-Data
from app import manager
from scripts.load_data import LoadData
from scripts.aggregation import AggregationData
from flask_migrate import MigrateCommand
import requests

def index(request):
    r = requests.get('http://httpbin.org/status/418')
    print r.text
    return HttpResponse('<pre>' + r.text + '</pre>')

manager.add_command('load', LoadData)
manager.add_command('agg', AggregationData)
manager.add_command('db', MigrateCommand)
manager.run()
