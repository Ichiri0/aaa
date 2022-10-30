from django.urls import path

from taskmanager import settings
from  . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('catalog', views.catalog, name='catalog'),
    path('add_user', views.add_user, name='add_user'),
    path('free_records', views.free_records, name='free_records_default'),
]

