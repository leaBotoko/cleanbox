from django.db import models
from django.contrib.auth.models import User

# Historique des connexions
class HistoriqueConnexion(models.Model):
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)
    date_connexion = models.DateTimeField(auto_now_add=True)
    adresse_ip = models.GenericIPAddressField()

    def __str__(self):
        return f"{self.utilisateur.username} - {self.date_connexion} - {self.adresse_ip}"

# Messages envoyés
class Message(models.Model):
    expediteur = models.ForeignKey(User, on_delete=models.CASCADE)
    destinataire = models.ForeignKey(User, related_name='messages_recus', on_delete=models.CASCADE)
    objet = models.CharField(max_length=255)
    contenu = models.TextField()
    date_envoi = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.expediteur.username} → {self.destinataire} : {self.objet}"

# Fichiers scannés
class FichierScanne(models.Model):
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)
    nom_fichier = models.CharField(max_length=255)
    statut = models.CharField(max_length=50)  # Exemple : "Sain" ou "Malware détecté"
    date_scan = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nom_fichier} - {self.statut}"
