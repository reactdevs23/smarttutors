# Generated by Django 5.0.7 on 2024-11-26 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tution', '0006_alter_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='medium',
            field=models.CharField(choices=[('bangla', 'bangla'), ('english', 'english'), ('arabic', 'arabic'), ('urdu', 'urdu'), ('hindi', 'hindi')], default='bangla', max_length=100),
        ),
    ]
