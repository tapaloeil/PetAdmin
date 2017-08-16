from django import forms
from .models import PetModel, PetImageModel, FA


class PetForm(forms.ModelForm):
    class Meta:
        model=PetModel
        fields=[
            "Category",
            "PetName",
            "Sex",
            "BirthDt",
            "City",
            "Departement",
            "OK_CHAT",
            "OK_CHIEN",
            "OK_ENFANT",
            "FA",
            "Description",
            "Status"
        ]
        widgets = {
            'BirthDt': forms.DateInput(attrs={'type': 'date'})
        }

class PetPhotoUpload(forms.ModelForm):
    class Meta:
        model=PetImageModel
        fields=[
            "Image"
        ]

class FAForm(forms.ModelForm):
    class Meta:
        model=FA
        fields=[
            "Nom",
            "Prenom",
            "Adresse",
            "Adresse2",
            "CP",
            "Ville",
            "Pays",
            "Telephone",
            "Telephone2",
            "TypeMaison",
            "TailleMaison",
            "OK_CHAT",
            "OK_CHIEN"
        ]
