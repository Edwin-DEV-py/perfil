# Generated by Django 4.2.3 on 2023-09-16 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppPerfil', '0003_alter_profile_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=100, unique=True)),
                ('id_carta', models.CharField(max_length=24)),
            ],
        ),
        migrations.RemoveField(
            model_name='profile',
            name='id_carta',
        ),
    ]
