from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO
from flask_babel import Babel
from flask_mail import Mail

db = SQLAlchemy()
socketio = SocketIO()
mail = Mail()
babel = Babel()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)
    socketio.init_app(app)
    mail.init_app(app)
    babel.init_app(app)

    with app.app_context():
        from . import routes, models
        db.create_all()
        
    return app
