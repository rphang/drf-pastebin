# Generated by Django 4.2.4 on 2023-08-20 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pastes', '0002_paste_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paste',
            name='slug',
            field=models.SlugField(editable=False, max_length=100, unique=True),
        ),
    ]
