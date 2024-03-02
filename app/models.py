from django.db import models

# Create your models here.

class Team(models.Model):
    Teamname=models.CharField(max_length=10)
    captain=models.CharField(max_length=20)
    Homeground=models.CharField(max_length=20)

    def __str__(self):
        return self.Teamname
