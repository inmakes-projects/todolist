from django.db import models

# Create your models here.

class Task(models.Model):
    name = models.CharField(max_length=100)
    priority = models.IntegerField()
    date = models.DateField(auto_now=False)

    def __str__(self):
        return self.name
    
