from django.db import models

# Create your models here.

class User(models.Model):
    name=models.CharField(max_length=25)
    email=models.EmailField(primary_key=True)
    phoneno=models.CharField(max_length=18)
    password=models.CharField(max_length=18)
    username=models.CharField(max_length=18)
    gender=models.CharField(max_length=1)
    dob=models.DateField()

    def __str__(self):
        return self.username
