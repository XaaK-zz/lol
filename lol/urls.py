from django.conf.urls import patterns, url

urlpatterns = patterns('lol.views',
    url(r'^$', 'index', name='index'),
    url(r'^upload/$', 'upload', name='upload'),
    url(r'^upload/new$', 'new', name='new'),
    url(r'^rate/(?P<snippet_id>\d+)$', 'rate', name='rate'),
)
