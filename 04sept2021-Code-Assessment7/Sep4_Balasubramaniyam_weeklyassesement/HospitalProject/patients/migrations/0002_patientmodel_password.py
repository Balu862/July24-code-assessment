# Generated by Django 3.2.6 on 2021-09-04 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='patientmodel',
            name='password',
            field=models.CharField(default=None, max_length=50),
        ),
    ]
