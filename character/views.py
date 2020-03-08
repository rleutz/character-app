from django.shortcuts import render
from .models import Character, CharacterData

def character_list(request):
    characters = Character.objects.all().order_by('slug')
    return render(request, 'character/character_list.html', {})
