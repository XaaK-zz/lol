from django.conf.urls import patterns, url

urlpatterns = patterns('lol.views',
    url(r'^$', 'index'),
    url(r'^upload/$', 'upload'),
)
