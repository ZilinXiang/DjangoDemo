from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.demo, name='demo'),
    re_path(r'^test$', views.test),
]