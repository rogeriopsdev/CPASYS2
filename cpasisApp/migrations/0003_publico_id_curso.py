# Generated by Django 5.0.6 on 2024-06-05 11:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cpasisApp', '0002_dimensao_id_eixo'),
    ]

    operations = [
        migrations.AddField(
            model_name='publico',
            name='id_curso',
            field=models.ForeignKey(blank=True, db_column='id_curso', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='cpasisApp.curso'),
        ),
    ]
