from django.conf import settings
from django.db import models
from django.utils import timezone

class Character(models.Model):

    GROUP_ROLE = (
        ('DPS', 'DPS'),
        ('Tank', 'Tank'),
        ('Healer', 'Healer')
    )

    slug = models.SlugField(unique=True, max_length=255)
    name = models.CharField(max_length=255, null=True, blank=True)
    player = models.CharField(max_length=255, null=True, blank=True)
    mule_for = models.CharField(max_length=255, null=True, blank=True)
    character_main = models.BooleanField(default=False)
    notes = models.TextField(null=True, blank=True)
    gender = models.CharField(max_length=255, null=True, blank=True)
    level = models.PositiveIntegerField(null=True, blank=True)
    character_class = models.CharField(max_length=255, null=True, blank=True)
    race = models.CharField(max_length=255, null=True, blank=True)
    alliance = models.CharField(max_length=255, null=True, blank=True)
    health = models.PositiveIntegerField(null=True, blank=True)
    magicka = models.PositiveIntegerField(null=True, blank=True)
    stamina = models.PositiveIntegerField(null=True, blank=True)
    image = models.ImageField(upload_to='profile_image', blank=True)
    group_role = models.CharField(max_length=6, null=True, blank=True, choices=GROUP_ROLE)

    def get_absolute_url(self):
        return reverse(
            'character_detail',
            args=[self.slug])

    def __str__(self):
        return self.slug

    class Meta:
        ordering = ['-character_main', 'slug']

class CharacterData(models.Model):
    data_value = models.CharField(max_length=255)
    data_type_name = models.CharField(max_length=50)
    data_type_category = models.CharField(max_length=50)
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    value_is_number = models.BooleanField(default=False)

    def __str__(self):
        return self.data_value

    class Meta:
        ordering = ['data_type_category', 'data_type_name']
