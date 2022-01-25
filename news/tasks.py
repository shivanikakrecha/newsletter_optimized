from celery.decorators import task
from news.utils import EmailThread
from django.contrib.auth.models import User
from django.core import management
from news.models import *
from datetime import datetime
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings


@task(max_retries=5)
def execute_news_letter():

    try:
        print ("Execute celery to fetch news")
        """
        Cleanup expired sessions by using Django management command.
        and call the management command which will fetch the news from the
        api endpoint. Endpoint is described into the env file.
        """
        management.call_command("news_scheduler", verbosity=0)

        '''
        query for fetch news

        SELECT "news_news"."id", "news_news"."created_at", 
        "news_news"."modified_at", "news_news"."author", 
        "news_news"."news_description", "news_news"."news_headline", 
        "news_news"."category", "news_news"."source_url", 
        "news_news"."api_endpoint" FROM "news_news" 
        WHERE ("news_news"."created_at" AT TIME ZONE 'UTC')::date = 2021-06-11
        '''
        news_objects = News.objects.filter(created_at__date=datetime.now().date())
        user_objects = User.objects.all()


        for user in user_objects.filter(id=5):

            user_preferencies = user.fetch_userpreferencies()

            '''
            SELECT "news_news"."id", "news_news"."created_at", 
            "news_news"."modified_at", "news_news"."author", 
            "news_news"."news_description", "news_news"."news_headline", 
            "news_news"."category", "news_news"."source_url", 
            "news_news"."api_endpoint" FROM "news_news" 
            WHERE (("news_news"."created_at" AT TIME ZONE 'UTC')::date = 2021-06-11 
            AND "news_news"."category" IN (SELECT U0."Preference" 
            FROM "userpreference_userpreference" U0 WHERE U0."user_id" = 5))
            '''
            filtered_news = news_objects.filter(category__in=user_preferencies)
            context = dict()
            context['filtered_news'] = filtered_news
            context['SITE_URL'] = settings.SITE_URL
            context['user_id'] = user.id

            subject = "Latest news update"
            html = render_to_string('news/email_template.html', context)

            # Call email thread to send an email
            EmailThread(subject, html, [user.email]).start()

            # It will mark is_notified flag as True.
            NewsAuthenticity.objects.filter(news__in=news_objects).update(is_notified=True)


        return "success"
    except Exception as e:
        print(e)


    print("working!")
    


@task
def do_work(self, list_of_work, progress_observer):
    total_work_to_do = len(list_of_work)
    for i, work_item in enumerate(list_of_work):
        do_work_item(work_item)
        # tell the progress observer how many out of the total items we have processed
        progress_observer.set_progress(i, total_work_to_do)
    return 'work is complete'