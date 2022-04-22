from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from sklearn.metrics import accuracy_score
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from core.dps.dpsmodels import PredictionDepressionModel

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

    bdi1 = int(request.POST['bdi1'])
    bdi2 = int(request.POST['bdi2'])
    bdi3 = int(request.POST['bdi3'])
    bdi4 = int(request.POST['bdi4'])
    bdi5 = int(request.POST['bdi5'])
    bdi6 = int(request.POST['bdi6'])
    bdi7 = int(request.POST['bdi7'])
    bdi8 = int(request.POST['bdi8'])
    bdi9 = int(request.POST['bdi9'])
    bdi10 = int(request.POST['bdi10'])
    bdi11 = int(request.POST['bdi11'])
    bdi12 = int(request.POST['bdi12'])
    bdi13 = int(request.POST['bdi13'])
    bdi14 = int(request.POST['bdi14'])
    bdi15 = int(request.POST['bdi15'])
    bdi16 = int(request.POST['bdi16'])
    bdi17 = int(request.POST['bdi17'])
    bdi18 = int(request.POST['bdi18'])
    bdi19 = int(request.POST['bdi19'])
    bdi20 = int(request.POST['bdi20'])
    bdi21 = int(request.POST['bdi21'])

    values = [bdi1, bdi2, bdi3, bdi4, bdi5, bdi6, bdi7, bdi8, bdi9, bdi10, bdi11, bdi12, bdi13, bdi14, bdi15, bdi16,
              bdi17, bdi18, bdi19, bdi20, bdi21,
              bdi1 + bdi2 + bdi3 + bdi4 + bdi5 + bdi6 + bdi7 + bdi8 + bdi9 + bdi10 + bdi11 + bdi12 + bdi13 + bdi14 + bdi15 + bdi16 +
              bdi17 + bdi18 + bdi19 + bdi20 + bdi21]
    predictionbdimodel = PredictionDepressionModel()
    classifier = predictionbdimodel.decisionTree_classifier()
    prediction = classifier.predict([values])

    if prediction[0] == 1:
        result = 'Depresion Minima'
    if prediction[0] == 2:
        result = 'Depresion Leve'
    if prediction[0] == 3:
        result = 'Depresion Moderada'
    if prediction[0] == 4:
        result = 'Depresion Grave'

    # print(predictionbdimodel.accuracy(predictionbdimodel.svm_classifier()))
    # message = "Sexo {}".format(request.POST['sx'])
    return render(request, 'result/predict.html', {'message': result})
