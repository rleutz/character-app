from django.contrib import admin
from .models import Character, DataType, CharacterData

admin.site.register(Character)
admin.site.register(DataType)
admin.site.register(CharacterData)

# Register your models here.
