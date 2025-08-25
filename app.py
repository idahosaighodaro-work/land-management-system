from flask import Flask
from models.request_model import db
from views import request_bp
from config.settings import Config

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
app.register_blueprint(request_bp)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)