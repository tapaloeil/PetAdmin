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
        widgets = {
            'BirthDt': forms.DateInput(attrs={'type': 'date'})
        }

class PetPhotoUpload(forms.ModelForm):
    Image=forms.FileField()
    class Meta:
        model=PetImageModel
        fields=[
            "Pet",
            "Image"
        ]