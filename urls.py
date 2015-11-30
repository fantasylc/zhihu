from django.conf.urls import url, patterns

urlpatterns = patterns('zhihu.views',
                       url(r'^answerall/$', 'zhindex', name='index'),
                       url(r'^answer/(?P<id>\d+)/$', 'answer', name='answer'),
                       )
