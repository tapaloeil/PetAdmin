import datetime
from django.db import models
from django.utils import timezone
from tinymce.models import HTMLField
from filer.fields.image import FilerImageField
from model_utils.models import TimeStampedModel
from django.utils.timezone import now



class FA (TimeStampedModel):
	OKCH=(
		("Y","Oui"),
		("N","Non"),
		("U","Je ne sais pas")
	)
	Nom=models.CharField(max_length=100, verbose_name="Nom")
	Prenom=models.CharField(max_length=100, verbose_name="Prénom")
	Adresse=models.CharField(max_length=100, verbose_name="Adresse", blank=True, null=True)
	Adresse2=models.CharField(max_length=100, verbose_name="Adresse 2", blank=True, null=True)
	CP=models.CharField(max_length=10, verbose_name="CP", blank=True, null=True)
	Ville=models.CharField(max_length=100, verbose_name="Ville")
	PaysCH=(
		("France","France"),
		("Belgique","Belgique"),
		("Suisse","Suisse"),
		("Espagne","Espagne")
	)
	Pays=models.CharField(max_length=100, choices=PaysCH, verbose_name="Pays", default="France")
	Telephone=models.CharField(max_length=15, verbose_name="Téléphone", blank=True, null=True)
	Telephone2=models.CharField(max_length=15, verbose_name="Téléphone 2", blank=True, null=True)
	MaisonCH=(
		("Maison", "Maison"),
		("Appartement", "Appartement")
		)
	TypeMaison=models.CharField(max_length=30, choices=MaisonCH,verbose_name="Type habitation", default="Maison")
	TailleMaison=models.PositiveSmallIntegerField(verbose_name="Taille de l'habitation en m²", blank=True, null=True)
	OK_CHAT=models.CharField(max_length=1, choices=OKCH, default="U", verbose_name="OK Chat ?")
	OK_CHIEN=models.CharField(max_length=1, choices=OKCH, default="U", verbose_name="OK Chien ?")

	def __str__(self):
		return "%s %s | %s | %s" % (self.Prenom, self.Nom, self.CP, self.Telephone)

	def get_absolute_url(self):
		return "/fa/%i" % self.id

	class Meta:
		verbose_name="Famille d'accueil"
		verbose_name_plural="Familles d'accueil"

class PetModel(TimeStampedModel):
	OKCH=(
		("Y","Oui"),
		("N","Non"),
		("U","Je ne sais pas")
	)
	CATEG_CH=(
		("Chien","Chien"),
		("Chat","Chat")
		)
	Category = models.CharField(max_length=30, choices=CATEG_CH, default="Chat", verbose_name="Catégorie")
	PetName = models.CharField(max_length=200, verbose_name="Nom	")
	Description = HTMLField(blank=True, null=True, verbose_name='Description')
	SEX_CH=(
		("M", "Mâle"),
		("F", "Femelle")
	)
	Sex = models.CharField(max_length=30, choices=SEX_CH, default="M", verbose_name='Sexe')
	BirthDt=models.DateField(default=datetime.date.today, verbose_name="Date de naissance")
	City=models.CharField(max_length=100, verbose_name="Ville")
	Departement=models.CharField(max_length=3, verbose_name="Département")
	STATUS_CH=(
		("A adopter", "A adopter"),
		("Adopté", "Adopté"),
		("Caché", "Caché")
	)
	Status=models.CharField(max_length=30, choices=STATUS_CH, default="A adopter")
	OK_CHAT=models.CharField(max_length=1, choices=OKCH, default="U", verbose_name="OK Chat ?")
	OK_CHIEN=models.CharField(max_length=1, choices=OKCH, default="U", verbose_name="OK Chien ?")
	OK_ENFANT=models.CharField(max_length=1, choices=OKCH, default="U", verbose_name="OK Enfants ?")
	FA=models.ForeignKey(FA, verbose_name="Famille d'accueil", blank=True, null=True)

	class Meta:
		verbose_name='Animal'
		verbose_name_plural="Animaux"

	def get_absolute_url(self):
		return "/animal/%i" % self.id

class PetImageModel(TimeStampedModel):
	Pet=models.ForeignKey(PetModel, related_name='PetPhotos')
	Image= models.ImageField(upload_to = 'pictures/%y%m%d')

