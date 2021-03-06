import os

from flask import Flask

app = Flask(__name__)
print("init happened")
config_path = os.environ.get("CONFIG_PATH", "germanapp.config.DevelopmentConfig")
app.config.from_object(config_path)

from . import api
