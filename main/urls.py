from django.urls import path
from . import views

urlpatterns = [
    path('about', views.about),  #переход на страницу о нас
    #path('post_video', views.post_video),
    path('', views.show_video, name='show_video') #главная страница
]
