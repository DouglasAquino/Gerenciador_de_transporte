# Generated by Django 3.0.5 on 2020-05-30 15:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, max_length=128, null=True, verbose_name='Nome')),
                ('sigla', models.CharField(blank=True, max_length=10, null=True, verbose_name='Sigla')),
            ],
        ),
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, max_length=128, null=True, verbose_name='Nome')),
            ],
        ),
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, max_length=128, null=True, verbose_name='Nome')),
                ('matricula', models.CharField(blank=True, max_length=10, null=True, verbose_name='Matricula')),
                ('cargo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app_transporte.Cargo')),
                ('departamento', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app_transporte.Departamento')),
                ('usuario', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Veiculo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(blank=True, max_length=150, null=True, verbose_name='Descrição')),
                ('modelo', models.CharField(blank=True, max_length=100, null=True, verbose_name='Modelo')),
                ('placa', models.CharField(blank=True, max_length=10, null=True, verbose_name='Placa')),
            ],
        ),
        migrations.CreateModel(
            name='Solicitacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('origem', models.CharField(blank=True, max_length=150, null=True, verbose_name='Origem')),
                ('destino', models.CharField(blank=True, max_length=150, null=True, verbose_name='Destino')),
                ('data_hora', models.DateTimeField(auto_now_add=True, verbose_name='data da solicitação')),
                ('solicitante', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app_transporte.Funcionario')),
            ],
        ),
        migrations.CreateModel(
            name='Atendimento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_hora', models.DateTimeField(blank=True, max_length=128, null=True, verbose_name='Horario do atendimento')),
                ('motorista', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app_transporte.Funcionario')),
                ('solicitacao', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app_transporte.Solicitacao')),
                ('veiculo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app_transporte.Veiculo')),
            ],
        ),
    ]
