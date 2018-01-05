import os
from flask_script import Manager, Shell, Server
from flask_script.commands import Clean, ShowUrls
from flask_migrate import MigrateCommand

from elastichq.factory import create_app

from elastichq.settings import DevConfig, ProdConfig
from elastichq.database import db

if os.environ.get("ELASTICHQ_ENV") == 'prod':
    app = create_app(ProdConfig)
else:
    app = create_app(DevConfig)

manager = Manager(app)


def _make_context():
    return {'app': app, 'db': db}


@manager.command
def test():
    import pytest
    exit_code = pytest.main([os.path.join(os.path.abspath(os.path.dirname(__file__)), 'tests'), '--verbose'])
    return exit_code


manager.add_command('server', Server())
manager.add_command('shell', Shell(make_context=_make_context))
manager.add_command('db', MigrateCommand)
manager.add_command("urls", ShowUrls())
manager.add_command("clean", Clean())

if __name__ == '__main__':
    manager.run()
