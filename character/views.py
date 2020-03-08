from django.shortcuts import render

def character_list(request):
    return render(request, '/character/character_list.html', {})
