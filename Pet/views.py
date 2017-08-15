from django.shortcuts import render
from .models import PetModel, PetImageModel, FA
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView
from .forms import PetForm, PetPhotoUpload
from django.http import HttpResponseRedirect

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

def PetCreate(request):
	form=PetForm(request.POST or None)
	if form.is_valid():
		pet=form.save(commit=False)
		pet.save()
		return HttpResponseRedirect(pet.get_absolute_url())
	return render (request, "front/form_pet.html", {"form":form})

def  PetDetailView(request, pk):
	try:
		pet=PetModel.objects.get(pk=pk)
		form=PetForm(request.POST or None, instance=pet)
		if form.is_valid():
			pet=form.save(commit=False)
			pet.save()
			return HttpResponseRedirect(pet.get_absolute_url())
		formPhotos=PetPhotoUpload(request.POST or None, initial={"Pet":pet})
		if formPhotos.is_valid():
			photo=form.save(commit=False)
			photo.save()
			return HttpResponseRedirect(pet.get_absolute_url())
	except PetModel.DoesNotExist:
		raise Http404("Cet animal n'est pas référencé")

	return render(request, 'front/detail_pet.html', context={'object':pet, 'form':form, 'formPhoto':formPhotos})

def PetImageUpload(request):
	if request.method=="POST":
		form=PetPhotoUpload(request.POST, request.FILES)
		if form.is_valid():
			form.save()
	else:
		form=PetPhotoUpload()
	return render(request, "front/upload_photo.html", {"form":form})

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