from django.db import models

# Create your models here.
class userrecord(models.Model):
    First_Name = models.CharField(max_length=264,unique=True)
    Last_Name = models.CharField(max_length=264,unique=True)
    Email = models.EmailField(unique=True)

    def __str__(self):
        return self.First_Name
