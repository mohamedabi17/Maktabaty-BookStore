# Generated by Django 4.1.3 on 2023-01-02 05:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_commande_etat'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commande',
            name='etat',
        ),
    ]
