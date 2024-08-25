from flask import Flask, jsonify, request, render_template
from .env_load import Config
from flask_cors import CORS
from flask_login import LoginManager
from .blueprints import home_bp, auth_bp
from .models import db, migrate
from .models import User


app = Flask(__name__, template_folder='templates')
CORS(app)


config = Config()
config.get_environment_config()
config.set_server_side_session(db)
config.SQLALCHEMY_DATABASE_URI= 'sqlite:///yourdatabase.db'
# sqlalchemy needs to know the database configuration
app.config.from_object(config)


# Initialize Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
# initialize sqlalchemy
db.init_app(app)
migrate.init_app(app, db)

# User loader function for Flask-Login
@login_manager.user_loader
def load_user(user_id: int):
    # Replace this with your logic for loading users from a database
    return User.query.get(user_id)

# this makes the app aware of the modules that need to be loaded
app.register_blueprint(home_bp)
app.register_blueprint(auth_bp)