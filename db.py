from app import app
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand
from flask_marshmallow import Marshmallow
from py_yaml_fixtures.flask import PyYAMLFixtures

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost/migrate'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['SQLALCHEMY_ECHO'] = True

app.config['PY_YAML_FIXTURES_DIR'] = 'db/fixtures'

app.config['PY_YAML_FIXTURES_COMMAND_NAME'] = 'import-fixtures'

# Init db
db = SQLAlchemy(app)

# Init ma
ma = Marshmallow(app)

fixtures = PyYAMLFixtures(app)

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db',MigrateCommand)

if __name__ == "__main__":
    manager.run()