from django.urls import path

from . import views

urlpatterns = [
    path('accueil/', views.index, name='index'),
    path('contact', views.afficheDuo, name='contact'),
    path('resolve', views.afficheDuo, name='resolve'),
    path('', views.index, name='index'),
]
