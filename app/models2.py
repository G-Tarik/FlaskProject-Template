"""
Flask-SQLAlchemy models
"""
from uuid import uuid4
from sqlalchemy.dialects.postgresql import UUID
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Stories(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    uuid = db.Column(UUID(as_uuid=True), default=uuid4)
    title = db.Column(db.String(20))
    status = db.Column(db.String(10))

