from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('parse_site/', parse_site, name='parse_site'),
    path('upload_db/', upload_db, name='upload_db'),
    path('download_from_db/', download_from_db, name='download_from_db'),
]
