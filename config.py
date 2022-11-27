import os
# basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    #needed for DATABASE
    HOSTNAME = "localhost"
    DATABASE = "budgetDB"
    USERNAME = "postgres"
    PASSWORD = "KAROLINKA"
    PORT_ID = 5432

    #needed for other Flask configuration
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'SuP3r H@rD K3y'