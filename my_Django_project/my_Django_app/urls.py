from django.urls import path
from . import views

urlpatterns = [
    #path('', views.index, name='index'),
    path('', views.main),
    path('about', views.about),
    path('fstring', views.fstring),
    path('test', views.test),
    path('chat', views.chat_view, name='chat_view'),
    path('stat', views.stat),
]