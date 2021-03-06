# Generated by Django 4.0.3 on 2022-04-11 23:36

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(choices=[('male', 'Masculino'), ('female', 'Femenino')], db_column='pat_gender', default='male', max_length=10, verbose_name='Sexo')),
                ('graduate', models.CharField(db_column='pat_graduate', max_length=100, verbose_name='Ciclo Academico')),
                ('faculty', models.CharField(max_length=100, verbose_name='Facultad')),
                ('civil_status', models.CharField(max_length=100, verbose_name='Estado Civil')),
                ('tfamily', models.CharField(max_length=100, verbose_name='Tipo de Familia')),
                ('age', models.IntegerField(default=18, verbose_name='Edad')),
                ('date_creation', models.DateField(db_column='pat_date_joined', default=datetime.datetime.now, verbose_name='Fecha de Creacion')),
            ],
            options={
                'verbose_name': 'Patient',
                'verbose_name_plural': 'Patients',
                'db_table': 'patients',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Sacks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient', models.ForeignKey(db_column='pat_id', on_delete=django.db.models.deletion.CASCADE, to='dps.patient', verbose_name='Paciente')),
            ],
        ),
        migrations.CreateModel(
            name='BDI',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('q1', models.IntegerField(default=0)),
                ('q2', models.IntegerField()),
                ('q3', models.IntegerField()),
                ('q4', models.IntegerField()),
                ('q5', models.IntegerField()),
                ('q6', models.IntegerField()),
                ('q7', models.IntegerField()),
                ('q8', models.IntegerField()),
                ('q9', models.IntegerField()),
                ('q10', models.IntegerField()),
                ('q11', models.IntegerField()),
                ('q12', models.IntegerField()),
                ('q13', models.IntegerField()),
                ('q14', models.IntegerField()),
                ('q15', models.IntegerField()),
                ('q16', models.IntegerField()),
                ('q17', models.IntegerField()),
                ('q18', models.IntegerField()),
                ('q19', models.IntegerField()),
                ('q20', models.IntegerField()),
                ('q21', models.IntegerField()),
                ('score', models.IntegerField()),
                ('class_dep', models.IntegerField()),
                ('patient', models.ForeignKey(db_column='pat_id', on_delete=django.db.models.deletion.CASCADE, to='dps.patient', verbose_name='Paciente')),
            ],
            options={
                'verbose_name': 'BDI',
                'verbose_name_plural': 'BDIs',
                'db_table': 'bdis',
                'ordering': ['id'],
            },
        ),
    ]
