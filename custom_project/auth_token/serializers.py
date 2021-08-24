from django.contrib.auth import authenticate
from django.utils.translation import ugettext_lazy as _

from rest_framework import serializers

from api.models import Forest

class AuthTokenSerializer(serializers.Serializer):
    name = serializers.CharField()

    def validate(self, attrs):
        name = attrs.get('name')

        if Forest.objects.filter(name=name).exists():
            forest = Forest.objects.get(name=name)
        else:
            msg = _('name is not Created')
            raise serializers.ValidationError(msg)

        attrs['forest'] = forest
        return attrs