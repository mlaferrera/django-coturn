import hmac
import hashlib
from django.conf import settings
from django.contrib.auth.models import User
from .models import TurnusersLt


def sync_new_user_to_coturn(sender, instance, **kwargs):
    ##
    # NOTE: Do not use this for REST API. You do not need to sync users if you are using the REST API.
    #
    #
    if sender == User:
        username = instance.get_username()
    else:
        if not hasattr(settings, "COTURN_USERNAME_FIELD"):
            raise ImportError("Coturn was sent a signal from a non-django User model, but COTURN_USERNAME_FIELD is not set")
        if not hasattr(instance, settings.COTURN_USERNAME_FIELD):
            raise ValueError("Coturn - username field {} does not exist on model we were sent in sync signal".format(settings.COTURN_USERNAME_FIELD))
        if "." in settings.COTURN_USERNAME_FIELD:
            # walk down the set of sub-fields until you reach the username
            fields = settings.COTURN_USERNAME_FIELD.split(".")
            working_instance = instance
            for field in fields:
                if hasattr(working_instance, field):
                    working_instance = getattr(working_instance, field)
                else:
                    raise ValueError("missing sub-field in username search: {}".format(field))
            username = working_instance()
        else:
            username = getattr(instance, settings.COTURN_USERNAME_FIELD)
            username = username()
    if not hasattr(settings, "COTURN_REALM"):
        raise ValueError("Coturn - missing COTURN_REALM entry in settings.py")
    realm = settings.COTURN_REALM
    # NOTE: since we assume the system will be running coturn in REST API mode, this password will never be used.
    # so we set it to something random.
    password = User.objects.make_random_password()
    hash_val = hmac.new(settings.SECRET_KEY.encode("utf-8"), password.encode("utf-8"), hashlib.sha1)
    hash_val.update(realm)
    new_user = TurnusersLt(name=username, realm=realm, password=hash_val.hexdigest())
    new_user.save(using="coturn")

