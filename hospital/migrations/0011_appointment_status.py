# Generated by Django 4.0.3 on 2022-06-08 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0010_rename_appointemnet_appointment'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
