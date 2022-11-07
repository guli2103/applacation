
from django.contrib import admin
from django.urls import path
from core.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('moshin1', moshin1),
    path('moshin2', moshin2),
    path('moshin3', moshin3),
    path('moshin4', moshin4),
    path('moshin5', moshin5),
    path('moshin6', moshin6)
]
