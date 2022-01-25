from django.urls import path, re_path

app_name = "news"


urlpatterns = [
	re_path(r'^(?P<task_id>[\w-]+)/$', views.get_progress, name='task_status')
]