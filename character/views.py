from django.shortcuts import render, get_object_or_404
from .models import Character, CharacterData

def character_list(request):
    characters = Character.objects.all().order_by('slug')
    return render(request, 'character/character_list.html', {'characters': characters})

def character_detail(request, pk):
    character = Character.objects.get(pk=pk)
    charlist = CharacterData.objects.exclude(data_type_name='Slug').filter(data_type_category='Character', character_id=pk)
    list = CharacterData.objects.exclude(data_type_category = 'Character').filter(character_id=pk)
    name = CharacterData.objects.get(character_id=pk, data_type_name='Slug')
    return render(request, 'character/character_detail.html', {'character': character, 'name': name, 'list': list, 'charlist': charlist})
