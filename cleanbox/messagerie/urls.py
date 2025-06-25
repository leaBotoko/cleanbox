from django.urls import path
from . import views

urlpatterns = [
    path('accueil/', views.accueil, name='accueil'),
    path('connexion/', views.connexion, name='connexion'),
    path('inscription/', views.inscription, name='inscription'),
]
