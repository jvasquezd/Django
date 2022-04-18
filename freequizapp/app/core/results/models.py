from django.db import models
from core.quizes.models import Quiz
from django.contrib.auth.models import User
from django.forms import model_to_dict


# Create your models here.
class Result(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.FloatField()

    def __str__(self):
        return str(self.pk)

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = 'Result'
        verbose_name_plural = 'Results'
        db_table = 'results'
        ordering = ['id']
