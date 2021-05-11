from django.db.models.signals import post_save
from users.models import Connect4ProUser
from django.dispatch import receiver
from users.models import BusinessProfile, ProviderProfile


# This function aims to create a profile everytime a user registers
@receiver(post_save, sender=Connect4ProUser)
def create_profile(sender, instance, created, **kwargs):
    if created and instance.last_name == True:
        BusinessProfile.objects.create(user=instance)
    elif created and instance.last_name == False:
        ProviderProfile.objects.create(user=instance)


# kwargs just accepts any additional keyword arguments on the end of the function
@receiver(post_save, sender=Connect4ProUser)
def save_profile(sender, instance, **kwargs):
    if instance.last_name == True:
        instance.business_profile.save()
    elif instance.last_name == False:
        instance.provider_profile.save()
