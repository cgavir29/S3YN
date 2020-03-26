import auth
from mongoengine import Document, StringField


class User(Document):
    name = StringField(max_length=50, required=True)
    email = StringField(max_length=50, unique=True, required=True)
    password = StringField(required=True)

    @classmethod
    def check_credentials(cls, email, password):
        user = cls.objects(email=email)
        if not user:  # Empty list
            return False

        ok = auth.check_encrypted_password(password, user[0].password)
        if not ok:
            return False

        return user[0]
