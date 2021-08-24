from django.contrib import admin
from .models import Token


class TokenAdmin(admin.ModelAdmin):
    list_display = ('key', 'forest', 'created')
    fields = ('forest',)
    ordering = ('-created',)

admin.site.register(Token, TokenAdmin)