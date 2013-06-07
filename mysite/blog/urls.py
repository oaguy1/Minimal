from django.conf.urls import patterns, url
from blog import views

urlpatterns = patterns('',
            url(r'^$', views.index, name='index'),
            # url(r'^login/$', views.login, name='login'),
            url(r'^(?P<post_year>\d+)/(?P<post_month>\d+)/(?P<post_day>\d+)/(?P<post_slug>\w+)/$', views.post, name='post'),
            )
