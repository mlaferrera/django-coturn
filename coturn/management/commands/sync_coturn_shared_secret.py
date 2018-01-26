from django.conf import settings
from django.core.management.base import BaseCommand
from coturn.models import TurnSecret

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        realm = settings.COTURN_REALM
        secret = settings.COTURN_SHARED_SECRET
        if len(secret) > 127:
            raise Exception("Coturn's database doesn't support secrets longer than 127 characters")
        for entry in TurnSecret.objects.using('coturn').all():
            entry.delete(using="coturn")
        new_secret = TurnSecret(realm=realm, value=secret)
        new_secret.save(using="coturn")
