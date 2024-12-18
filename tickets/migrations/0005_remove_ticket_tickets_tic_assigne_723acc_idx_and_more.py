# Generated by Django 5.1.4 on 2024-12-18 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0004_ticket_ads_info'),
        ('users', '0003_rename_sex_person_gender'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='ticket',
            name='tickets_tic_assigne_723acc_idx',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='assigned_employee',
        ),
        migrations.AddIndex(
            model_name='ticket',
            index=models.Index(fields=['created_by'], name='tickets_tic_created_d1df98_idx'),
        ),
    ]