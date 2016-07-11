from django.conf.urls import patterns, url, include
from rango import views
from django.contrib.auth import admin
#from django.conf import settings #media


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tango_with_django_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
    #url(r'^rango/', include('rango.urls')),
    url(r'^$', views.index, name='index'),
    url(r'^about/', views.about, name='about'),

)

# UNDERNEATH your urlpatterns definition, add the following two lines:
'''if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'^media/(?P<path>.*)',
        'serve',
        {'document_root': settings.MEDIA_ROOT}), )'''