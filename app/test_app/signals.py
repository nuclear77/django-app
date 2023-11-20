from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Library


@receiver(post_save, sender=Library)
def Item_created(sender, instance, created, **kwergs):
    if created:
        print("была создана библиотека", instance.name)
    else:
        print("библиотека обновлена", instance.name)

