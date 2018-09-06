from . import db

class Pitch(db.Model):

    __tablename__ = 'pitchs'

    id = db.Column(db.Integer, primary_key = True)
    category = db.Column(db.String)
    pitch = db.Column(db.String)

    def save_pitch(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_pitch(cls,cat):
        pitch = Pitch.query.filter_by(category=cat).all()
        return pitch