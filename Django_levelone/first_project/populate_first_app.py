import os
import sys
os.environ.setdefault('DJANGO_SETTINGS_MODULE','first_project.settings')

import django
django.setup()

# this for pop script
import random
from first_app.models import Accessrecord, Webpage,Topic
from faker import Faker

fake_generator = Faker()

topics = ['Search Engine','Social','Online Shopping','Games','New']


def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t


def populate(N=5):

    for entry in range(N):

        #get the topic for entry

        top = add_topic()


        # now create fake dat for that entry
        fake_url = fake_generator.url()
        fake_date = fake_generator.date()
        fake_name = fake_generator.company()



        # new enrty for Webpage

        webpg = Webpage.objects.get_or_create(topic=top,url=fake_url,name=fake_name)[0]


        # create entry for Accessrecord

        access_date = Accessrecord.objects.get_or_create(name=webpg,date=fake_date)[0]

if __name__ == '__main__':
   print("populating script")
   populate(15)
   print("population complete")
