from django.conf.urls import url, include
from . import views

urlpatterns = {
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^about/$', views.about_text, name='about_text'),
    url(r'^search/$', views.search_posts, name='search_posts'),
    url(r'^top20/$', views.top_20_from_helion, name='top_20_from_helion'),
    url(r'^regex/$', views.regex, name='regex'),


}