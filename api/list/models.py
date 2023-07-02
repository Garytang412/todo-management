from django.db import models
from django.contrib.auth.models import User
from group.models import Group

# Create your models here.
class Priority(models.Model):
    name = models.CharField(max_length=200)
    color = models.CharField(max_length=7)
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='priorities')
    
    def __str__(self):
        return self.name

class List(models.Model):
    title = models.CharField(max_length=200)
    priority = models.ForeignKey(Priority, on_delete=models.CASCADE,related_name='lists')
    group = models.ForeignKey(Group, on_delete=models.CASCADE,related_name='lists')
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='lists')

    def __str__(self):
        return self.title