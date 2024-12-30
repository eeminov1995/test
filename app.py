from flask import Flask
from models import db
from routes.main import main
from routes.api import api
from utils.helpers import add_header
from config.config import Config

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

with app.app_context():
    db.create_all()

app.register_blueprint(main)
app.register_blueprint(api)

@app.after_request
def after_request(response):
    return add_header(response)

if __name__ == '__main__':
    app.run(debug=True)
