from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import BlogPost
from django.core.mail import send_mail
from django.conf import settings


@receiver(post_save, sender=BlogPost)
def notify_admin_new_post(sender, instance, **kwargs):
    if instance.status == "published":
        send_mail(
            f"{instance.title}",
            f"Blog post titled {instance.title} has been created. Body {instance.body}",
            "someuser@email.com",
            [
                settings.DEFAULT_FROM_EMAIL,
                "spaceyatech@emailcom",
                "community@django.com",
            ],
        )


@receiver(post_delete, sender=BlogPost)
def notify_admin_post_deleted(sender, instance, **kwargs):
    print(f"Blog post titled {instance.title} has been deleted.")
