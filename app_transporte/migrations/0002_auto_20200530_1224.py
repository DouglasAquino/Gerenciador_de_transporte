# Generated by Django 3.0.5 on 2020-05-30 15:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_transporte', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='solicitacao',
            options={'ordering': ['solicitante__nome'], 'verbose_name': 'solicitação', 'verbose_name_plural': 'solicitações'},
        ),
    ]
