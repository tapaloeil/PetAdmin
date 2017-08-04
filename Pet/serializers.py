from rest_framework import serializers
from .models import PetModel, FA
from datetime import date,datetime,timedelta
from django.utils import timezone

class PetSerial(serializers.ModelSerializer):
	class Meta:
		model=PetModel
		fields=(
			"Category",
			"Name",
			"Sex",
			"BirthDt",
			"City",
			"Departement",
			"Statut",
			"OK_CHAT",
			"OK_CHIEN",
			"OK_ENFANT",
			"FA"
			)

	def create(self, validated_data):
		return PetModel.objects.create(**validated_data)

	def update(self, instance, validated_data):
		instance.Category=validated_data.get("Category", instance.Category)
		instance.Name=validated_data.get("Name", instance.Name)
		instance.Sex=validated_data.get("Sex", instance.Sex)
		instance.BirthDt=validated_data.get("BirthDt", instance.BirthDt)
		instance.City=validated_data.get("City", instance.City)
		instance.Departement=validated_data.get("Departement", instance.Departement)
		instance.Statut=validated_data.get("Statut", instance.Statut)
		instance.OK_CHAT=validated_data.get("OK_CHAT", instance.OK_CHAT)
		instance.OK_CHIEN=validated_data.get("OK_CHIEN", instance.OK_CHIEN)
		instance.OK_ENFANT=validated_data.get("OK_ENFANT", instance.OK_ENFANT)
		instance.save()
		return instance