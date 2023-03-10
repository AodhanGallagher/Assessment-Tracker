# Importing relevant modules and creating the database
from config import SQLALCHEMY_DATABASE_URI
from app import db
import os.path

db.create_all()