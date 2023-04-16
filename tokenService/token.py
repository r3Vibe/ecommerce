from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes


class VerificationToken:
    def __init__(self, user) -> None:
        self.user = user

    def encode_pk(self):
        return urlsafe_base64_encode(force_bytes(self.user.pk))

    @staticmethod
    def decode_pk(pk):
        return urlsafe_base64_decode(pk).decode()

    def generate_token(self):
        return default_token_generator.make_token(self.user)

    @staticmethod
    def verify_token(user, token):
        return default_token_generator.check_token(user, token)
