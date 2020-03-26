from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Notes(models.Model): 
    name = models.CharField(max_length=30, unique=True) 
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    def __str__(self):
        return str(self.id)+": "+self.name

class Items(models.Model): 
    item_name = models.CharField(max_length=30, unique=True) 
    note_id = models.ForeignKey(Notes, on_delete = models.CASCADE, related_name='items')
    def __str__(self):
        return str(self.id)+": "+self.item_name


