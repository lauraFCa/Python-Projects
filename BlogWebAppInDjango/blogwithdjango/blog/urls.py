from django.urls import path
from . import views   # import all views from the app

urlpatterns = [
    path('', views.post_list, name='post_list'),
]
