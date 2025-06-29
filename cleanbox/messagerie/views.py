from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import InscriptionForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def inscription(request):
    if request.method == 'POST':
        form = InscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Votre compte a été créé avec succès ! Vous pouvez maintenant vous connecter.")
            return redirect('connexion')  # On redirige vers la page de connexion
    else:
        form = InscriptionForm()

    return render(request, 'messagerie/inscription.html', {'form': form})
def accueil(request):
    return render(request, 'messagerie/accueil.html')
def connexion(request):
    return render(request, 'messagerie/connexion.html')
from django.shortcuts import render


# Vue pour le dashboard utilisateur
#@login_required
def dashboard(request):
    return render(request, 'messagerie/dashboard.html')
def nouveau_message(request):
    if request.method == 'POST':
        destinataire = request.POST.get('destinataire')
        objet = request.POST.get('objet')
        contenu = request.POST.get('contenu')
        fichier = request.FILES.get('fichier')

        #  analyse  texte + analyser le fichier (malware / phishing)

        messages.success(request, "Message envoyé avec succès.")
        return redirect('nouveau_message')  # Redirection après envoi

    return render(request, 'messagerie/nouveau_message.html')

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



