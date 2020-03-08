from django.shortcuts import render, get_object_or_404
from .models import Character, CharacterData

def character_list(request):
    characters = Character.objects.all().order_by('slug')
    return render(request, 'character/character_list.html', {'characters': characters})

def character_detail(request, pk):
    # c = get_object_or_404(Character, pk=pk)
    character = c.characterdata_set.filter(pk=pk)
    return render(request, 'character/character_detail.html', {'character': character})
