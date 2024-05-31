from django.db import models
from django.contrib.auth.models import User

class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_de_naissance = models.DateField()
    numero_telephone = models.CharField(max_length=20)
    adresse = models.CharField(max_length=200)

class Fournisseur(models.Model):
    nom = models.CharField(max_length=100)
    type_de_fournisseur = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)

class Produit(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField()
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    fournisseur = models.ForeignKey(Fournisseur, on_delete=models.CASCADE)

class Reservation(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    date_reservation = models.DateTimeField(auto_now_add=True)
    date_depart = models.DateField()
    date_retour = models.DateField()
    nombre_passagers = models.IntegerField()
    statut = models.CharField(max_length=20, default='En cours')
