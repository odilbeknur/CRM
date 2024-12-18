# Generated by Django 5.1.4 on 2024-12-18 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='doorphone',
        ),
        migrations.AddField(
            model_name='location',
            name='landmark',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Ориентир'),
        ),
    ]
