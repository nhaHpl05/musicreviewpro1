from django.urls import path
from . import views
from . import models

urlpatterns = [
    path('',views.index, name='index'),
    path('getSongs/', views.getSong, name='songs'),
    url(r'^ratings/', include('star_ratings.urls', namespace='ratings', app_name='ratings')),
]
