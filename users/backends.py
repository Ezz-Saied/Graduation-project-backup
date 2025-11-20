from django.contrib.auth.backends import ModelBackend
from .models import User

class EmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        if username is None or password is None:
            return None

        try:
            user = User.objects.get(email=username)
        except User.DoesNotExist:
            return None

        # block unverified users (except superuser)
        if not user.is_superuser and not user.is_verified:
            return None

        if user.check_password(password):
            return user
        return None
