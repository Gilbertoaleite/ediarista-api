# Generated by Django 3.2.8 on 2021-10-14 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_auto_20211013_2214'),
    ]

    operations = [
        migrations.AddField(
            model_name='diarista',
            name='cidade',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]