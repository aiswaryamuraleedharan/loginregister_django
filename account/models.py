from django.db import models

class RegisterDetails(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField(max_length=50)
    phonenumber = models.CharField(max_length=25)
    age = models.IntegerField()
    place = models.CharField(max_length=25)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.name
