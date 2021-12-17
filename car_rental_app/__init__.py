from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from flask_bcrypt import Bcrypt
# from flask_login import LoginManager
# from flask_migrate import Migrate
from flask_restful import Api
from config import Configuration

# db = SQLAlchemy()
# login_manager = LoginManager()
# bcrypt = Bcrypt()


def create_app():
    """
    Create flask application
    :return: the created flask application
    """
    app = Flask(__name__)
    app.config.from_object(Configuration)

    from .views import public_blueprint
    app.register_blueprint(public_blueprint)

    # db.init_app(app)
    #
    # bcrypt.init_app(app)
    #
    # login_manager.init_app(app)
    #
    # Migrate(app, db)
    #
    # from .views import user as user_blueprint
    # app.register_blueprint(user_blueprint)

    # from .rest import employee_api, department_api

    # api = Api(app)
    #
    # # adding the department resources
    # api.add_resource(department_api.DepartmentListApi, '/api/departments')
    # api.add_resource(department_api.Department, '/api/departments/<id>')
    #
    # # adding the employee resources
    # api.add_resource(employee_api.EmployeeListApi, '/api/employees')
    # api.add_resource(employee_api.Employee, '/api/employees/<id>')

    # from department_app import models

    return app
