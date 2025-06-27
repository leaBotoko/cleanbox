from django.urls import path
from . import views

urlpatterns = [
    path('accueil/', views.accueil, name='accueil'),
    path('connexion/', views.connexion, name='connexion'),
    path('inscription/', views.inscription, name='inscription'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('nouveau_message/', views.nouveau_message, name='nouveau_message'),
    path('historiques_connexion/', views.nouveau_message, name='historiques_connexion'),
    

]
