from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Book


@receiver(post_save, sender=Book)
def Item_created(sender, instance, created, **kwergs):
    if created:
        print("была создана книга", instance.title)
    else:
        print("книга обновлена", instance.title)

