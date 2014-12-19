from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
	url(r'^all/$', 'cs260.views.todolist'),
)
