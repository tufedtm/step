from django.conf.urls import include, url

urlpatterns = [
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^$', 'main.views.get_users', name='get_users')
]
