# Generated by Django 5.0.6 on 2024-06-05 00:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cpasisApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dimensao',
            name='id_eixo',
            field=models.ForeignKey(blank=True, db_column='id_eixo', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='cpasisApp.eixo'),
        ),
    ]
