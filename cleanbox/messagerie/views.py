from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import InscriptionForm
from django.contrib import messages

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





