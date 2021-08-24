import binascii
import os
from django.utils import timezone

from django.conf import settings
from django.db import models
from six import python_2_unicode_compatible

@python_2_unicode_compatible
class Token(models.Model):
    """
    The authorization token model based on Mac Address (not user)
    """
    key = models.CharField(max_length=40, primary_key=True)
    forest = models.OneToOneField('api.Forest', related_name='auth_token', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.key:
            self.key = self.generate_key()
        return super(Token, self).save(*args, **kwargs)

    def generate_key(self):
        return binascii.hexlify(os.urandom(20)).decode()

    def __str__(self):
        return self.key
