from django.shortcuts import render
from .models import PetModel, PetImageModel, FA
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView

@login_required
def full(request):
	return render(request, 'front/full.html',{})

@login_required
def index(request):
	return render(request, 'front/index.html',{"isIndex":True, "currPage":"index"})

@login_required
def pets(request):
	pets = PetModel.objects.all()
	categ = PetModel.CATEG_CH
	sex =PetModel.SEX_CH
	okch = PetModel.OKCH
	return render(request, 'front/pets.html', {'categchoices':categ, 'sexchoices':sex, 'okchoices':okch, 'allpets': pets, "currPage":"pets"})

def  PetDetailView(request, pk):
	try:
		pet=PetModel.objects.get(pk=pk)
		petPhotos=pet.PetPhotos
		print(petPhotos)
	except PetModel.DoesNotExist:
		raise Http404("Cet animal n'est pas référencé")

	return render(request, 'front/detail_pet.html', context={'object':pet,'photos':petPhotos})


@login_required
def add_pet(request):
	return render(request, 'front/form_pet.html',{"currPage":"pets"})

@login_required
def fa(request):
	fa = FA.objects.all()
	return render(request, 'front/fa.html', {"allfa": fa,"currPage":"fa"})

@login_required
def add_fa(request):
	return render(request, 'front/form_fa.html',{"currPage":"fa"})