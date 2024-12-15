# Generated by Django 5.1.4 on 2024-12-15 17:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
        ('tickets', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='measurement',
            name='ticket',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='measurement', to='tickets.ticket', verbose_name='Заявка'),
        ),
        migrations.AddIndex(
            model_name='product',
            index=models.Index(fields=['name', 'type'], name='products_pr_name_522359_idx'),
        ),
        migrations.AddField(
            model_name='measurement',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='measurements', to='products.product', verbose_name='Продукция'),
        ),
        migrations.AddIndex(
            model_name='measurement',
            index=models.Index(fields=['ticket', 'product'], name='products_me_ticket__3fa268_idx'),
        ),
    ]
