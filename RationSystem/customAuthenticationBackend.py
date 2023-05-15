from django.contrib.auth.backends import BaseBackend
from .models import RationUser
from django.db.models import Q

class RationUserAuthenticationBackend(BaseBackend):
    def authenticate(self, request, email=None, rationId=None, password=None, **kwargs):
        try:
            # Check if email exists in database
            if not RationUser.objects.filter(email=email).exists():
                return None
            
            # Retrieve RationUser object with provided email and ration ID
            user = RationUser.objects.get(Q(email=email) and Q(rationId=rationId))
            
            if user.check_password(password):
                return user
        except RationUser.DoesNotExist:
            return None
