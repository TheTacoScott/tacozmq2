from django.conf.urls import include, url
from django.contrib import admin
import main.views

urlpatterns = [
    url(r'^$', 'main.views.index', name='index'),
    url(r'^admin/', include(admin.site.urls)),
]
