from django.conf.urls import patterns, include, url
from django.contrib import admin

from gallery.views import main_view, upload_view, add_picture
from gallery.views import err_view, detail_view, delete_view

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pygallery.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', main_view, name="main_view"),
    url(r'^upload/', upload_view, name="upload_view"),
    url(r'^addpicture/', add_picture, name="add_picture"),
    url(r'^detail/(?P<id>[0-9]+)/$', detail_view, name="detail_view"),
    url(r'^delete/(?P<id>[0-9]+)/$', delete_view, name="delete_view"),
    url(r'^err/', err_view, name="err"),
)
