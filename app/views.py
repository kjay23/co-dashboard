from flask import render_template, redirect
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder import ModelView

from . import appbuilder, db
from .models import Employee, Department, Function


class EmployeeView(ModelView):
    datamodel = SQLAInterface(Employee)
    list_columns = ['full_name', 'department', 'employee_number']


class FunctionView(ModelView):
    datamodel = SQLAInterface(Function)
    related_views = [EmployeeView]


class DepartmentView(ModelView):
    datamodel = SQLAInterface(Department)
    related_views = [EmployeeView]


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

# 🗂️ Database init and view registration
db.create_all()

appbuilder.add_view(EmployeeView, "Employees", icon="fa-folder-open-o", category="Company")
appbuilder.add_separator("Company")
appbuilder.add_view(DepartmentView, "Departments", icon="fa-folder-open-o", category="Company")
appbuilder.add_view(FunctionView, "Functions", icon="fa-folder-open-o", category="Company")

