# Generated by Django 4.2.3 on 2023-09-13 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppPerfil', '0002_profile_credits'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]