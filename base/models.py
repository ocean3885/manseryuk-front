from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=20, blank=True)
    data = models.JSONField(default=dict,blank=True)
    gen = models.CharField(max_length=1,blank=True)
    sl = models.CharField(max_length=10,blank=True)
    year = models.CharField(max_length=4,blank=True)
    month = models.CharField(max_length=2,blank=True)
    day = models.CharField(max_length=2,blank=True)
    hour = models.CharField(max_length=2,blank=True)
    min = models.CharField(max_length=2,blank=True)
        
    def __str__(self):
        return self.name