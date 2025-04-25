import logging
from flask import Flask, redirect, url_for
from flask_appbuilder import AppBuilder, SQLA, IndexView
from flask_appbuilder.views import expose
from flask_login import current_user  # <-- Import this

"""
 Logging configuration
"""
logging.basicConfig(format="%(asctime)s:%(levelname)s:%(name)s:%(message)s")
logging.getLogger().setLevel(logging.DEBUG)

# Custom IndexView that redirects only if not logged in
class MyIndexView(IndexView):
    route_base = "/"

    @expose("/")
    def index(self):
        if not current_user.is_authenticated:
            return redirect(url_for("AuthDBView.login"))
        return super().index()  # fallback to default welcome page or dashboard

app = Flask(__name__)
app.config.from_object("config")
db = SQLA(app)
appbuilder = AppBuilder(app, db.session, indexview=MyIndexView)

from . import views

