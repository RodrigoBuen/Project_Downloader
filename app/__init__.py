from flask import Flask

app = Flask(__name__)
app.config.from_object("config")

from .views import control_view
