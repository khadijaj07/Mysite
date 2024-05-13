# Generated by Django 5.0.2 on 2024-03-11 11:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magasin', '0008_commande'),
    ]

    operations = [
        migrations.RenameField(
            model_name='commande',
            old_name='produits',
            new_name='Produits',
        ),
        migrations.AlterField(
            model_name='commande',
            name='dateCde',
            field=models.DateField(default=datetime.date(2024, 3, 11), null=True),
        ),
    ]
