import os
import sys
os.environ.setdefault('DJANGO_SETTINGS_MODULE','ProTwo.settings')

import django
django.setup()

# this for pop script
import random
from AppTwo.models import userrecord
from faker import Faker

fake_generator = Faker()

def populate(N=5):

    for entry in range(N):

        # now create fake dat for that entry
        fake_Fname = fake_generator.first_name()
        fake_Lname = fake_generator.last_name()
        fake_email = fake_generator.email()



        # new enrty for Webpage

        User_record = userrecord.objects.get_or_create(First_Name=fake_Fname,Last_Name=fake_Lname,Email=fake_email)[0]


if __name__ == '__main__':
   print("populating script")
   populate(15)
   print("population complete")
