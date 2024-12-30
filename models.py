from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fio = db.Column(db.String(256), nullable=False)
    email = db.Column(db.String(256), unique=True, nullable=False)
    phone = db.Column(db.String(20), unique=True, nullable=False)
    city = db.Column(db.String(256), nullable=False)
