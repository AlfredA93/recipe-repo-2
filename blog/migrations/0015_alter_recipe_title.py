# Generated by Django 3.2.20 on 2023-08-19 15:54

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_alter_recipe_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='title',
            field=models.CharField(max_length=140, unique=True, validators=[django.core.validators.RegexValidator(code='invalid_title', message='Title must be Alphanumeric', regex='^[0-9a-zA-Z\\s]*$')]),
        ),
    ]