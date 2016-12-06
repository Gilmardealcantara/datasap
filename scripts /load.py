from os import getenv, listdir, getcwd, path
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from app import db as dbPg;