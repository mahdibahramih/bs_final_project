from django.db import models
from datetime import datetime
from django.db import models

# Create your models here.


class client(models.Model):
    token = models.CharField(max_length=60 , primary_key=True )
    place = models.CharField(max_length=100)
    def  __str__(self):
        return "{}  ------  {} ".format(self.token ,self.place)



class news(models.Model):
    header = models.CharField(max_length=60)
    text = models.TextField()
    TTL = models.DateField()
    clients = models.ForeignKey(client, on_delete=models.CASCADE)
    def  __str__(self):
        return "{}  ---  {} ---  {}".format(self.header ,self.text , self.TTL)


class poster(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()
    field_name = models.ImageField(height_field=None, width_field=None, max_length=100)
    timetolive = models.DateField()
    is_first = models.BooleanField(default = False)
    clients = models.ForeignKey(client, on_delete=models.CASCADE)
    def __str__(self):
        return "{}  ----  {} ---- {}   --------------------- {}".format(self.title , self.text , self.timetolive , self.field_name)



class subscribed(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=11)
    email = models.CharField(max_length=50)
    def __str__(self):
        return "{}  -----  {} ----- {} ".format(self.name , self.phone , self.email)
