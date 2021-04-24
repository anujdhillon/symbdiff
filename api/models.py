from django.db import models
from datetime import datetime

# Create your models here.

class Comment(models.Model):
  content = models.CharField(max_length=200)
  author = models.CharField(max_length=50,default="anonymous")
  date_created = models.DateTimeField(default=datetime.now)

      
  def __str__(self):
    return self.content