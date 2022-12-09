from django.shortcuts import render
from django.http import HttpResponse
import random
import string


def home(request):
    return render(request, 'generator/main.html', {'title': 'Password generator'})


def password(request):
    characters = string.ascii_lowercase

    if request.GET.get('Uppercase'):
        characters = string.ascii_letters

    if request.GET.get('Numbers'):
        characters += string.digits

    if request.GET.get('SpecialCharacter'):
        characters += string.punctuation

    length = int(request.GET.get('length', 8))
    result = ''

    for i in range(length):
        result += random.choice(characters)

    return render(request, 'generator/password.html', {'title': 'Generated', 'password': result})


def aboutme(request):
    return render(request, 'generator/aboutme.html', {'tittle': 'About me'})
