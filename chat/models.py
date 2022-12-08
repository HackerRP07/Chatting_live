from django.db import models
from datetime import datetime
# Create your models here.
class Room(models.Model):
    name =models.CharField(max_length=50)
    
class Message(models.Model):
    value =models.CharField(max_length=500)
    date =models.DateField(default=datetime.now,blank=True)
    user =models.CharField(max_length=50)
    room =models.CharField(max_length=25)