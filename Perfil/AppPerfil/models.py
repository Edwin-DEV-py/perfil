from django.db import models

class Profile(models.Model):
    user = models.CharField(max_length=100, unique=True)
    id_carta = models.CharField(max_length=24)
    games = models.IntegerField()
    sub = models.BooleanField(default=False)
    credits = models.IntegerField(default=0)
    