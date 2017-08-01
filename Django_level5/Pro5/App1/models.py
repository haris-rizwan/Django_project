from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# the user class in django already has Username ,F_name , L_name,and email address
# included in it

# we creat the class to add adtional information or attributes for the user

class UserProfileInfo(models.Model):

    user = models.OneToOneField(User)

    #adtional attributes go below it

    profile_url = models.URLField(blank=True)

    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)


    def __str__(self):
        return self.user.username
