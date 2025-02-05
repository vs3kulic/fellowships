# filepath: /Users/vajosekulic/Documents/Programming/Fellowships/Fellowships/urls.py
from django.contrib import admin
from django.urls import path
from Fellowships import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('select_character/', views.select_character, name='select_character'),
    path('opponent_selected/', views.opponent_selected, name='opponent_selected'),
    path('coin_toss/', views.coin_toss, name='coin_toss'),
]