from flask import Flask
from flask_bootstrap import Bootstrap
from config import Config
from handler import Handler

app = Flask(__name__)
app.config.from_object(Config)
bootstrap = Bootstrap(app)
# handler = Handler()

from webapp import routes

