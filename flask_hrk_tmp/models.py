"""
Model User 
demo: single table
Created BY: https://hackersandslackers.com/flask-login-user-authentication/
Modified BY: NajlaBH
"""

from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from .extensions import db 

class User(UserMixin, db.Model):
    """Model for user accounts."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    password = db.Column(db.String(100))
    #expert = db.Column(db.Boolean)
    #admin = db.Column(db.Boolean)



    @property
    def unhashed_password(self):
        raise AttributeError('Cannot view unhashed password!')

    @unhashed_password.setter
    def unhashed_password(self, unhashed_password):
        self.password = generate_password_hash(unhashed_password)


    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password, method='sha256')

    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)

    def __repr__(self):
        return '<User {}>'.format(self.username)
