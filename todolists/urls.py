from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
	url(r'^all/$', 'todolists.views.todolist'),
	url(r'^all/(?P<stat>\d+)/$', 'todolists.views.todolist'),
	url(r'^all/(?P<stat>\d+)/(?P<dfrom>\w+)/(?P<dto>\w+)/$', 'todolists.views.todolist'),
	url(r'^all/(?P<stat>\d+)/(?P<dfrom>\w+)/(?P<dto>\w+)/(?P<range>\w+)/$', 'todolists.views.todolist'),
	url(r'^todo/(?P<todo_id>\d+)/$', 'todolists.views.todo'),
	url(r'^create/$','todolists.views.create'),
	url(r'^cancel/(?P<todo_id>\d+)/$', 'todolists.views.cancel_todo'),
	url(r'^finish/(?P<todo_id>\d+)/$', 'todolists.views.finish_todo'),
)
