# Generated by Django 4.0.3 on 2022-06-08 11:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0008_remove_appointemnt_status'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Appointemnt',
            new_name='Appointemnet',
        ),
    ]