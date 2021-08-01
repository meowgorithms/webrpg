from flask_sqlalchemy import Model
from app import db

# Needs to be pulled from DB:
# archetype base stats

class ArchetypeModel(Model):
    