# Generated by Django 4.0.3 on 2022-06-06 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0004_doctor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='department',
            field=models.CharField(choices=[('Cardiologist', 'Cardiologist'), ('Emergency Doctor', 'Emergency Doctor'), ('Surgeon', 'Surgeon'), ('ICU Doctor', 'ICU Doctor'), ('Radiologist', 'Radiologist')], default='Cardiologist', max_length=50),
        ),
        migrations.AlterField(
            model_name='patient',
            name='department',
            field=models.CharField(choices=[('Cardiology', 'Cardiology'), ('Emergency ', 'Emergency '), ('Surgery', 'Surgery'), ('ICU', 'ICU '), ('Radiology', 'Radiology')], default='Cardiology', max_length=50),
        ),
    ]
