import datetime
from django.db import models
from django.utils import timezone
from tinymce.models import HTMLField
from filer.fields.image import FilerImageField
from model_utils.models import TimeStampedModel
from django.utils.timezone import now

class PetModel(TimeStampedModel):
    CATEG_CH=(
        ("Chien","Chien"),
        ("Chat","Chat")
        )
    Category = models.CharField(max_length=30, choices=CATEG_CH, default="Chat", verbose_name="Catégorie")
    Name = models.CharField(max_length=200, verbose_name="Nom de l'animal")
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
    OKCH=(
        ("Y","Oui"),
        ("N","Non"),
        ("U","Je ne sais pas")
    )
    OK_CHAT=models.CharField(max_length=1, choices=OKCH, default="U", verbose_name="OK Chat ?")
    OK_CHIEN=models.CharField(max_length=1, choices=OKCH, default="U", verbose_name="OK Chien ?")
    OK_ENFANT=models.CharField(max_length=1, choices=OKCH, default="U", verbose_name="OK Enfants ?")

class PetImageModel(TimeStampedModel):
    Pet=models.ForeignKey(PetModel, verbose_name='Animal')
    Image= FilerImageField(related_name="photos")