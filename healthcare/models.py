from django.db import models

# Create your models here.


class User(models.Model):

    email = models.EmailField(max_length=70, blank=True)

    phone_number = models.CharField(max_length=10)

    def __str__(self):
        return self.email