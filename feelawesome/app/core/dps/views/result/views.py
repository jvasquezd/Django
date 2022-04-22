from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView

"""
class ResultView(TemplateView):
    template_name = 'result/predict.html'

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            sx = request.POST['data']
            data['data'] = sx
            print(sx)
        except Exception as e:
            data['error'] = str(e)
        # context = self.get_context_data(**kwargs)
        return render(request, 'result/predict.html', data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        context['title'] = "Predicting Depression"
        return context
"""


def resultview(request):
    data = request.POST
    print(data)
    message = "Sexo {}".format(request.POST['sx'])
    return render(request, 'result/predict.html', {'message': message})
