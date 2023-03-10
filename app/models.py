# Importing relevant modules and creating the database schema / template
from app import db

class Assessments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30))
    module_code = db.Column(db.String(10), index=True)
    deadline = db.Column(db.Date)
    description = db.Column(db.String(125))
    complete = db.Column(db.Boolean)