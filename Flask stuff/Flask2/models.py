from Flask2 import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    #User table
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(140), unique=True, nullable=False)
    image_file = db.Column(db.String(50), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

class WatchLater(db.Model, UserMixin):
    #My watchlater table, this will also contribute  to the genration of recommendations
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    poster = db.Column(db.String, nullable=False)
    id_movie = db.Column(db.Integer, nullable=False)
    User_id = db.Column(db.Integer, nullable=False)
    def __repr__(self):
        return f"WatchLater('{self.title}', '{self.poster}', '{self.id_movie}')"


class Liked(db.Model, UserMixin):
    #This table will also be used for reccomendations
    id= db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    poster = db.Column(db.String, nullable=False)
    id_movie = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Liked('{self.title}', '{self.poster}', '{self.id_movie}')"
