# Generated by Django 3.0.2 on 2020-03-01 17:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('character', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CharacterData',
            new_name='CharacterDataSet',
        ),
        migrations.RenameModel(
            old_name='DataTypes',
            new_name='DataType',
        ),
    ]
