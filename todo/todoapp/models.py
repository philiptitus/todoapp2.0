from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


# Create your models here.

class User_info(models.Model):

   user  = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
   instagram = models.URLField(blank = True)
 


   def __str__(self):
      return self.user.username
   

class Tlist(models.Model):
   item = models.CharField(unique=True,max_length=250)
   description = models.TextField(max_length=1000)
   completion_date = models.DateTimeField(auto_now=True)
   date_completed = models.DateTimeField(blank=True, null=True)
   user = models.ForeignKey(User, default=None, null=True, on_delete=models.CASCADE)

   def __str__(self):
         return self.item
   