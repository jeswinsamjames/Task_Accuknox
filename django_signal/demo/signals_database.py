from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

@receiver(post_save, sender=User)
def my_signal(sender, instance, **kwargs):
    instance.username = "signaluser"
    instance.save()

def save_user():
    try:
        with transaction.atomic():
            user = User.objects.create(username="testuser")
            raise Exception("Rolling back transaction")
    except Exception:
        try:
            User.objects.get(username="signaluser")
            print("Signal ran in a separate transaction")
        except ObjectDoesNotExist:
            print("Signal ran in the same transaction as the caller")

save_user()

# we cannot retrieve "signaluser" it proves that the signal ran in the same transaction and was rolled back