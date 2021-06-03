from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, default="")
    email = models.CharField(max_length=50, default="")
    mobile = models.CharField(max_length=10, default="")

    def __str__(self):
        return self.first_name