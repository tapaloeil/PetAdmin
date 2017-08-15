from django import forms
from .models import PetModel, PetImageModel


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
            "Description"
        ]

class PetPhotoUpload(forms.ModelForm):
    class Meta:
        model=PetImageModel
        fields=[
            "Pet",
            "Image"
        ]