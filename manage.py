#!/usr/bin/env python
# coding:utf-8

from app import create_app, db
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand
from app.models import User
import logging

app = create_app()
manager = Manager(app)
migrate = Migrate(app, db)
logger = logging.getLogger(__name__)
def make_shell_context():
    return dict(app=app, db=db, user=User)

manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    logger.info('start server')
    manager.run()
