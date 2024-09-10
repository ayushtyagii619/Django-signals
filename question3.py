#By default, Django signals run in the same database transaction as the caller.
from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def save_the_user(sender, instance, **kwargs):
    print("Signal received, Performing a database operation wit signal.")
    instance.username = 'modified_user'
    instance.save()
    print("Signal processing complete.")

def create_the_user():
    print("Creating user.....")
    with transaction.atomic():
        User.objects.create(username='test_user')
        print("User created.")

create_the_user()
