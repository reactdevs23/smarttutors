# Generated by Django 5.0.7 on 2024-11-24 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tution', '0002_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.CharField(default=models.CharField(max_length=100), max_length=100),
        ),
    ]
