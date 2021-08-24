from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from auth_token.models import Token
# Create your models here.

class Forest(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    dept_name = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    
    ordering = ('created_at')
    
    def __str__(self):
        if self.name==None:
            return "error"
        return self.name

@receiver(post_save, sender=Forest)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(forest=instance)    