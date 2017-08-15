from django.contrib import admin
from .models import PetModel, PetImageModel, FA
from jet.admin import CompactInline
# Register your models here.

class FAAdmin(admin.ModelAdmin):
	list_display=("Prenom","Nom", "Ville", "Telephone", "TailleMaison")
	list_filter=("Ville", "TypeMaison", "TailleMaison", "OK_CHAT","OK_CHIEN")

class PetImageModelAdmin(admin.StackedInline):
	model=PetImageModel

class PetModelAdmin(admin.ModelAdmin):
	list_display=("PetName","Category","Sex","BirthDt","City","Departement","Status")
	list_filter=("Category","Sex", "City", "Departement", "Status")
	fieldsets=(
		(None,{
			'fields':('PetName', 'Category', 'Sex',('BirthDt'),'City','Departement','OK_CHAT','OK_CHIEN','OK_ENFANT','Status', 'FA')
		}),
		('Description',{
			'fields':('Description',),
			}),
		)
	inlines=(PetImageModelAdmin,)

admin.site.register(PetModel,PetModelAdmin)
admin.site.register(FA, FAAdmin)