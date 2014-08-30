from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'personal.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    #Urls para projects
    url(r'^$', 'projects.views.project_view', name='project_view'),
    url(r'^project/(?P<title>[\w\-\W]+)/', 'projects.views.project_view_detail', name='project_view_detail'),

       
)
urlpatterns += patterns('',
    url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT}),
)

