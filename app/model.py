from . import db, ma
from datetime import datetime

class Post(db.Model):
    __tablename__ = 'user_posts'
    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(20))
    summary = db.Column(db.String(20))
    description = db.Column(db.String(300))
    posted = db.Column(db.DateTime,default=datetime.utcnow)

    def __init__(self,  title, description, posted):
        self.description = description
        self.posted = posted
        self.title = title


    def __repr__(self):
        return f'Pitch {self.id}'
    
   
    def save_pitch(self):
        db.session.add(self)
        db.session.commit()

class PitchSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'description', 'posted')