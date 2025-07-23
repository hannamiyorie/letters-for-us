from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy ()

class Message(db.Model):
    __tablename__ = 'message'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    def to_dict(self):
            return {
                "id": self.id,
                "name" : self.name,
                "content" : self.content,
                "created_at" : self.created_at.strftime("%d %B %Y %H:M")
            }
    