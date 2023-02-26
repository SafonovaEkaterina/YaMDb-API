# Generated by Django 3.2 on 2023-02-26 13:36

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='title',
            name='year',
            field=models.PositiveSmallIntegerField(validators=[django.core.validators.MaxValueValidator(2023), django.core.validators.MinValueValidator(1900, message='Год выпуска не может быть меньше 1900')], verbose_name='Год выпуска произведения'),
        ),
    ]
