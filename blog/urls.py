from django.conf.urls import patterns, include, url

from django.contrib import admin
from myblog import views
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
     #url(r'^$', 'myblog.views.home', name='home'),
    #url(r'^myblog/', include('blog.urls')),
    
    url(r'^admin/', include(admin.site.urls)),

    (r'^$', 'myblog.views.index'),
url(
    r'^blog/view/(?P<slug>[^\.]+).html', 
    'myblog.views.view_post', 
    name='view_blog_post'),
url(
    r'^blog/category/(?P<slug>[^\.]+).html', 
    'myblog.views.view_category', 
    name='view_blog_category'),
url(r'^post/new/$', views.post_new, name="newpost"),
)