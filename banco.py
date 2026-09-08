from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()



class Banco(db.Model):

    __tablename__ = "Banco"

    id = db.Column(db.Integer, primary_key=True)
    beta = db.Column(db.Float, nullable=True)
    tempo = db.Column(db.Integer, nullable=True)

