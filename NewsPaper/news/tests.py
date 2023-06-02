from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from django.test import TestCase

from news.models import PostCategory


# Create your tests here.

@receiver(m2m_changed, sender=PostCategory)
def notify_post_created(sender, instance, **kwargs):
    if kwargs['action'] == 'post_add':
        categories = instance.categories.all()
        subscribers_user = []
        subscribers_emails=[]
        for cat in categories:
            subscribers = cat.subscriber.all()
            subscribers_user += [s.user for s in subscribers]

        for mail in subscribers_user:
            mails = mail.email
            subscribers_emails += mail
