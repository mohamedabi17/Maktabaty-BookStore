# Generated by Django 4.1.3 on 2023-01-02 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_remove_commande_etat'),
    ]

    operations = [
        migrations.AddField(
            model_name='commande',
            name='etat',
            field=models.CharField(default='pending', max_length=100),
            preserve_default=False,
        ),
    ]
