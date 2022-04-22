from datetime import datetime
from secrets import choice

from django.db import models
from django.forms import model_to_dict

from core.dps.choices import gender_choices


# Create your models here.
class Patient(models.Model):
    gender = models.CharField(max_length=10, choices=gender_choices, default='male', verbose_name='Sexo',
                              db_column='pat_gender')
    graduate = models.CharField(max_length=100, verbose_name='Ciclo Academico', db_column='pat_graduate')
    faculty = models.CharField(max_length=100, verbose_name='Facultad')
    civil_status = models.CharField(max_length=100, verbose_name='Estado Civil')
    tfamily = models.CharField(max_length=100, verbose_name='Tipo de Familia')
    age = models.IntegerField(default=18, verbose_name='Edad')
    date_creation = models.DateField(default=datetime.now, verbose_name='Fecha de Creacion',
                                     db_column='pat_date_joined')

    def __str__(self):
        return '{} {} {} {}'.format(self.gender, self.graduate, self.faculty, self.age)

    def toJSON(self):
        item = model_to_dict(self)
        item['gender'] = {'id': self.gender, 'name': self.get_gender_display()}
        return item

    class Meta:
        verbose_name = 'Patient'
        verbose_name_plural = 'Patients'
        db_table = 'patients'
        ordering = ['id']


class BDI(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, verbose_name='Paciente', db_column='pat_id')
    q1 = models.IntegerField()
    q2 = models.IntegerField()
    q3 = models.IntegerField()
    q4 = models.IntegerField()
    q5 = models.IntegerField()
    q6 = models.IntegerField()
    q7 = models.IntegerField()
    q8 = models.IntegerField()
    q9 = models.IntegerField()
    q10 = models.IntegerField()
    q11 = models.IntegerField()
    q12 = models.IntegerField()
    q13 = models.IntegerField()
    q14 = models.IntegerField()
    q15 = models.IntegerField()
    q16 = models.IntegerField()
    q17 = models.IntegerField()
    q18 = models.IntegerField()
    q19 = models.IntegerField()
    q20 = models.IntegerField()
    q21 = models.IntegerField()
    score = models.IntegerField()
    class_dep = models.IntegerField()

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = 'BDI'
        verbose_name_plural = 'BDIs'
        db_table = 'bdis'
        ordering = ['id']


class Sack(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, verbose_name='Paciente', db_column='pat_id')
    s1 = models.TextField()
    s2 = models.TextField()
    s3 = models.TextField()
    s4 = models.TextField()
    s5 = models.TextField()
    s6 = models.TextField()
    s7 = models.TextField()
    s8 = models.TextField()
    s9 = models.TextField()
    s10 = models.TextField()
    s11 = models.TextField()
    s12 = models.TextField()
    s13 = models.TextField()
    s14 = models.TextField()
    s15 = models.TextField()
    s16 = models.TextField()
    s17 = models.TextField()
    s18 = models.TextField()
    s19 = models.TextField()
    s20 = models.TextField()
    s21 = models.TextField()
    s22 = models.TextField()
    s23 = models.TextField()
    s24 = models.TextField()

    class Meta:
        verbose_name = 'Sack'
        verbose_name_plural = 'Sacks'
        db_table = 'sacks'
        ordering = ['id']
