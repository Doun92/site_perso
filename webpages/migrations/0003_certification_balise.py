# Generated by Django 4.0.3 on 2022-05-22 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0002_certification'),
    ]

    operations = [
        migrations.AddField(
            model_name='certification',
            name='balise',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
