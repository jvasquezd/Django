from datetime import datetime
from statistics import mode
from django.utils import timezone
from django.db import models
from django.forms import model_to_dict

from config.settings import MEDIA_URL, STATIC_URL
from core.courses.choices import gender_choices
from core.models import BaseModel
from django.db.models.fields.related import ManyToManyField



def thumbnail_directory_path(instance, filename):
    return 'courses/{0}/{1}'.format(instance.title,filename)

def chapter_directory_path(instance, filename):
    return 'courses/{0}/{1}/{2}'.format(instance.course,instance.title, filename)

def lesson_directory_path(instance, filename):
    return 'courses/{0}/{1}/Lesson #{2}: {3}/{4}'.format(instance.course,instance.chapter. instance.lesson_number,instance.title, filename)


# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=150, verbose_name='Nombre')
    last_name = models.CharField(max_length=100, verbose_name='Apellido')
    gender = models.CharField(max_length=10,choices=gender_choices, default='male', verbose_name='Sexo')
    
    
class Course(models.Model):
    authors = ManyToManyField(Author)
    title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=100)
    thumbnail=models.ImageField(upload_to=thumbnail_directory_path, null=True, blank=True, verbose_name='Imagen')
    video=models.FileField(upload_to=thumbnail_directory_path, null=True, blank=True, verbose_name='Video')
    vimeo=models.CharField(max_length=100, verbose_name='Vimeo Video ID (Optional)',blank=True, null=True)
    slug=models.SlugField(max_length=250, unique_for_date='published', null=False, unique=True, verbose_name='Slug')
    published=models.DateField(default=timezone.now)
    is_active=models.BooleanField(default=True)
    
    class Meta:
        ordering = ('-published',)
        
    def __str__(self):
        return self.title


class Chapter(models.Model):
    course=models.ForeignKey(Course, on_delete=models.CASCADE, blank=True, null=True)
    chapter_number=models.IntegerField(blank=True, null=True)
    title=models.CharField(max_length=255)
    thumbnail=models.ImageField(upload_to=chapter_directory_path, null=True, blank=True, verbose_name='Imagen')
    video=models.FileField(upload_to=chapter_directory_path, null=True, blank=True, verbose_name='Video')
    vimeo=models.CharField(max_length=100, verbose_name='Vimeo Video ID (Optional)',blank=True, null=True)
    content=models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.title

class Lesson(models.Model):
    course=models.ForeignKey(Course, on_delete=models.CASCADE, blank=True, null=True)
    chapter=models.ForeignKey(Chapter, on_delete=models.CASCADE, blank=True, null=True)
    lesson_number=models.IntegerField(blank=True, null=True)
    title=models.CharField(max_length=255)
    thumbnail=models.ImageField(upload_to=chapter_directory_path, null=True, blank=True, verbose_name='Imagen')
    video=models.FileField(upload_to=chapter_directory_path, null=True, blank=True, verbose_name='Video')
    vimeo=models.CharField(max_length=100, verbose_name='Vimeo Video ID (Optional)',blank=True, null=True)
    content=models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.title