from django.http import HttpResponse
from django.shortcuts import render
from .models import StackOverflow
from bs4 import BeautifulSoup
import urllib2


def index(request):
    stacks = StackOverflow.objects.order_by('-question_id')
    return render(request, 'index.html', {'stacks': stacks})



