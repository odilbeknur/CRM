# Generated by Django 5.1.4 on 2024-12-18 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='type',
            field=models.CharField(choices=[('g', 'Г'), ('b', 'ЮЛ'), ('f', 'ФЛ')], max_length=1, verbose_name='Тип клиента'),
        ),
    ]