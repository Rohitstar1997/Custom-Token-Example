from django.contrib import admin
from .models import Token


class TokenAdmin(admin.ModelAdmin):
    list_display = ('key', 'forest', 'created')
    fields = ('forest',)
    ordering = ('-created',)
    
    # def get_object(self, request, object_id, from_field=None):
    #     """
    #     Map from User ID to matching Token.
    #     """
    #     queryset = self.get_queryset(request)
    #     field = User._meta.pk
    #     try:
    #         object_id = field.to_python(object_id)
    #         user = User.objects.get(**{field.name: object_id})
    #         return queryset.get(user=user)
    #     except (queryset.model.DoesNotExist, User.DoesNotExist, ValidationError, ValueError):
    #         return None

    # def delete_model(self, request, obj):
    #     # Map back to actual Token, since delete() uses pk.
    #     token = Token.objects.get(key=obj.key)
    #     return super().delete_model(request, token)

admin.site.register(Token, TokenAdmin)