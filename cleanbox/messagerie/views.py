from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import ConnexionForm
from django.contrib.auth import authenticate, login, logout
from .models import Message


def accueil(request):
    return render(request, 'messagerie/accueil.html')
def connexion(request):
    if request.method == "POST":
        form = ConnexionForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return render(request, 'messagerie/dashboard.html', {'user': request.user})
 # Redirige vers page d'accueil ou dashboard
            else:
                messages.error(request, "Nom d'utilisateur ou mot de passe incorrect.")
    else:
        form = ConnexionForm()
    return render(request, 'messagerie/connexion.html', {'form': form})



def inscription(request):
    if request.method == 'POST':
        print("POST reçu :", request.POST)  # Debug
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            messages.error(request, "Les mots de passe ne correspondent pas.")
            print("Erreur : mots de passe différents")  # Debug
            return redirect('inscription')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Nom d'utilisateur déjà utilisé.")
            print("Erreur : username déjà utilisé")  # Debug
            return redirect('inscription')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Adresse email déjà utilisée.")
            print("Erreur : email déjà utilisé")  # Debug
            return redirect('inscription')

        user = User.objects.create_user(username=username, email=email, password=password1)
        user.save()
        messages.success(request, "Compte créé avec succès.")
        print("Utilisateur créé")  # Debug

        return redirect('connexion')

    print("Méthode GET")  # Debug
    return render(request, 'messagerie/inscription.html')

# Vue pour le dashboard utilisateur
@login_required
def dashboard(request):
    return render(request, 'dashboard.html', {'user': request.user})

def historique_connexions(request):
    return render(request, 'messagerie/historique_connexions.html')


def nouveau_message(request):
    if request.method == 'POST':
        destinataire_username = request.POST.get('destinataire')
        contenu = request.POST.get('contenu')
        # Vérifier que le destinataire existe
        try:
            destinataire = User.objects.get(username=destinataire_username)
        except User.DoesNotExist:
            messages.error(request, "Le destinataire n'existe pas.")
            return render(request, 'nouveau_message.html')
        # Ici tu appelles ta fonction / modèle anti-phishing pour analyser `contenu`
        est_phishing = detect_phishing(contenu)  # à créer selon ton modèle
        if est_phishing:
            messages.error(request, "Message détecté comme phishing, envoi refusé.")
            return render(request, 'nouveau_message.html')

        # Sinon, on crée et sauvegarde le message
        Message.objects.create(
            expediteur=request.user,
            destinataire=destinataire,
            contenu=contenu
        )
        messages.success(request, "Message envoyé avec succès.")
        return redirect('inbox')  # ou une page d'accueil messages

    return render(request, 'nouveau_message.html')

def detect_phishing(texte):
    # ici tu mets l'appel à ton modèle, exemple simplifié
    # retourne True si phishing détecté, sinon False
    # Pour l'instant, on simule toujours False (pas phishing)
    return False
def fichiers_scannes(request):
    # Affiche l'historique des fichiers scannés
    return render(request, 'messagerie/fichiers_scannes.html')

def parametres(request):
    # Permet à l'utilisateur de modifier ses paramètres (email, mot de passe, etc.)
    return render(request, 'messagerie/parametre_compte.html')

def deconnexion(request):
    # Déconnecte l'utilisateur et redirige vers la page de connexion
    return redirect('connexion')
def  nouveau_message(request):
    return render(request, 'messagerie/nouveau_message.html')

def  messages_envoyes(request):
    return render(request, 'messagerie/messages_envoyes.html')
def dashboard(request):
    return render(request, 'messagerie/dashboard.html', {'user': request.user})

   





