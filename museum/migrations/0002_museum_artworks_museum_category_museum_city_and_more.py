# Generated by Django 5.1.1 on 2024-09-17 15:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artwork', '0001_initial'),
        ('museum', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='museum',
            name='artworks',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='artwork.artwork'),
        ),
        migrations.AddField(
            model_name='museum',
            name='category',
            field=models.CharField(default='Unknown Category', max_length=50),
        ),
        migrations.AddField(
            model_name='museum',
            name='city',
            field=models.CharField(default='Unknown City', max_length=50),
        ),
        migrations.AddField(
            model_name='museum',
            name='country',
            field=models.CharField(default='Unknown Country', max_length=50),
        ),
        migrations.AddField(
            model_name='museum',
            name='description',
            field=models.CharField(default='Unknown Description', max_length=50),
        ),
        migrations.AddField(
            model_name='museum',
            name='latitud',
            field=models.DecimalField(decimal_places=5, default=None, max_digits=20),
        ),
        migrations.AddField(
            model_name='museum',
            name='longitud',
            field=models.DecimalField(decimal_places=5, default=None, max_digits=20),
        ),
        migrations.AlterField(
            model_name='museum',
            name='name',
            field=models.CharField(default=None, max_length=50),
        ),
    ]
