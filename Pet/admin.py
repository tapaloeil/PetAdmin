from django.contrib import admin
from .models import PetModel, PetImageModel
from jet.admin import CompactInline
# Register your models here.

class PetImageModelAdmin(admin.StackedInline):
	model=PetImageModel

class PetModelAdmin(admin.ModelAdmin):
	list_display=("Name","Category","Sex","BirthDt","City","Departement","Status")
	list_filter=("Category","Sex", "City", "Departement", "Status")
	fieldsets=(
		(None,{
			'fields':('Name', 'Category', 'Sex',('BirthDt'),'City','Departement','OK_CHAT','OK_CHIEN','OK_ENFANT','Status')
		}),
		('Description',{
			'fields':('Description',),
			}),
		)
	inlines=(PetImageModelAdmin,)

admin.site.register(PetModel,PetModelAdmin)