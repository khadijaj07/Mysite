# Generated by Django 5.0.2 on 2024-02-19 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magasin', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produit',
            name='description',
            field=models.TextField(default='Non definie'),
        ),
    ]