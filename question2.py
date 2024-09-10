#Yes, by default, Django signals run in the same thread as the caller.

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
import threading

@receiver(post_save, sender=User)
def save_the_user(sender, instance, **kwargs):
    print("Signal received in thread:", threading.current_thread().name)

def create_the_user():
    print("User created in thread:", threading.current_thread().name)
    User.objects.create(username='test_user')

create_the_user()
