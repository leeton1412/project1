from django.shortcuts import render

# Create your views here.


def index(request):
    """ Render Index.html """
    return render(request, 'home/index.html')