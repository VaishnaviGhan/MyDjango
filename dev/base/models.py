from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=128)
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return self.name
