from django.contrib import admin
from django.urls import path
from lotto import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', views.index),
    path('hello/', views.hello, name='hello_name'),
    path('lotto/', views.index, name='index'),
    path('lotto/new/', views.post, name='new_lotto'),
    path('lotto/<int:lottokey>/detail', views.detail, name='detail'),
]
