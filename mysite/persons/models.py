from typing import ChainMap
from django.db import models
import datetime
from django.db import models
from django.utils import timezone

class Person(models.Model):
    name = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    tel = models.CharField(max_length=200)
    dir = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return   self.name 
    