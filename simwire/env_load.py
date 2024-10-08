import os
import random
import string

from dotenv import load_dotenv
from os.path import join, dirname

# it is critical that instance variables stay in a segment of code
# that never needs to change such as the current instance's environment name
# load the business access object for communicating with the database




class Config(object):
    DEBUG = True
    TESTING = False
    SESSION_TYPE = 'sqlalchemy'
    SQLALCHEMY_ECHO = True
    PERMANENT_SESSION_LIFETIME = 86400
    MYSQL_CONFIGURATION = {
        'connection_type': '',
        'username': '',
        'password': '',
        'hostname': '',
        'database': ''
    }
    SQLALCHEMY_DATABASE_URI = ''
    SECRET_KEY = ''
    SESSION_SQLALCHEMY = None

    def gen_rand_alphanum(self,length=8):
        characters = string.ascii_letters + string.digits
        return ''.join(random.choice(characters) for _ in range(length))
    
    def set_server_side_session(self, db):
        self.SESSION_SQLALCHEMY = db

    def get_environment_config(self):
        environment_filepaths = [
            join(dirname(__file__), '.env.local'),
            join(dirname(__file__), '../.env.aws')
        ]

        for environment_file in environment_filepaths:
            # setup reader for environment file
            dotenv_path = join(environment_file)
            load_dotenv(dotenv_path)

        self.SECRET_KEY = os.environ.get("SECRET_KEY") or 'default_secret_key'

        RUN_WEB_USING_IDE = int(os.environ.get("RUN_WEB_USING_IDE")) or 0
        MYSQL_USER = os.environ.get("MYSQL_USER") or self.gen_rand_alphanum()
        MYSQL_PASSWORD = os.environ.get("MYSQL_PASSWORD") or self.gen_rand_alphanum()
        MYSQL_DB = os.environ.get("MYSQL_DB") or 'simwire'
        MYSQL_CONNECTOR = os.environ.get("MYSQL_CONNECTOR") or 'mysql'
        MYSQL_HOST = os.environ.get("MYSQL_CONTAINER_HOST") or 'localhost'
        MYSQL_PORT = os.environ.get("MYSQL_PORT") or '3306'
        # USE PYCHARM CONFIGURATION WHEN RUNNING IN DEBUG MODE
        if RUN_WEB_USING_IDE == 1:
            MYSQL_HOST = os.environ.get("MYSQL_PYCHARM_HOST") or 'pycharm_host'

        self.SQLALCHEMY_DATABASE_URI = \
            MYSQL_CONNECTOR + '://' \
            + MYSQL_USER + ':' + MYSQL_PASSWORD + '@' \
            + MYSQL_HOST + ':' + MYSQL_PORT + '/' \
            + MYSQL_DB
