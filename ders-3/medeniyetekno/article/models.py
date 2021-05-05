from django.db import models
from django.contrib.auth.models import User

class article(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=200,unique=True)
    content = models.TextField()