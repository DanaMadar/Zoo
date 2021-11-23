from django.shortcuts import render
import requests


# Create your views here.
def animal_view(request, animal_id):
    return render(request,  'animal.html' {'id' : animal_id})

def all_animals_view(request):
    return render(request, 'animals.html')