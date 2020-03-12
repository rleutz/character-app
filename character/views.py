from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView
from django.db.models.functions import Cast
from .models import Character, CharacterData

# List of characters by filter
class character_filter_view(ListView):
    template_name = 'character_list.html'
    model = Character

    def get_queryset(self, **kwargs):
        self.owner = self.request.GET.get('owner')
        return Character.objects.filter(player=self.owner)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['owner'] = self.request.GET.get('owner')
        return context

# List of all characters
class character_list_view(ListView):
    template_name = 'character_list.html'
    model = Character

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['owner'] = self.request.GET.get('owner')
        return context

# def character_list(request):
#     characters = Character.objects.all().order_by('slug')
#     return render(request, 'character/character_list.html', {'characters': characters})

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
    for v in list:
        if(v.value_is_number == True) {
            v.data_value=Cast('integer', v.data_value)
        }
    # name = CharacterData.objects.get(character_id=pk, data_type_name='Slug')
    return render(request, 'character/character_detail.html', {'calliance': calliance, 'calliancetag': calliancetag, 'cname': cname, 'cnametag': cnametag, 'cclass': cclass, 'cclasstag': cclasstag, 'cgender': cgender, 'cgendertag': cgendertag, 'chealth': chealth, 'chealthtag': chealthtag, 'clevel': clevel, 'cleveltag': cleveltag, 'cmagicka': cmagicka, 'cmagickatag': cmagickatag, 'crace': crace, 'cracetag': cracetag, 'cstamina': cstamina, 'cstaminatag': cstaminatag, 'character': character, 'cname': cname, 'list': list, 'charlist': charlist})
