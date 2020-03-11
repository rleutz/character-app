from django.shortcuts import render, get_object_or_404
from .models import Character, CharacterData

def character_filter(request):
    characters = Character.objects.filter(player=self.owner).order_by('slug')
    return render(request, 'character/character_list.html', {'characters': characters})

def character_list(request):
    characters = Character.objects.all().order_by('slug')
    return render(request, 'character/character_list.html', {'characters': characters})

def character_detail(request, pk):
    character = Character.objects.get(pk=pk)

    charlist = CharacterData.objects.filter(data_type_category='Character', character_id=pk)
    for d in charlist:
        if(d.data_type_name == 'Alliance'):
            calliancetag = d.data_type_name
            calliance = d.data_value
        if(d.data_type_name == 'Class'):
            cclasstag = d.data_type_name
            cclass = d.data_value
        if(d.data_type_name == 'Gender'):
            cgendertag = d.data_type_name
            cgender = d.data_value
        if(d.data_type_name == 'Health'):
            chealthtag = d.data_type_name
            chealth = d.data_value
        if(d.data_type_name == 'Level'):
            cleveltag = d.data_type_name
            clevel = d.data_value
        if(d.data_type_name == 'Magicka'):
            cmagickatag = d.data_type_name
            cmagicka = d.data_value
        if(d.data_type_name == 'Race'):
            cracetag = d.data_type_name
            crace = d.data_value
        if(d.data_type_name == 'Stamina'):
            cstaminatag = d.data_type_name
            cstamina = d.data_value
        if(d.data_type_name == 'Slug'):
            cnametag = d.data_type_name
            cname = d.data_value

    list = CharacterData.objects.exclude(data_type_category = 'Character').filter(character_id=pk)
    # name = CharacterData.objects.get(character_id=pk, data_type_name='Slug')
    return render(request, 'character/character_detail.html', {'calliance': calliance, 'calliancetag': calliancetag, 'cname': cname, 'cnametag': cnametag, 'cclass': cclass, 'cclasstag': cclasstag, 'cgender': cgender, 'cgendertag': cgendertag, 'chealth': chealth, 'chealthtag': chealthtag, 'clevel': clevel, 'cleveltag': cleveltag, 'cmagicka': cmagicka, 'cmagickatag': cmagickatag, 'crace': crace, 'cracetag': cracetag, 'cstamina': cstamina, 'cstaminatag': cstaminatag, 'character': character, 'cname': cname, 'list': list, 'charlist': charlist})
