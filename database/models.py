from mongoengine import Document, EmailField, StringField,ListField, ReferenceField,PULL,CASCADE
from flask_bcrypt import generate_password_hash, check_password_hash
import string, random


class Movie(Document):
    name = StringField(required=True, unique=True)
    casts = ListField(StringField(), required=True)
    genres = ListField(StringField(), required=True)
    added_by = ReferenceField('User')

class User(Document):
    email = EmailField(required=True, unique=True)
    password = StringField(required=True, min_length=6)
    movies = ListField(ReferenceField('Movie', reverse_delete_rule=PULL))
    salt = StringField()
    def hash_password(self):
        chars = string.ascii_letters + string.punctuation
        size = 12
        self.salt = ''.join(random.choice(chars) for x in range(size))
        self.password = generate_password_hash(self.password + self.salt).decode('utf8')
    def check_password(self, password):
        return check_password_hash(self.password, password + self.salt)

User.register_delete_rule(Movie, 'added_by', CASCADE)