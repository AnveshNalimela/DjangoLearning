from django.db import models

# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='teams')
    age=models.IntegerField()
    isSuperUser=models.BooleanField(default=False)
