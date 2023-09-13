from django.contrib import admin
from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'id_carta','games', 'sub', 'credits')

admin.site.register(Profile,ProfileAdmin)
