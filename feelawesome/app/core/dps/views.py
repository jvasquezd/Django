from django.shortcuts import render

# Create your views here.
def myfirstview(request):
    data={
        'name':'Wiliam'
    }
    return render(request,'index.html', data)