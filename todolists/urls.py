from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
	url(r'^all/$', 'scheduler.views.todolist'),
)
