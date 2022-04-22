from django.urls import path, include
# from core.dps.views.result.views import ResultView
# from core.dps.views.quiz.views import QuizView
from core.dps.views.quiz.views import quizview
from core.dps.views.result.views import resultview

app_name = 'dps'

urlpatterns = [
    # quiz
    path('quiz/', quizview, name='quiz'),
    # result
    path('result/', resultview, name='result'),
]
