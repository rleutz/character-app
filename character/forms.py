from django import forms

from .models import Character

class CharacterForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(CharacterForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['readonly'] = True

    class Meta:
        model = Character
        fields = ('name', 'character_main', 'mule_for', 'notes', 'image')
