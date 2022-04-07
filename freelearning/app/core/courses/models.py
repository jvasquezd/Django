from datetime import datetime

from django.db import models
from django.forms import model_to_dict

from config.settings import MEDIA_URL, STATIC_URL
from core.courses.choices import gender_choices
from core.models import BaseModel
from django.db.models.fields.related import ManyToManyField



def thumbnail_directory_path(instance, filename):
    return 'courses/{0}/{1}'.format(instance.title,filename)

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=150, verbose_name='Nombre')
    last_name = models.CharField(max_length=100, verbose_name='Apellido')
    gender = models.CharField(max_length=10,choices=gender_choices, default='male', verbose_name='Sexo')
    
    
class Course(models.Model):
    authors = ManyToManyField(Author)
    title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=100)
    thumbnail=models.ImageField(upload_to='courses/%Y/%m/%d', null=True, blank=True, verbose_name='Imagen')
    video=models.FileField(upload_to='videos/%Y/%m/%d', null=True, blank=True, verbose_name='Video')
    vimeo=models.CharField(max_length=100, verbose_name='Vimeo Video ID (Optional)')

class Chapter(models.Model):
    pass

class Lesson(models.Model):
    pass