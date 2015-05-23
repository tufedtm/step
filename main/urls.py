from django.conf.urls import include, url

urlpatterns = [
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^$', 'main.views.index', name='index'),

    url(r'^profile/(?P<user_id>[\d]+)$', 'main.views.profile', name='profile'),
    url(r'^profile/edit$', 'main.views.profile_edit', name='profile_edit'),
    url(r'^profile/users$', 'main.views.profiles', name='users'),
]