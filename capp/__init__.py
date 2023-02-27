from flask import Flask
import os

application = Flask(__name__)

# application.config['SECRET_KEY'] = os.environ['SECRET_KEY']  

application.config['SECRET_KEY'] = '4f3f72cb819c76576b54a3fea56499875e97e020804e1466'

from capp.home.routes import home
from capp.methodology.routes import methodology
from capp.carbon_app.routes import carbon_app
from capp.users.routes import users

application.register_blueprint(home)
application.register_blueprint(methodology)
application.register_blueprint(carbon_app)
application.register_blueprint(users)

