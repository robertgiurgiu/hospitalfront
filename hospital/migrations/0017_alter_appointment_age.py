# Generated by Django 4.0.3 on 2022-06-08 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0016_appointment_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='age',
            field=models.CharField(max_length=3),
        ),
    ]
