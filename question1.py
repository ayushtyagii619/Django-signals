from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
import time

@receiver(post_save, sender=User)
def save_the_user(sender, instance, **kwargs):
    print("Signal received.")
    time.sleep(5)
    print("Processing complete.")

def create_the_user():
    print("User Creating.....")
    User.objects.create(username='test_user')
    print("User created.")

create_the_user()

'''By default, Django signals are executed synchronously. 
This means that the signal's connected receiver functions are called in the 
same thread and at the same time as the code that sends the signal. '''