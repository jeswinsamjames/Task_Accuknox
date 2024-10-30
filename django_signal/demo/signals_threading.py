from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
import threading

@receiver(post_save, sender=User)
def my_signal(sender, **kwargs):
    print(f"Signal thread ID: {threading.get_ident()}")

def save_user():
    print(f"Caller thread ID: {threading.get_ident()}")
    User.objects.create(username="testuser")

save_user()

#Both thread IDs will be the same, showing that Django signals run in the same thread as the caller