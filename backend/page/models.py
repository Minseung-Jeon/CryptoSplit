from django.db import models
import decimal

# Create your models here.
class User(models.Model):
    event_name = models.CharField(max_length=100)
    your_name = models.CharField(max_length=100)
    your_email = models.EmailField(max_length=100)
    friend_name = models.CharField(max_length=100)
    friend_email = models.EmailField(max_length=100)
    amount = models.DecimalField(max_digits=100, decimal_places=2)

    def __str__(self):
        return self.event_name

    