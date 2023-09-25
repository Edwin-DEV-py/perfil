from django.db import models
from django.utils import timezone

class Profile(models.Model):
    user = models.CharField(max_length=100, unique=True)
    games = models.IntegerField(default=0)
    sub = models.BooleanField(default=False)
    credits = models.IntegerField(default=0)
    days = models.DateTimeField(null=True,blank=True)
    
    def activate_sub(self):
        self.sub = True
        self.days = timezone.now()
        self.save()
        
    def deactivate_sub(self):
        self.sub = False
        self.days = None
        self.save()
        
    def is_active_sub(self):
        if self.days is not None:
            expire_sub = self.days + timezone.timedelta(days=30)
            return expire_sub >= timezone.now()
        return False
    
class UserInventory(models.Model):
    user = models.CharField(max_length=100)
    id_carta = models.CharField(max_length=24)
    quantity = models.IntegerField(default=0)
    type = models.CharField(max_length=20,default='None')
    