from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
import time

@receiver(post_save, sender=User)
def my_signal(sender, **kwargs):
    print("Signal started")
    time.sleep(2)  
    print("Signal finished")

def save_user():
    print("Before saving user")
    user = User.objects.create(username="testuser")
    print("After saving user")

save_user()

#After saving user only prints after the signal finishes executing, it confirms that Django signals are synchronous by default