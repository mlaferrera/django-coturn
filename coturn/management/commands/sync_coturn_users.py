from django.contrib.auth.models import User
from django.conf import settings
from django.core.management.base import BaseCommand
from coturn.models import TurnusersLt
import hmac
import hashlib


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        realm = settings.COTURN_REALM
        # NOTE: since we assume the system will be running coturn in REST API mode, this password will never be used.
        # so we set it to something random.
        password = User.objects.make_random_password()
        for user in User.objects.all():
            hash_val = hmac.new(settings.SECRET_KEY, password, hashlib.sha1)
            hash_val.update(realm)
            new_user = TurnusersLt(name=user.get_username(), realm=realm, password=hash_val.digest())
            new_user.save(using="coturn")
