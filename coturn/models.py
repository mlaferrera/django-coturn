# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class AdminUser(models.Model):
    name = models.CharField(unique=True, max_length=32, blank=True, null=True)
    realm = models.CharField(max_length=127, blank=True, null=True)
    password = models.CharField(max_length=127, blank=True, null=True)

    class Meta:
        db_table = 'admin_user'


class AllowedPeerIp(models.Model):
    realm = models.CharField(max_length=127, blank=True, null=True)
    ip_range = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        db_table = 'allowed_peer_ip'
        unique_together = (('realm', 'ip_range'),)


class DeniedPeerIp(models.Model):
    realm = models.CharField(max_length=127, blank=True, null=True)
    ip_range = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        db_table = 'denied_peer_ip'
        unique_together = (('realm', 'ip_range'),)


class OauthKey(models.Model):
    kid = models.CharField(unique=True, max_length=128, blank=True, null=True)
    ikm_key = models.CharField(max_length=256, blank=True, null=True)
    timestamp = models.BigIntegerField(blank=True, null=True)
    lifetime = models.IntegerField(blank=True, null=True)
    as_rs_alg = models.CharField(max_length=64, blank=True, null=True)
    realm = models.CharField(max_length=127, blank=True, null=True)

    class Meta:
        db_table = 'oauth_key'


class TurnOriginToRealm(models.Model):
    origin = models.CharField(unique=True, max_length=127, blank=True, null=True)
    realm = models.CharField(max_length=127, blank=True, null=True)

    class Meta:
        db_table = 'turn_origin_to_realm'


class TurnRealmOption(models.Model):
    realm = models.CharField(max_length=127, blank=True, null=True)
    opt = models.CharField(max_length=32, blank=True, null=True)
    value = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        db_table = 'turn_realm_option'
        unique_together = (('realm', 'opt'),)


class TurnSecret(models.Model):
    realm = models.CharField(max_length=127, blank=True, null=True)
    value = models.CharField(max_length=127, blank=True, null=True)

    class Meta:
        db_table = 'turn_secret'
        unique_together = (('realm', 'value'),)


class TurnusersLt(models.Model):
    realm = models.CharField(max_length=127, blank=True, null=True)
    name = models.CharField(max_length=512, blank=True, null=True)
    hmackey = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        db_table = 'turnusers_lt'
        unique_together = (('realm', 'name'),)
