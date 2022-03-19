from django.db import models

# Create your models here.
class levelMod(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    score = models.IntegerField(default=0)
    level = models.CharField(max_length=20)