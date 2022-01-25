from django.contrib import admin
from news.models import *

# Register your models here.
class NewsAdmin(admin.ModelAdmin):
	list_display = ('news_headline', "category", "source_url", "total_autheticities")

	def total_autheticities(self, obj):
		# This method represents the total user count.
		return NewsAuthenticity.objects.filter(news=obj).count()

admin.site.register(News, NewsAdmin)
admin.site.register(NewsAuthenticity)