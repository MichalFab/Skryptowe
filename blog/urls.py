from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from BlogApplication import views
urlpatterns = [
    url(r'^admin/', admin.site.urls, name='admin'),
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^category/(?P<pk>\d+)/$', views.category_post_list, name='category_post_list'),
    url(r'^about/$', views.about_text, name='about_text'),
    url(r'^search/$', views.search_posts, name='search_posts'),
    url(r'^top20/$', views.top_20_from_helion, name='top_20_from_helion'),
    url(r'^regex/$', views.regex, name='regex'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
