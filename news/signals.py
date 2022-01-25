from django.db.models.signals import post_save
from news.models import News, NewsAuthenticity
from django.contrib.auth.models import User


def create_news_authenticity(sender, instance, created, **kwargs):
	if created:

		for user in User.objects.all():
			NewsAuthenticity.objects.create(
				news=instance, user=user
			)


post_save.connect(create_news_authenticity, sender=News)