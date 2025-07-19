from django.shortcuts import render
from django.shortcuts import render, redirect

from django.contrib import messages
from django.contrib.auth.decorators import login_required

def accueil(request):
    return render(request, 'messagerie/accueil.html')
def connexion(request):
    return render(request, 'messagerie/connexion.html')
def inscription(request):
    return render(request, 'messagerie/inscription.html')


# Vue pour le dashboard utilisateur
#@login_required
def dashboard(request):
    return render(request, 'messagerie/dashboard.html')

def historique_connexions(request):
    return render(request, 'messagerie/historique_connexions.html')
def messages_envoyes(request):
    # Affiche la liste des messages déjà envoyés
    return render(request,'messagerie/messages_envoyes.html')

def fichiers_scannes(request):
    # Affiche l'historique des fichiers scannés
    return render(request, 'messagerie/fichiers_scannes.html')

def parametres(request):
    # Permet à l'utilisateur de modifier ses paramètres (email, mot de passe, etc.)
    return render(request, 'messagerie/parametre_compte.html')

def deconnexion(request):
    # Déconnecte l'utilisateur et redirige vers la page de connexion
    return redirect('connexion')


   





