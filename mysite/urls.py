from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('', views.index),
]

handler404 = 'polls.views.handler404'
