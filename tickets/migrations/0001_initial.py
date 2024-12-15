# Generated by Django 5.1.4 on 2024-12-15 17:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название этапа')),
                ('priority', models.PositiveIntegerField(verbose_name='Приоритет этапа')),
            ],
            options={
                'verbose_name': 'Этап',
                'verbose_name_plural': 'Этапы',
                'ordering': ['priority'],
            },
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('status', models.CharField(choices=[('new', 'Новая'), ('in_progress', 'В работе'), ('completed', 'Завершена')], default='new', max_length=20, verbose_name='Статус заявки')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('assigned_employee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='assigned_tickets', to='users.employee', verbose_name='Назначенный сотрудник')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tickets', to='users.client', verbose_name='Клиент')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_tickets', to='users.employee', verbose_name='Создатель заявки')),
            ],
            options={
                'verbose_name': 'Заявка',
                'verbose_name_plural': 'Заявки',
            },
        ),
        migrations.CreateModel(
            name='StageHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('completed_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата завершения')),
                ('performed_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='performed_stages', to='users.employee', verbose_name='Ответственный сотрудник')),
                ('stage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stage_histories', to='tickets.stage', verbose_name='Этап')),
                ('ticket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stage_history', to='tickets.ticket', verbose_name='Заявка')),
            ],
            options={
                'verbose_name': 'История этапов',
                'verbose_name_plural': 'История этапов',
            },
        ),
        migrations.AddIndex(
            model_name='ticket',
            index=models.Index(fields=['status'], name='tickets_tic_status_0e5646_idx'),
        ),
        migrations.AddIndex(
            model_name='ticket',
            index=models.Index(fields=['assigned_employee'], name='tickets_tic_assigne_723acc_idx'),
        ),
        migrations.AddIndex(
            model_name='stagehistory',
            index=models.Index(fields=['ticket', 'stage'], name='tickets_sta_ticket__c93a07_idx'),
        ),
    ]