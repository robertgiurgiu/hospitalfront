# Generated by Django 4.0.3 on 2022-06-08 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0006_remove_patient_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointemnt',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40)),
                ('phone', models.CharField(max_length=40)),
                ('email', models.CharField(max_length=40)),
                ('department', models.CharField(choices=[('Cardiology', 'Cardiology'), ('Emergency ', 'Emergency '), ('Surgery', 'Surgery'), ('ICU', 'ICU '), ('Radiology', 'Radiology')], default='Cardiology', max_length=50)),
                ('doctorName', models.CharField(max_length=40)),
                ('note', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField(default=False)),
            ],
        ),
    ]
