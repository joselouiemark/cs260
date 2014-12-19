from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	# Examples:
	url(r'^$', 'cs260.views.login'),
	url(r'^accounts/login/$', 'cs260.views.login'),
	url(r'^accounts/register/$', 'cs260.views.register_user'),
	# url(r'^blog/', include('blog.urls')),

	url(r'^admin/', include(admin.site.urls)),
)

