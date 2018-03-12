from django.conf.urls import url, patterns
from django.contrib import admin
from django.conf.urls import include

from django.contrib import admin
admin.autodiscover()
app_name ='polls'
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^polls/', 'polls.views.index',name='index'),

)
