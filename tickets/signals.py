from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.utils.timezone import now
from .models import Ticket

@receiver(post_save, sender=Ticket)
def set_ticket_status(sender, instance, **kwargs):
    seconds_elapsed = (now() - instance.created_at).seconds
    print(f"Time since creation: {seconds_elapsed} seconds.")
    if instance.pk is not None and seconds_elapsed > 60:
        instance.status = 'old'
        instance.save()
        print(f"Signal: Ticket {instance.id} status set to 'old'")
    else:
        print(f"Signal condition not met for Ticket {instance.id}")

