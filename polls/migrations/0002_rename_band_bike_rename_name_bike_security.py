# Generated by Django 4.2.1 on 2023-05-17 08:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Band',
            new_name='Bike',
        ),
        migrations.RenameField(
            model_name='bike',
            old_name='name',
            new_name='security',
        ),
    ]