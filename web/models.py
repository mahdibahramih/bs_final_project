from django.db import models
from datetime import datetime
from django.db import models
# Create your models here.


class news(models.Model):
    header = models.CharField(max_length=60)
    text = models.TextField()
    TTL = models.DateField()
    def  __str__(self):
        return "{}  ---  {} ---  {}".format(self.header ,self.text , self.TTL)


class client(models.Model):
    token = models.CharField(max_length=60)
    place = models.CharField(max_length=100)
    def  __str__(self):
        return "{}  ------  {} ".format(self.token ,self.place)