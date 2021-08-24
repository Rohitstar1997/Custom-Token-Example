from .models import Forest
from rest_framework import serializers
from django.core.exceptions import ValidationError
class ForestSerializer(serializers.ModelSerializer):
    # name = serializers.CharField(max_length=20)
    class Meta:
        model = Forest
        fields = ('name', 'dept_name', 'city', 'state', 'country')
    
    def validate_name(self, value):
        if len(value) < 4:
            raise ValidationError("this forest name must be above 4 letters")
        return value
    
    def create(self, validated_data):
        user = Forest.objects.create(name=validated_data['name'])
        user.is_staff=True
        user.save()
        return user