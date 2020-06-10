
from werkzeug.security import generate_password_hash, check_password_hash

from find_it import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    is_admin = db.Column(db.Boolean(), server_default="false", nullable=False)
    points = db.Column(db.BigInteger(), server_default="0", nullable=False)
    submissions = db.Column(db.Integer(), server_default="0", nullable=False)

    DISALLOWED_USERNAMES = (
        'admin', 'findit', 'find_it', 'administrator'
    )

    def __init__(self, username):
        self.username = username
        self.is_admin = False

    def __repr__(self):
        return '<User %r>' % self.username

    @property
    def password(self):
        raise AttributeError('this is a write-only field')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)
