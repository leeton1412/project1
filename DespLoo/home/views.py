from django.shortcuts import render

# Create your views here.


def home(request):
    """ Render Index.html """
    return render(request, 'home/index.html')