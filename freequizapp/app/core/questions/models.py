from django.db import models
from core.quizes.models import Quiz
from django.forms import model_to_dict


# Create your models here.
class Question(models.Model):
    text = models.CharField(max_length=200)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.text)

    def toJSON(self):
        item = model_to_dict(self)
        return item

    def get_answers(self):
        return self.answer_set.all()

    class Meta:
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'
        db_table = 'questions'
        ordering = ['id']


class Answer(models.Model):
    text = models.CharField(max_length=200)
    correct = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"question: {self.question.text}, answer: {self.text}, correct: {self.correct}"

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = 'Answer'
        verbose_name_plural = 'Answers'
        db_table = 'answers'
        ordering = ['id']
