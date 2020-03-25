import auth
from mongoengine import *


class User(Document):
    name = StringField(max_length=50, required=True)
    email = StringField(max_length=50, required=True)
    password = StringField(required=True)

    @classmethod
    def check_credentials(cls, email, password):
        user = cls.objects(email=email)
        ok = auth.check_encrypted_password(password, user.password)

        return user if user and ok else False
