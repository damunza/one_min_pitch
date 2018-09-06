from app import create_app, db
from app.models import Pitch
from flask_script import Manager, Server
from  flask_migrate import Migrate, MigrateCommand

# creating app instance
app = create_app('development')

manager = Manager(app)
manager.add_command('server',Server)

migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)

if __name__ == '__main__':
    manager.run()