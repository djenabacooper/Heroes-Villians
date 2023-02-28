from django.urls import path
from . import views

urlpatterns = [
    path('supers/',views.super_list),
]