from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=100, default = "default")
    email = models.CharField(max_length=100, default = "default")
    password = models.CharField(max_length=100, default = "default")

    def __str__(self):
        return self.name
    
class Money(models.Model):
    amount = models.IntegerField(default=0)
    complete = models.BooleanField(default=False)


    def __str__(self):
        return self.amount
    