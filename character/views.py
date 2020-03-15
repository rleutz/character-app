from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from django.views.generic.list import ListView
from .models import Character, CharacterData, UrlTable
import feedparser
from .forms import CharacterForm, UrlForm


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
        context['feed'] = feedparser.parse("https://www.elderscrollsonline.com/en-us/rss/news/")
        return context

# List of all characters
class character_list_view(ListView):
    template_name = 'character_list.html'
    model = Character

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['owner'] = self.request.GET.get('owner')
        context['feed'] = feedparser.parse("https://www.elderscrollsonline.com/en-us/rss/news/")
        return context

class url_list_view(ListView):
    template_name = "character/url_list.html"
    model = UrlTable

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

def url_new(request):
    if request.method == "POST":
        form = UrlForm(request.POST)
        if form.is_valid():
            url = form.save(commit=False)
            url.published_date = timezone.now()
            url.save()
            return redirect('url_list')

    form = UrlForm()
    return render(request, 'character/url_edit.html', {'form': form})

def url_detail(request, pk):
    url = get_object_or_404(UrlTable, pk=pk)
    return render(request, 'character/url_detail.html', {'url': url})

def url_edit(request, pk):
    url = get_object_or_404(UrlTable, pk=pk)
    if request.method == "POST":
        form = UrlForm(request.POST, instance=url)
        if form.is_valid():
            url = form.save(commit=False)
            url.save()
            return redirect('url_list')
    else:
        form = UrlForm(instance=url)
    return render(request, 'character/url_edit.html', {'form': form})



def character_detail(request, pk):
    character = Character.objects.get(pk=pk)

    list = CharacterData.objects.exclude(data_type_category = 'Character').filter(character_id=pk)
    for v in list:
        if(v.value_is_number == True):
            v.data_value=int(v.data_value)
    # name = CharacterData.objects.get(character_id=pk, data_type_name='Slug')
    return render(request, 'character/character_detail.html', {'character': character, 'list': list})

def character_edit(request, pk):
    character = get_object_or_404(Character, pk=pk)
    if request.method == "POST":
        form = CharacterForm(request.POST, request.FILES, instance=character)
        if form.is_valid():
            character = form.save(commit=False)
            character.save()
            return redirect('character_detail', pk=character.pk)
    else:
        form = CharacterForm(instance=character)
    return render(request, 'character/character_edit.html', {'form': form})
