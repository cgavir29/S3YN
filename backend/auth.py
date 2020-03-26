from passlib.hash import pbkdf2_sha256 as pass256


def encrypt_password(password):
    return pass256.hash(password)


def check_encrypted_password(password, hash):
    return pass256.verify(password, hash)
