from .models import UserProfile, User
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=User)
def post_save_create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

    else:
        try:
            profile = UserProfile.objects.get(user=instance)
            profile.save()
        except:
            UserProfile.objects.create(user=instance)