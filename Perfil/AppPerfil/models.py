from django.db import models

class Profile(models.Model):
    user = models.CharField(max_length=100, unique=True)
    games = models.IntegerField(default=0)
    sub = models.BooleanField(default=False)
    credits = models.IntegerField(default=0)
    
class UserInventory(models.Model):
    user = models.CharField(max_length=100)
    id_carta = models.CharField(max_length=24)
    quantity = models.IntegerField(default=0)
    type = models.CharField(max_length=20,default='None')
    