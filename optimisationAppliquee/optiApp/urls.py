from django.urls import path

from . import views

urlpatterns = [
    path('accueil/', views.index, name='index'),
    path('duo', views.afficheDuo, name='duo'),
    path('', views.index, name='index'),
    
]