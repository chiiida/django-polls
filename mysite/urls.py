from django.conf.urls import handler404, handler500
from django.contrib import admin
from django.urls import include, path

import mysite.views

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
    path('', mysite.views.index),
] 

# handler404 = 'polls.views.error_404_view'