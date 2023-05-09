from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
    return render(request, 'generator/home.html', {'password':'helloworld'})
def generatedPassword(request):
    generated_password = ''
    characters = list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()[]{};:,./<>?'))
    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))
    length = int(request.GET.get('length',12)) #12 is the default value
    for x in range(length):
        generated_password += random.choice(characters) #randomly choose a character from the list
    return render(request, 'generator/password.html', {'password':generated_password})
def about(request):
    return render(request, 'generator/about.html')