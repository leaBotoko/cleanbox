from django.urls import path
from . import views
urlpatterns =[
    path('accueil/', views.accueil, name='accueil'),
    path('connexion/', views.connexion, name='connexion'),
    path('inscription/', views.inscription, name='inscription'),
    path('dashboard/', views.dashboard, name='dashboard'),
    #path('nouveau_message/', views.nouveau_message, name='nouveau_message'),
    path('historiques_connexion/', views.historique_connexions, name='historiques_connexion'),
    path('dashboard/', views.dashboard, name='dashboard'),  # Tableau de bord
    path('messages_envoyes/', views.messages_envoyes, name='messages_envoyes'),  # Liste Messages envoyés
    path('fichiers_scannes/', views.fichiers_scannes, name='fichiers_scannes'),  # Historique des fichiers scannés
    path('parametre_compte/', views.parametres, name='parametres'),  # Page Paramètres du compte
    path('deconnexion/', views.deconnexion, name='deconnexion'),  # Déconnexion
]

    