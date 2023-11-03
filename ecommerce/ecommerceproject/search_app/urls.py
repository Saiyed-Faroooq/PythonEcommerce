from django.urls import path, include
from .import views
from django.conf import settings

app_name = 'search_app'

urlpatterns = [
    path('', views.searchresult, name='searchresult'),
]
