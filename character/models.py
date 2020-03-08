from django.conf import settings
from django.db import models
from django.utils import timezone

class Character(models.Model):
    slug = models.SlugField(unique=True, max_length=255)

    def get_absolute_url(self):
        return reverse(
            'character_detail',
            args=[self.slug])

    def __str__(self):
        return self.slug

    class Meta:
        ordering = ['slug']

class CharacterData(models.Model):
    data_value = models.CharField(max_length=255)
    data_type_name = models.CharField(max_length=50)
    data_type_category = models.CharField(max_length=50)
    character = models.ForeignKey(Character, on_delete=models.CASCADE)

    def __str__(self):
        return self.data_value

    class Meta:
        ordering = ['data_value']
