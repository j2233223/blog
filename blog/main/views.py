from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.
def main(request):
    now = datetime.datetime.now() 
    context = {'like':'Django 很棒','now':now}
    return render(request, 'main/main.html', context)


def about(request):
    '''
    Render the about page
    '''
    return render(request, 'main/about.html')