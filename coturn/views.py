import hmac
import hashlib
import base64
import datetime
from django.conf import settings
from .models import TurnSecret


_epoch = datetime.datetime(1970,1,1, tzinfo=datetime.timezone.utc)

def _get_epochtime(time):
    epochtime = (time - _epoch).total_seconds()
    return epochtime

def create_TURN_API_password(username):
    if hasattr(settings, "COTURN_PASSWORD_LIFETIME"):
        lifetime = int(settings.COTURN_PASSWORD_LIFETIME)
    else:
        lifetime = 60
    stamp = datetime.datetime.now(tz=datetime.timezone.utc)
    stamp += datetime.timedelta(seconds=lifetime)
    epoch_stamp = _get_epochtime(stamp)
    temp_username = "{}:{}".format(epoch_stamp, username)
    secret = TurnSecret.objects.using("coturn").all()[0]
    hash_val = hmac.new(secret.value, temp_username, hashlib.sha1)
    encoded = base64.b64encode(hash_val.digest())
    return temp_username, encoded
