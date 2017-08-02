from django.shortcuts import render
from .models import PetModel
from django.utils import timezone
from django.contrib.auth.decorators import login_required

@login_required
def full(request):
	return render(request, 'front/full.html',{})

@login_required
def index(request):
	return render(request, 'front/index.html',{})

@login_required
def pets(request):
	pets = PetModel.objects.all()
	return render(request, 'front/pets.html', {'allpets': pets})