from django import forms
from .models import PetModel


class PetForm(forms.ModelForm):
    class Meta:
        model=PetModel
        fields=[
            "Name",
            "Category",
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