# Generated by Django 5.1.4 on 2024-12-18 17:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tickets', '0008_alter_ticket_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Finance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction', models.CharField(max_length=100, unique=True, verbose_name='Транзакция')),
                ('full_cost', models.FloatField(verbose_name='Полная стоимость')),
                ('remain', models.FloatField(verbose_name='Остаток')),
                ('sum', models.FloatField(verbose_name='Сумма')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('ticket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payments', to='tickets.ticket', verbose_name='Заявка')),
            ],
            options={
                'verbose_name': 'Платеж',
                'verbose_name_plural': 'Платежи',
            },
        ),
    ]