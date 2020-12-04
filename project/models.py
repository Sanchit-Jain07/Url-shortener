from .import db

class Links(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    link = db.Column(db.Text, nullable=False)