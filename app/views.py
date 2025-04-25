from flask import render_template, redirect
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder import ModelView
from flask_appbuilder import expose, BaseView, has_access

from . import appbuilder, db
from .models import Employee, Department, Function, Transaction


# 📊 Custom Dashboard View
class MyDashboardView(BaseView):
    route_base = "/dashboard"

    @expose('/')
    @has_access
    def index(self):
        transactions = Transaction.query.order_by(Transaction.id.desc()).limit(5).all()
        coins_remaining = 1220  # Replace with dynamic value if available
        coin_percentage = min(100, (coins_remaining / 2000) * 100)
        return render_template('home.html',
                               transactions=transactions,
                               coins_remaining=coins_remaining,
                               coin_percentage=coin_percentage)

appbuilder.add_view_no_menu(MyDashboardView())

# 🔁 Redirect root to /login/
@appbuilder.app.route('/')
def index():
    return redirect('/login/')

# 🚫 Custom 404 page
@appbuilder.app.errorhandler(404)
def page_not_found(e):
    return (
        render_template(
            "404.html", base_template=appbuilder.base_template, appbuilder=appbuilder
        ),
        404,
    )



