from django.urls import path

from . import views

urlpatterns = [
    path('accueil/', views.index, name='index'),
    path('contact', views.contact, name='contact'),
    path('resolve/', views.resolve, name='resolve'),
    path('resolve/solution', views.afficheSolution, name='solution'),
    path('', views.index, name='index'),
]
