from django.shortcuts import render
from .models import PetModel, FA
from django.utils import timezone
from django.contrib.auth.decorators import login_required

@login_required
def full(request):
	return render(request, 'front/full.html',{})

@login_required
def index(request):
	return render(request, 'front/index.html',{"isIndex":True, "currPage":"index"})

@login_required
def pets(request):
	pets = PetModel.objects.all()
	return render(request, 'front/pets.html', {'allpets': pets, "currPage":"pets"})

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