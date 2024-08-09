from django.shortcuts import render
from django.http import HttpResponse
import random


def home(request):
    return render(request, 'generator/home.html')

def about(request):
    return render(request, 'generator/about.html')
def password(request):
    thePassword = ''
    lower_characters = list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('upperCase'):
        lower_characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        lower_characters.extend(list('!@#$%^&*()'))
    if request.GET.get('numbers'):
        lower_characters.extend(list('123456789'))
    length = int(request.GET.get('length', 12))
    for x in range(length):
        thePassword += random.choice(lower_characters)
    return render(request, 'generator/password.html', {'password': thePassword})
