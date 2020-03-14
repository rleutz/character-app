from django import forms

from .models import Character

class CharacterForm(forms.ModelForm):

    class Meta:
        model = Character
        fields = ('slug', 'character_main', 'mule_for', 'notes', 'image')
