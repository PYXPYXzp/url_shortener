from flask import Flask
from flask_migrate import Migrate, MigrateCommand
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager


app = Flask(__name__)
app.config.from_object('config')
app.config[
    'SQLALCHEMY_DATABASE_URI'
# ] = 'postgresql://root:root@172.17.0.3/postgres'
] = 'postgresql://docker:docker@172.17.0.3/url_postgres'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)


CSRF_ENABLED = True
SECRET_KEY = '123qwe'

if __name__ == '__main__':
    manager.run()

import view, models
