from flask import Flask
from flask_migrate import Migrate, MigrateCommand
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager

import settings


app = Flask(__name__)
app.config.from_object('config')
app.config[
    'SQLALCHEMY_DATABASE_URI'
] = 'postgresql://{0}:{1}@{2}/{3}'.format(
    settings.DATABASE['username'],
    settings.DATABASE['password'],
    settings.DATABASE['host'],
    settings.DATABASE['db_name']
)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)


CSRF_ENABLED = True
SECRET_KEY = '123qwe'

if __name__ == '__main__':
    manager.run()

import view, models
