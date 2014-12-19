from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', 'scheduler.views.todolist'),
	
	url(r'^accounts/register/$', 'cs260.views.register_user'),
	url(r'^accounts/login/$', 'cs260.views.login'),
	url(r'^accounts/auth/$', 'cs260.views.auth_view'),
	url(r'^accounts/logout/$', 'cs260.views.logout'),
	url(r'^accounts/loggedin/$', 'cs260.views.loggedin'),
	url(r'^accounts/invalid/$', 'cs260.views.invalid_login'),
	url(r'^accounts/register/$', 'cs260.views.register_user'),
	url(r'^accounts/register_success/$', 'cs260.views.register_success'),

	#include todolists urls
	url(r'^todolists/', include('todolists.urls')),
	
	url(r'^admin/', include(admin.site.urls)),
)

