from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView

"""
class QuizView(TemplateView):
    template_name = 'quiz/instrument.html'
    success_url = reverse_lazy('dps:result')
    url_redirect = success_url

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            sx = request.POST['sx']
            data['sx'] = sx
            print(sx)
        except Exception as e:
            data['error'] = str(e)
        # context = self.get_context_data(**kwargs)
        return render(request, 'result/predict.html', data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "5MinTest Quiz"
        return context
"""


def quizview(request):
    return render(request, "quiz/instrument.html")
