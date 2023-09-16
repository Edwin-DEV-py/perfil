from django.contrib import admin
from .models import Profile,UserInventory

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user','games', 'sub', 'credits')
    
class UserInventoryAdmin(admin.ModelAdmin):
    list_display = ('user','id_carta')

admin.site.register(Profile,ProfileAdmin)
admin.site.register(UserInventory,UserInventoryAdmin)
