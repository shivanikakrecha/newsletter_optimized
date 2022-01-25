from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save

from userpreference.models import BaseModel


class BulkCreateManager(models.Manager):
    """
    This manager will handle the signal while backend is bulk create of news objects.
    """
    def bulk_create(self, objs, **kwargs):
        response = super(models.Manager,self).bulk_create(objs,**kwargs)
        for i in objs:
            post_save.send(i.__class__, instance=i, created=True)
        return response


# Create your models here.
class News(BaseModel):
    author = models.CharField(max_length=255, null=True, blank=True)
    news_description = models.TextField(null=True, blank=True)
    news_headline = models.TextField()
    category = models.CharField(max_length=30)
    source_url = models.TextField()
    api_endpoint = models.TextField(null=True, blank=True)
    objects = BulkCreateManager()

    def __str__(self):
        return self.news_headline


class NewsAuthenticity(BaseModel):
    news = models.ForeignKey(News, on_delete=models.SET_NULL, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    is_news_autheticate = models.BooleanField(default=False)
    is_notified = models.BooleanField(default=False)

    def __str__(self):
        return self.news.news_headline


'''
SELECT * FROM News WHERE category='entertainment';

###################################### SQL VIEW #########################################
Views are using for to optimized database performance. 

Views can be made accessible to users while the underlying tables are not directly accessible.
This allows the DBA to give users only the data they need, while protecting other data in the
same table.

Ex. We have one table named user is available and we want  to retire user table containing data
    for active users, and instead use a new table with similar data but one that has data for
    both active and inactive users, with one extra column active.

'''

class NewsViewModel(models.Model):
    total_authenticity = models.IntegerField()
    user_approved = models.IntegerField()

    class Meta:
       managed = False