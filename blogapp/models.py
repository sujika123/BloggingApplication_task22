from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class Login(AbstractUser):
    is_user = models.BooleanField(default=False)

class userlogin(models.Model):
    user = models.ForeignKey(Login,on_delete = models.CASCADE,related_name = 'user',null=True)
    name = models.CharField(max_length=50)
    email =  models.EmailField()

    def __str__(self):
        return self.name

class blog(models.Model):
    user = models.ForeignKey(Login, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=150)
    content = models.TextField()
    author = models.CharField(max_length=100)
    pubdate = models.DateField(auto_now=True)
    status = models.IntegerField(default=0)

    def __str__(self):
        return self.title

